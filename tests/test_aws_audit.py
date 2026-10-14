from __future__ import annotations

import unittest
import csv
import json
from contextlib import redirect_stderr
from io import StringIO
from unittest.mock import patch
from pathlib import Path

from botocore.exceptions import ClientError

from scripts.aws_audit.audit import build_report, report_exit_code
from scripts.aws_audit.cli import _csv_rows, main


def api_error(code: str) -> ClientError:
    return ClientError(
        {"Error": {"Code": code, "Message": "synthetic test response"}}, "SyntheticCall"
    )


class Paginator:
    def __init__(self, pages: list[dict]) -> None:
        self.pages = pages

    def paginate(self, **_kwargs):
        return iter(self.pages)


class FakeClient:
    def __init__(self, *, pages=None, responses=None, errors=None) -> None:
        self.pages = pages or {}
        self.responses = responses or {}
        self.errors = errors or {}

    def get_paginator(self, operation: str) -> Paginator:
        if operation in self.errors:
            raise self.errors[operation]
        return Paginator(self.pages.get(operation, []))

    def __getattr__(self, name: str):
        if name in self.errors:
            raise self.errors[name]

        def call(**_kwargs):
            response = self.responses.get(name)
            if isinstance(response, Exception):
                raise response
            return response or {}

        return call


class FakeSession:
    def __init__(self, clients: dict[tuple[str, str], FakeClient]) -> None:
        self.clients = clients

    def client(self, service: str, *, region_name: str) -> FakeClient:
        return self.clients[(service, region_name)]


def clean_s3_client() -> FakeClient:
    return FakeClient(
        responses={
            "get_bucket_tagging": {
                "TagSet": [{"Key": "Owner"}, {"Key": "Environment"}, {"Key": "Project"}]
            },
            "get_public_access_block": {
                "PublicAccessBlockConfiguration": {
                    "BlockPublicAcls": True,
                    "IgnorePublicAcls": True,
                    "BlockPublicPolicy": True,
                    "RestrictPublicBuckets": True,
                }
            },
            "get_bucket_policy_status": {"PolicyStatus": {"IsPublic": False}},
            "get_bucket_acl": {"Grants": []},
        }
    )


class AwsAuditTests(unittest.TestCase):
    def session(
        self, *, ec2: FakeClient | None = None, bucket_client: FakeClient | None = None
    ) -> FakeSession:
        inventory = FakeClient(
            pages={
                "list_buckets": [
                    {"Buckets": [{"Name": "portfolio-example", "BucketRegion": "ap-south-1"}]}
                ]
            }
        )
        return FakeSession(
            {
                ("ec2", "ap-south-1"): ec2 or FakeClient(),
                ("s3", "us-east-1"): inventory,
                ("s3", "ap-south-1"): bucket_client or clean_s3_client(),
            }
        )

    def test_clean_synthetic_resources_are_reported_as_pass_without_aws_calls(self) -> None:
        tags = [{"Key": "Owner"}, {"Key": "Environment"}, {"Key": "Project"}]
        ec2 = FakeClient(
            pages={
                "describe_instances": [
                    {"Reservations": [{"Instances": [{"InstanceId": "i-example", "Tags": tags}]}]}
                ],
                "describe_security_groups": [
                    {
                        "SecurityGroups": [
                            {"GroupId": "sg-example", "Tags": tags, "IpPermissions": []}
                        ]
                    }
                ],
            }
        )
        report = build_report(
            self.session(ec2=ec2),
            region="ap-south-1",
            required_tags=("Owner", "Environment", "Project"),
        )
        self.assertEqual(8, report["summary"]["PASS"])
        self.assertEqual(0, report["summary"]["FINDING"])
        self.assertEqual(0, report["summary"]["UNKNOWN"])
        self.assertEqual(0, report["summary"]["NOT_CONFIGURED"])
        self.assertEqual(0, report_exit_code(report))

    def test_reports_wide_ipv4_and_ipv6_ingress_and_missing_tag_keys(self) -> None:
        ec2 = FakeClient(
            pages={
                "describe_instances": [
                    {"Reservations": [{"Instances": [{"InstanceId": "i-example", "Tags": []}]}]}
                ],
                "describe_security_groups": [
                    {
                        "SecurityGroups": [
                            {
                                "GroupId": "sg-example",
                                "Tags": [{"Key": "Owner"}],
                                "IpPermissions": [
                                    {
                                        "IpProtocol": "tcp",
                                        "FromPort": 22,
                                        "ToPort": 22,
                                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                                    },
                                    {"IpProtocol": "-1", "Ipv6Ranges": [{"CidrIpv6": "::/0"}]},
                                ],
                            }
                        ]
                    }
                ],
            }
        )
        report = build_report(
            self.session(ec2=ec2), region="ap-south-1", required_tags=("Owner", "Environment")
        )
        ingress = next(
            row for row in report["findings"] if row["check_id"] == "security-group-wide-ingress"
        )
        self.assertEqual("FINDING", ingress["status"])
        self.assertEqual(
            ["0.0.0.0/0", "::/0"], [rule["address"] for rule in ingress["details"]["rules"]]
        )
        missing_tags = [row for row in report["findings"] if row["check_id"] == "required-tags"]
        self.assertEqual(3, len(missing_tags))
        self.assertEqual(2, sum(row["status"] == "FINDING" for row in missing_tags))
        self.assertEqual(1, report_exit_code(report))

    def test_missing_s3_controls_and_api_denial_are_never_reported_as_pass(self) -> None:
        bucket = FakeClient(
            responses={
                "get_bucket_tagging": api_error("NoSuchTagSet"),
                "get_public_access_block": api_error("NoSuchPublicAccessBlockConfiguration"),
                "get_bucket_policy_status": api_error("NoSuchBucketPolicy"),
                "get_bucket_acl": api_error("AccessDenied"),
            }
        )
        report = build_report(
            self.session(bucket_client=bucket), region="ap-south-1", required_tags=("Owner",)
        )
        by_id = {row["check_id"]: row for row in report["findings"]}
        self.assertEqual("FINDING", by_id["required-tags"]["status"])
        self.assertEqual("NOT_CONFIGURED", by_id["s3.public-access-block"]["status"])
        self.assertEqual("NOT_CONFIGURED", by_id["s3.bucket-policy-public-status"]["status"])
        self.assertEqual("UNKNOWN", by_id["s3.bucket-acl-wide-grants"]["status"])
        self.assertEqual(
            "AccessDenied", by_id["s3.bucket-acl-wide-grants"]["details"]["error_code"]
        )
        self.assertEqual(2, report_exit_code(report))

    def test_reports_public_bucket_policy_and_broad_acl_group(self) -> None:
        bucket = FakeClient(
            responses={
                "get_bucket_tagging": {"TagSet": [{"Key": "Owner"}]},
                "get_public_access_block": {
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": True,
                        "IgnorePublicAcls": True,
                        "BlockPublicPolicy": False,
                        "RestrictPublicBuckets": True,
                    }
                },
                "get_bucket_policy_status": {"PolicyStatus": {"IsPublic": True}},
                "get_bucket_acl": {
                    "Grants": [
                        {
                            "Grantee": {
                                "Type": "Group",
                                "URI": "http://acs.amazonaws.com/groups/global/AllUsers",
                            },
                            "Permission": "READ",
                        }
                    ]
                },
            }
        )
        report = build_report(
            self.session(bucket_client=bucket), region="ap-south-1", required_tags=("Owner",)
        )
        by_id = {row["check_id"]: row for row in report["findings"]}
        self.assertEqual("FINDING", by_id["s3.public-access-block"]["status"])
        self.assertEqual(
            ["BlockPublicPolicy"], by_id["s3.public-access-block"]["details"]["disabled_settings"]
        )
        self.assertEqual("FINDING", by_id["s3.bucket-policy-public-status"]["status"])
        self.assertEqual("FINDING", by_id["s3.bucket-acl-wide-grants"]["status"])
        self.assertEqual(
            "AllUsers", by_id["s3.bucket-acl-wide-grants"]["details"]["grants"][0]["group"]
        )
        self.assertEqual(1, report_exit_code(report))

    def test_collection_api_failure_is_unknown_and_does_not_stop_other_services(self) -> None:
        ec2 = FakeClient(errors={"describe_instances": api_error("UnauthorizedOperation")})
        report = build_report(self.session(ec2=ec2), region="ap-south-1", required_tags=("Owner",))
        instance_check = next(
            row for row in report["findings"] if row["check_id"] == "ec2.instances.list"
        )
        self.assertEqual("UNKNOWN", instance_check["status"])
        self.assertEqual("UnauthorizedOperation", instance_check["details"]["error_code"])
        self.assertTrue(
            any(row["resource_id"] == "portfolio-example" for row in report["findings"])
        )
        self.assertEqual(2, report_exit_code(report))

    def test_csv_rows_are_flat_and_cli_requires_sensitive_output_acknowledgement(self) -> None:
        report = build_report(self.session(), region="ap-south-1", required_tags=("Owner",))
        rows = _csv_rows(report)
        self.assertTrue(rows)
        self.assertEqual(
            {
                "check_id",
                "resource_type",
                "resource_id",
                "region",
                "status",
                "summary",
                "details_json",
            },
            set(rows[0]),
        )
        sample_path = Path(__file__).resolve().parents[1] / "samples/aws-audit-report.csv"
        with sample_path.open(encoding="utf-8", newline="") as stream:
            sample_rows = list(csv.DictReader(stream))
        self.assertEqual(2, len(sample_rows))
        self.assertEqual("FINDING", sample_rows[0]["status"])
        sample_json = sample_path.with_suffix(".json")
        fixture = json.loads(sample_json.read_text(encoding="utf-8"))
        self.assertEqual(1, fixture["exit_code"])
        self.assertIn("Synthetic sample only", fixture["limitations"][0])
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit) as raised:
            main(["--region", "ap-south-1", "--json-output", "audit.json"])
        self.assertEqual(2, raised.exception.code)

    def test_bucket_region_uses_list_buckets_region_without_location_lookup(self) -> None:
        inventory = self.session().clients[("s3", "us-east-1")]
        with patch.object(
            inventory,
            "get_bucket_location",
            side_effect=AssertionError("unexpected lookup"),
            create=True,
        ):
            report = build_report(self.session(), region="ap-south-1", required_tags=("Owner",))
        bucket_region = next(
            row for row in report["findings"] if row["check_id"] == "s3.bucket.region"
        )
        self.assertEqual("ap-south-1", bucket_region["region"])


if __name__ == "__main__":
    unittest.main()
