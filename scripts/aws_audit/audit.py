"""Collect a small, read-only AWS posture snapshot.

This tool reports individual observations; it is not a complete security or IAM
evaluator. AWS API failures are represented as UNKNOWN rather than as passes.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

from botocore.exceptions import BotoCoreError, ClientError


PUBLIC_GROUP_URIS = {
    "http://acs.amazonaws.com/groups/global/AllUsers": "AllUsers",
    "http://acs.amazonaws.com/groups/global/AuthenticatedUsers": "AuthenticatedUsers",
}
NO_PUBLIC_POLICY_CODES = {"NoSuchBucketPolicy", "NoSuchPolicy"}
NO_PUBLIC_ACCESS_BLOCK_CODES = {"NoSuchPublicAccessBlockConfiguration"}
ACTIVE_INSTANCE_STATES = ["pending", "running", "stopping", "stopped"]


@dataclass(frozen=True)
class Finding:
    check_id: str
    resource_type: str
    resource_id: str
    region: str
    status: str
    summary: str
    details: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _error_code(error: Exception) -> str:
    if isinstance(error, ClientError):
        return str(error.response.get("Error", {}).get("Code", "UnknownClientError"))
    if isinstance(error, BotoCoreError):
        return type(error).__name__
    return type(error).__name__


def _unknown(
    check_id: str,
    resource_type: str,
    resource_id: str,
    region: str,
    error: Exception,
) -> Finding:
    code = _error_code(error)
    return Finding(
        check_id,
        resource_type,
        resource_id,
        region,
        "UNKNOWN",
        f"AWS API check could not be completed ({code}).",
        {"error_code": code},
    )


def _exception_codes(error: ClientError) -> str:
    return str(error.response.get("Error", {}).get("Code", "UnknownClientError"))


def _tag_finding(
    resource_type: str,
    resource_id: str,
    region: str,
    tags: list[dict[str, str]],
    required_tags: tuple[str, ...],
) -> Finding:
    present = {tag["Key"] for tag in tags if isinstance(tag.get("Key"), str)}
    missing = [key for key in required_tags if key not in present]
    status = "FINDING" if missing else "PASS"
    summary = (
        f"Missing required tag key(s): {', '.join(missing)}."
        if missing
        else "All configured required tag keys are present."
    )
    return Finding(
        "required-tags",
        resource_type,
        resource_id,
        region,
        status,
        summary,
        {"required_tag_keys": list(required_tags), "missing_tag_keys": missing},
    )


def _paginate(client: Any, operation: str, **kwargs: Any) -> list[dict[str, Any]]:
    """Return paginator items; boto3 paginators keep collection checks complete."""
    items: list[dict[str, Any]] = []
    for page in client.get_paginator(operation).paginate(**kwargs):
        if operation == "describe_instances":
            for reservation in page.get("Reservations", []):
                items.extend(reservation.get("Instances", []))
        elif operation == "list_buckets":
            items.extend(page.get("Buckets", []))
        elif operation == "describe_security_groups":
            items.extend(page.get("SecurityGroups", []))
    return items


def _audit_ec2(
    ec2: Any,
    region: str,
    required_tags: tuple[str, ...],
) -> list[Finding]:
    findings: list[Finding] = []
    try:
        instances = _paginate(
            ec2,
            "describe_instances",
            Filters=[{"Name": "instance-state-name", "Values": ACTIVE_INSTANCE_STATES}],
        )
    except (ClientError, BotoCoreError) as error:
        findings.append(_unknown("ec2.instances.list", "collection", "instances", region, error))
    else:
        for instance in instances:
            instance_id = str(instance.get("InstanceId", "unknown-instance"))
            findings.append(
                _tag_finding(
                    "ec2-instance", instance_id, region, instance.get("Tags", []), required_tags
                )
            )

    try:
        groups = _paginate(ec2, "describe_security_groups")
    except (ClientError, BotoCoreError) as error:
        findings.append(
            _unknown("ec2.security-groups.list", "collection", "security-groups", region, error)
        )
    else:
        for group in groups:
            group_id = str(group.get("GroupId", "unknown-security-group"))
            findings.append(
                _tag_finding(
                    "security-group", group_id, region, group.get("Tags", []), required_tags
                )
            )
            exposed_rules = []
            for permission in group.get("IpPermissions", []):
                protocol = str(permission.get("IpProtocol", "unknown"))
                ports = (
                    "all ports"
                    if protocol == "-1"
                    else f"{permission.get('FromPort', '?')}-{permission.get('ToPort', '?')}"
                )
                for address in permission.get("IpRanges", []):
                    if address.get("CidrIp") == "0.0.0.0/0":
                        exposed_rules.append(
                            {"address": "0.0.0.0/0", "protocol": protocol, "ports": ports}
                        )
                for address in permission.get("Ipv6Ranges", []):
                    if address.get("CidrIpv6") == "::/0":
                        exposed_rules.append(
                            {"address": "::/0", "protocol": protocol, "ports": ports}
                        )
            findings.append(
                Finding(
                    "security-group-wide-ingress",
                    "security-group",
                    group_id,
                    region,
                    "FINDING" if exposed_rules else "PASS",
                    (
                        f"Inbound rules allow traffic from a world-open CIDR: {len(exposed_rules)} rule(s)."
                        if exposed_rules
                        else "No inbound rule uses 0.0.0.0/0 or ::/0."
                    ),
                    {"rules": exposed_rules},
                )
            )
    return findings


def _bucket_region(
    s3: Any, bucket: dict[str, Any], requested_region: str
) -> tuple[str | None, Exception | None]:
    listed_region = bucket.get("BucketRegion")
    if isinstance(listed_region, str) and listed_region:
        return listed_region, None
    try:
        response = s3.get_bucket_location(Bucket=bucket["Name"])
    except (ClientError, BotoCoreError) as error:
        return None, error
    location = response.get("LocationConstraint")
    if location == "EU":
        return "eu-west-1", None
    return (location or "us-east-1"), None


def _audit_bucket(
    session: Any,
    inventory_s3: Any,
    bucket: dict[str, Any],
    requested_region: str,
    required_tags: tuple[str, ...],
) -> list[Finding]:
    name = str(bucket.get("Name", "unknown-bucket"))
    region, region_error = _bucket_region(inventory_s3, bucket, requested_region)
    if region is None:
        unknown = _unknown(
            "s3.bucket.region", "s3-bucket", name, requested_region, region_error or RuntimeError()
        )
        return [unknown]

    findings: list[Finding] = []
    findings.append(
        Finding(
            "s3.bucket.region",
            "s3-bucket",
            name,
            region,
            "PASS",
            "Bucket region was identified.",
            {},
        )
    )
    try:
        s3 = session.client("s3", region_name=region)
    except (ClientError, BotoCoreError) as error:
        return findings + [_unknown("s3.bucket.client", "s3-bucket", name, region, error)]

    try:
        tag_response = s3.get_bucket_tagging(Bucket=name)
        tags = tag_response.get("TagSet", [])
    except ClientError as error:
        if _exception_codes(error) == "NoSuchTagSet":
            tags = []
        else:
            findings.append(_unknown("s3.bucket.tags", "s3-bucket", name, region, error))
            tags = None
    except BotoCoreError as error:
        findings.append(_unknown("s3.bucket.tags", "s3-bucket", name, region, error))
        tags = None
    if tags is not None:
        findings.append(_tag_finding("s3-bucket", name, region, tags, required_tags))

    try:
        config = s3.get_public_access_block(Bucket=name).get("PublicAccessBlockConfiguration", {})
    except ClientError as error:
        if _exception_codes(error) in NO_PUBLIC_ACCESS_BLOCK_CODES:
            findings.append(
                Finding(
                    "s3.public-access-block",
                    "s3-bucket",
                    name,
                    region,
                    "NOT_CONFIGURED",
                    "No bucket-level public-access-block configuration was returned.",
                    {},
                )
            )
        else:
            findings.append(_unknown("s3.public-access-block", "s3-bucket", name, region, error))
    except BotoCoreError as error:
        findings.append(_unknown("s3.public-access-block", "s3-bucket", name, region, error))
    else:
        keys = (
            "BlockPublicAcls",
            "IgnorePublicAcls",
            "BlockPublicPolicy",
            "RestrictPublicBuckets",
        )
        disabled = [key for key in keys if config.get(key) is not True]
        findings.append(
            Finding(
                "s3.public-access-block",
                "s3-bucket",
                name,
                region,
                "FINDING" if disabled else "PASS",
                (
                    f"Bucket-level public-access-block setting(s) are not enabled: {', '.join(disabled)}."
                    if disabled
                    else "All four bucket-level public-access-block settings are enabled."
                ),
                {"disabled_settings": disabled},
            )
        )

    try:
        is_public = s3.get_bucket_policy_status(Bucket=name).get("PolicyStatus", {}).get("IsPublic")
    except ClientError as error:
        if _exception_codes(error) in NO_PUBLIC_POLICY_CODES:
            findings.append(
                Finding(
                    "s3.bucket-policy-public-status",
                    "s3-bucket",
                    name,
                    region,
                    "NOT_CONFIGURED",
                    "No bucket policy was returned; ACL and account-level controls are checked separately.",
                    {},
                )
            )
        else:
            findings.append(
                _unknown("s3.bucket-policy-public-status", "s3-bucket", name, region, error)
            )
    except BotoCoreError as error:
        findings.append(
            _unknown("s3.bucket-policy-public-status", "s3-bucket", name, region, error)
        )
    else:
        findings.append(
            Finding(
                "s3.bucket-policy-public-status",
                "s3-bucket",
                name,
                region,
                "FINDING" if is_public is True else "PASS" if is_public is False else "UNKNOWN",
                (
                    "AWS reports the bucket policy as public."
                    if is_public is True
                    else "AWS reports the bucket policy as not public."
                    if is_public is False
                    else "The response did not include a boolean public-status value."
                ),
                {"is_public": is_public},
            )
        )

    try:
        grants = s3.get_bucket_acl(Bucket=name).get("Grants", [])
    except (ClientError, BotoCoreError) as error:
        findings.append(_unknown("s3.bucket-acl-wide-grants", "s3-bucket", name, region, error))
    else:
        broad_grants = []
        for grant in grants:
            grantee = grant.get("Grantee", {})
            label = (
                PUBLIC_GROUP_URIS.get(grantee.get("URI"))
                if grantee.get("Type") == "Group"
                else None
            )
            if label:
                broad_grants.append(
                    {"group": label, "permission": grant.get("Permission", "unknown")}
                )
        findings.append(
            Finding(
                "s3.bucket-acl-wide-grants",
                "s3-bucket",
                name,
                region,
                "FINDING" if broad_grants else "PASS",
                (
                    "Bucket ACL grants access to a broad predefined group."
                    if broad_grants
                    else "No AllUsers or AuthenticatedUsers group grant was returned."
                ),
                {"grants": broad_grants},
            )
        )
    return findings


def build_report(
    session: Any,
    *,
    region: str,
    required_tags: tuple[str, ...],
) -> dict[str, Any]:
    """Audit selected regional EC2 resources and account-owned general S3 buckets."""
    findings: list[Finding] = []
    ec2 = session.client("ec2", region_name=region)
    findings.extend(_audit_ec2(ec2, region, required_tags))

    # ListBuckets is an account-wide inventory API; bucket controls are then
    # evaluated with clients for each bucket's actual Region.
    inventory_s3 = session.client("s3", region_name="us-east-1")
    try:
        buckets = _paginate(inventory_s3, "list_buckets")
    except (ClientError, BotoCoreError) as error:
        findings.append(_unknown("s3.buckets.list", "collection", "buckets", "global", error))
    else:
        for bucket in buckets:
            findings.extend(_audit_bucket(session, inventory_s3, bucket, region, required_tags))

    counts = {status: 0 for status in ("PASS", "FINDING", "UNKNOWN", "NOT_CONFIGURED")}
    for finding in findings:
        counts[finding.status] = counts.get(finding.status, 0) + 1
    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "required_tag_keys": list(required_tags),
        "scope": {
            "ec2": "active instances and security groups in the selected Region",
            "s3": "general purpose buckets owned by the caller across the account",
        },
        "summary": counts,
        "findings": [finding.as_dict() for finding in findings],
        "limitations": [
            "Read-only API observations only; no resource is changed.",
            "This is not a complete IAM, Organizations, network-path, or effective-access evaluator.",
            "Bucket ACL checks inspect the bucket ACL, not every object's ACL.",
            "An API error or missing configuration is not treated as a pass.",
        ],
    }
    report["exit_code"] = report_exit_code(report)
    return report


def report_exit_code(report: dict[str, Any]) -> int:
    """Return 0 for completed clean checks, 1 for findings, 2 for incomplete checks."""
    summary = report.get("summary", {})
    if summary.get("UNKNOWN", 0) or summary.get("NOT_CONFIGURED", 0):
        return 2
    if summary.get("FINDING", 0):
        return 1
    return 0
