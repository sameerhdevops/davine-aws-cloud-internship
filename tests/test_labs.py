from __future__ import annotations

import copy
import json
import math
import unittest
from pathlib import Path

from demos.week03_vpc.validate import validate_plan
from demos.week04_alb.health_threshold import TargetHealth
from demos.week06_serverless.handler import handle
from demos.week08_observability.alarm_math import evaluate
from demos.week09_integration.idempotency import InMemoryIdempotency
from demos.week10_governance.policy_check import validate_policy


ROOT = Path(__file__).resolve().parents[1]


class VpcPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = json.loads((ROOT / "demos/week03_vpc/network-plan.json").read_text(encoding="utf-8"))

    def assert_error(self, expected: str, errors: list[str]) -> None:
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_example_is_contained_nonoverlapping_and_routed(self) -> None:
        self.assertEqual([], validate_plan(self.plan))

    def test_rejects_direct_internet_gateway_route_on_private_subnet(self) -> None:
        self.plan["subnets"][1]["routes"].append("internet-gateway")
        self.assert_error("private subnet", validate_plan(self.plan))

    def test_rejects_overlapping_subnets(self) -> None:
        self.plan["subnets"][1]["cidr"] = "10.20.1.128/25"
        self.assert_error("overlaps", validate_plan(self.plan))

    def test_rejects_malformed_top_level_and_subnet_shapes_without_crashing(self) -> None:
        for value in (None, [], "plan"):
            with self.subTest(value=value):
                self.assertEqual(["plan must be an object"], validate_plan(value))
        cases = (
            (None, "subnets must be a list"),
            ("bad", "subnets must be a list"),
            ([None], "subnet 0 must be an object"),
            ([{}], "invalid CIDR"),
        )
        for value, expected in cases:
            broken = copy.deepcopy(self.plan)
            broken["subnets"] = value
            with self.subTest(value=value):
                self.assert_error(expected, validate_plan(broken))

    def test_rejects_invalid_cidr_types_and_address_families(self) -> None:
        broken = copy.deepcopy(self.plan)
        broken["vpc_cidr"] = None
        self.assertIn("invalid vpc_cidr", validate_plan(broken)[0])
        broken = copy.deepcopy(self.plan)
        broken["vpc_cidr"] = "2001:db8::/48"
        self.assertIn("IPv4 only", validate_plan(broken)[0])
        broken = copy.deepcopy(self.plan)
        broken["subnets"][0]["cidr"] = "10.20.1.0/24"
        broken["subnets"][1]["cidr"] = "2001:db8::/64"
        self.assert_error("not contained", validate_plan(broken))

    def test_rejects_duplicate_names_malformed_routes_and_unknown_route_labels(self) -> None:
        broken = copy.deepcopy(self.plan)
        broken["subnets"][1]["name"] = broken["subnets"][0]["name"]
        broken["subnets"][2]["routes"] = ["local", {"route": "internet-gateway"}]
        errors = validate_plan(broken)
        self.assert_error("duplicate subnet name", errors)
        self.assert_error("routes must be a list", errors)

        broken = copy.deepcopy(self.plan)
        broken["subnets"][0]["routes"] = ["local", "nat-gateway"]
        self.assert_error("unsupported illustrative route", validate_plan(broken))

    def test_rejects_duplicate_routes_invalid_exposure_and_bad_optional_az(self) -> None:
        broken = copy.deepcopy(self.plan)
        broken["subnets"][0]["routes"] = ["local", "local", "internet-gateway"]
        broken["subnets"][1]["exposure"] = []
        broken["subnets"][1]["az"] = " "
        errors = validate_plan(broken)
        self.assert_error("must not be duplicated", errors)
        self.assert_error("exposure must", errors)
        self.assert_error("az must", errors)


class HealthThresholdTests(unittest.TestCase):
    def test_thresholds_control_unhealthy_and_recovery_transitions(self) -> None:
        target = TargetHealth(healthy_threshold=2, unhealthy_threshold=2)
        self.assertEqual("initial", target.observe(True))
        self.assertEqual("healthy", target.observe(True))
        self.assertEqual("healthy", target.observe(False))
        self.assertEqual("unhealthy", target.observe(False))
        self.assertEqual("unhealthy", target.observe(True))
        self.assertEqual("healthy", target.observe(True))

    def test_rejects_noninteger_boolean_or_nonpositive_thresholds(self) -> None:
        for kwargs, exception in (
            ({"healthy_threshold": True}, TypeError),
            ({"unhealthy_threshold": 2.5}, TypeError),
            ({"healthy_threshold": 0}, ValueError),
            ({"unhealthy_threshold": -1}, ValueError),
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(exception):
                TargetHealth(**kwargs)

    def test_rejects_invalid_state_counters_and_observation_types(self) -> None:
        with self.assertRaises(ValueError):
            TargetHealth(state="unknown")
        with self.assertRaises(ValueError):
            TargetHealth(consecutive_successes=-1)
        with self.assertRaises(TypeError):
            TargetHealth(consecutive_failures=True)
        for value in (None, 1, "true"):
            with self.subTest(value=value), self.assertRaises(TypeError):
                TargetHealth().observe(value)


class ServerlessEventTests(unittest.TestCase):
    @staticmethod
    def event_for(key: str = "incoming%2Fresume+one.pdf") -> dict[str, object]:
        return {"Records": [{"s3": {"bucket": {"name": "example"}, "object": {"key": key}}}]}

    def test_parses_and_decodes_s3_object_key(self) -> None:
        self.assertEqual(
            [{"bucket": "example", "key": "incoming/resume one.pdf"}],
            handle(self.event_for()),
        )

    def test_plus_decoding_distinguishes_space_from_encoded_plus(self) -> None:
        self.assertEqual([{"bucket": "example", "key": "a b+c"}], handle(self.event_for("a+b%2Bc")))

    def test_accepts_empty_records_list_as_no_work(self) -> None:
        self.assertEqual([], handle({"Records": []}))

    def test_rejects_bad_event_records_and_nested_values_as_value_errors(self) -> None:
        for event in (None, [], "event", {}, {"Records": None}, {"Records": "bad"}, {"Records": [None]}, {"Records": [{}]}):
            with self.subTest(event=event), self.assertRaises(ValueError):
                handle(event)
        for event in (
            {"Records": [{"s3": None}]},
            {"Records": [{"s3": {"bucket": [], "object": {"key": "k"}}}]},
            {"Records": [{"s3": {"bucket": {"name": 1}, "object": {"key": "k"}}}]},
            {"Records": [{"s3": {"bucket": {"name": "b"}, "object": {"key": None}}}]},
            {"Records": [{"s3": {"bucket": {"name": ""}, "object": {"key": "k"}}}]},
            {"Records": [{"s3": {"bucket": {"name": "b"}, "object": {"key": ""}}}]},
        ):
            with self.subTest(event=event), self.assertRaises(ValueError):
                handle(event)


class AlarmMathTests(unittest.TestCase):
    def test_m_of_n_breach_clear_missing_and_window_selection(self) -> None:
        options = {"threshold": 70, "evaluation_periods": 3, "datapoints_to_alarm": 2}
        self.assertEqual("ALARM", evaluate([71, 69, 75], **options))
        self.assertEqual("OK", evaluate([71, 69, 70], **options))
        self.assertEqual("INSUFFICIENT_DATA", evaluate([71, None, 75], **options))
        self.assertEqual("OK", evaluate([100, 69, 70, 70], **options))

    def test_rejects_invalid_evaluation_parameters_and_boolean_numbers(self) -> None:
        with self.assertRaises(ValueError):
            evaluate([], threshold=1, evaluation_periods=0, datapoints_to_alarm=1)
        with self.assertRaises(ValueError):
            evaluate([], threshold=1, evaluation_periods=2, datapoints_to_alarm=3)
        with self.assertRaises(TypeError):
            evaluate([], threshold=1, evaluation_periods=True, datapoints_to_alarm=1)
        with self.assertRaises(TypeError):
            evaluate([], threshold=True, evaluation_periods=1, datapoints_to_alarm=1)
        with self.assertRaises(TypeError):
            evaluate([True], threshold=1, evaluation_periods=1, datapoints_to_alarm=1)

    def test_rejects_wrong_sequence_types_and_nonfinite_values_even_with_missing_data(self) -> None:
        options = {"threshold": 1, "evaluation_periods": 2, "datapoints_to_alarm": 1}
        for values in (None, 5, "12", b"12"):
            with self.subTest(values=values), self.assertRaises(TypeError):
                evaluate(values, **options)
        for values in ([math.nan, None], [math.inf, 0], ["1", 2]):
            with self.subTest(values=values):
                with self.assertRaises((TypeError, ValueError)):
                    evaluate(values, **options)
        with self.assertRaises(ValueError):
            evaluate([], threshold=math.nan, evaluation_periods=1, datapoints_to_alarm=1)

    def test_incomplete_windows_return_insufficient_data(self) -> None:
        self.assertEqual(
            "INSUFFICIENT_DATA",
            evaluate([1], threshold=0, evaluation_periods=2, datapoints_to_alarm=1),
        )


class IdempotencyTests(unittest.TestCase):
    def test_retries_reuse_first_result(self) -> None:
        store = InMemoryIdempotency()
        first = store.handle("submission-42")
        retry = store.handle("submission-42")
        self.assertIs(first, retry)
        self.assertEqual("req-1", retry.request_id)

    def test_rejects_blank_and_nonstring_keys(self) -> None:
        for value in ("", "  \t"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                InMemoryIdempotency().handle(value)
        for value in (None, 42, True):
            with self.subTest(value=value), self.assertRaises(TypeError):
                InMemoryIdempotency().handle(value)

    def test_preserves_exact_nonblank_key_instead_of_normalizing_it(self) -> None:
        store = InMemoryIdempotency()
        self.assertIsNot(store.handle("key"), store.handle(" key "))


class PolicyReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = json.loads((ROOT / "demos/week10_governance/example-policy.json").read_text(encoding="utf-8"))

    def errors_for(self, **statement_changes: object) -> list[str]:
        policy = copy.deepcopy(self.policy)
        policy["Statement"][0].update(statement_changes)
        return validate_policy(policy)

    def assert_error(self, expected: str, errors: list[str]) -> None:
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_named_bucket_object_policy_passes_static_allowlist(self) -> None:
        self.assertEqual([], validate_policy(self.policy))

    def test_accepts_single_statement_form_and_named_bucket_object_wildcard(self) -> None:
        policy = copy.deepcopy(self.policy)
        policy["Statement"] = policy["Statement"][0]
        policy["Statement"]["Resource"] = "arn:aws:s3:::example-talentflow-upload/uploads/*"
        self.assertEqual([], validate_policy(policy))

    def test_rejects_every_all_bucket_and_bucket_segment_wildcard_form(self) -> None:
        for resource in ("*", "arn:aws:s3:::*", "arn:aws:s3:::*/*", "arn:aws:s3:::bucket*/*", "arn:aws:s3:::bu*cket/key"):
            with self.subTest(resource=resource):
                self.assert_error("object ARNs", self.errors_for(Resource=resource))

    def test_rejects_bucket_only_malformed_and_unsupported_partition_arns(self) -> None:
        for resource in (
            "arn:aws:s3:::example-talentflow-upload",
            "arn:aws:s3:::example-talentflow-upload/",
            "arn:aws-cn:s3:::example-talentflow-upload/key",
            "arn:aws:s3:us-east-1:123456789012:bucket/example/key",
            "arn:aws:s3:::a/key",
            "arn:aws:s3:::example.bucket/key",
            "arn:aws:s3:::ExampleBucket/key",
            "arn:aws:s3:::bucket-/key",
            "arn:aws:s3:::xn--example/key",
            "arn:aws:s3:::amzn-s3-demo-bucket/key",
            "arn:aws:s3:::example--x-s3/key",
            "arn:aws:s3:::example-an/key",
        ):
            with self.subTest(resource=resource):
                self.assert_error("object ARNs", self.errors_for(Resource=resource))

    def test_rejects_bucket_actions_and_mixed_action_or_resource_lists(self) -> None:
        for changes in (
            {"Action": "s3:ListBucket"},
            {"Action": ["s3:GetObject", "s3:ListBucket"]},
            {"Resource": ["arn:aws:s3:::example-talentflow-upload/*", "*"]},
        ):
            with self.subTest(changes=changes):
                errors = validate_policy(self.policy | {"Statement": [{**self.policy["Statement"][0], **changes}]})
                self.assert_error("action outside" if "Action" in changes else "object ARNs", errors)

    def test_rejects_wrong_types_empty_and_unhashable_action_or_resource_values(self) -> None:
        for value in (None, 1, True, "", [], {}, ["s3:GetObject", None], ["s3:GetObject", {}], [["s3:GetObject"]]):
            with self.subTest(field="Action", value=value):
                errors = self.errors_for(Action=value)
                self.assert_error("Action must be", errors)
        for value in (None, 1, True, "", [], {}, ["arn:aws:s3:::example-talentflow-upload/*", None], [["arn:aws:s3:::example-talentflow-upload/*"]]):
            with self.subTest(field="Resource", value=value):
                self.assert_error("Resource must be", self.errors_for(Resource=value))

    def test_rejects_missing_and_unsupported_policy_structure(self) -> None:
        self.assertEqual(["policy must be an object"], validate_policy(None))
        for policy in (
            {},
            {"Version": 1, "Statement": []},
            {"Version": "2008-10-17", "Statement": self.policy["Statement"]},
        ):
            with self.subTest(policy=policy):
                self.assert_error("Version must", validate_policy(policy))
        for statement in (None, [], "bad"):
            with self.subTest(statement=statement):
                self.assert_error("Statement", validate_policy({"Version": "2012-10-17", "Statement": statement}))
        self.assert_error("statement 0 must be an object", validate_policy({"Version": "2012-10-17", "Statement": [None]}))

    def test_rejects_missing_fields_effect_sid_and_unsupported_constructs(self) -> None:
        base = self.policy["Statement"][0]
        for field in ("Action", "Resource", "Effect"):
            statement = {key: value for key, value in base.items() if key != field}
            self.assert_error("statement 0", validate_policy({"Version": "2012-10-17", "Statement": [statement]}))
        for changes in (
            {"Effect": "Deny"},
            {"Sid": []},
            {"NotAction": "s3:DeleteObject"},
            {"NotResource": "*"},
            {"Principal": "*"},
            {"Condition": {"Bool": {"aws:SecureTransport": "true"}}},
            {"Unexpected": "ignored?"},
        ):
            with self.subTest(changes=changes):
                errors = self.errors_for(**changes)
                if "Effect" in changes:
                    self.assert_error("Effect Allow", errors)
                elif "Sid" in changes:
                    self.assert_error("Sid must", errors)
                else:
                    self.assert_error("unsupported fields", errors)

    def test_validates_all_statements_instead_of_stopping_after_first(self) -> None:
        valid = copy.deepcopy(self.policy["Statement"][0])
        self.assertEqual(
            [],
            validate_policy({"Version": "2012-10-17", "Statement": [valid, copy.deepcopy(valid)]}),
        )
        invalid = {"Effect": "Allow", "Action": ["s3:GetObject", 4], "Resource": "arn:aws:s3:::*"}
        errors = validate_policy({"Version": "2012-10-17", "Statement": [valid, invalid]})
        self.assert_error("statement 1", errors)
        self.assert_error("policy contains unsupported fields", validate_policy(self.policy | {"Id": "unsupported"}))


if __name__ == "__main__":
    unittest.main()
