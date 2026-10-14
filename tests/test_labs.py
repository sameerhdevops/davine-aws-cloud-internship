from __future__ import annotations

import json
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

    def test_example_is_contained_nonoverlapping_and_routed(self) -> None:
        self.assertEqual([], validate_plan(self.plan))

    def test_rejects_direct_internet_gateway_route_on_private_subnet(self) -> None:
        self.plan["subnets"][1]["routes"].append("internet-gateway")
        self.assertTrue(any("private subnet" in error for error in validate_plan(self.plan)))

    def test_rejects_overlapping_subnets(self) -> None:
        self.plan["subnets"][1]["cidr"] = "10.20.1.128/25"
        self.assertTrue(any("overlaps" in error for error in validate_plan(self.plan)))


class HealthThresholdTests(unittest.TestCase):
    def test_thresholds_control_unhealthy_and_recovery_transitions(self) -> None:
        target = TargetHealth(healthy_threshold=2, unhealthy_threshold=2)
        self.assertEqual("initial", target.observe(True))
        self.assertEqual("healthy", target.observe(True))
        self.assertEqual("healthy", target.observe(False))
        self.assertEqual("unhealthy", target.observe(False))
        self.assertEqual("unhealthy", target.observe(True))
        self.assertEqual("healthy", target.observe(True))


class ServerlessEventTests(unittest.TestCase):
    def test_parses_and_decodes_s3_object_key(self) -> None:
        event = {"Records": [{"s3": {"bucket": {"name": "example"}, "object": {"key": "incoming%2Fresume+one.pdf"}}}]}
        self.assertEqual([{"bucket": "example", "key": "incoming/resume one.pdf"}], handle(event))

    def test_rejects_malformed_record(self) -> None:
        with self.assertRaises(ValueError):
            handle({"Records": [{}]})


class AlarmMathTests(unittest.TestCase):
    def test_m_of_n_breach_and_clear_state(self) -> None:
        options = {"threshold": 70, "evaluation_periods": 3, "datapoints_to_alarm": 2}
        self.assertEqual("ALARM", evaluate([71, 69, 75], **options))
        self.assertEqual("OK", evaluate([71, 69, 70], **options))
        self.assertEqual("INSUFFICIENT_DATA", evaluate([71, None, 75], **options))


class IdempotencyTests(unittest.TestCase):
    def test_retries_reuse_first_result(self) -> None:
        store = InMemoryIdempotency()
        first = store.handle("submission-42")
        retry = store.handle("submission-42")
        self.assertIs(first, retry)
        self.assertEqual("req-1", retry.request_id)

    def test_rejects_blank_key(self) -> None:
        with self.assertRaises(ValueError):
            InMemoryIdempotency().handle(" ")


class PolicyReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = json.loads((ROOT / "demos/week10_governance/example-policy.json").read_text(encoding="utf-8"))

    def test_named_bucket_object_policy_passes_static_allowlist(self) -> None:
        self.assertEqual([], validate_policy(self.policy))

    def test_rejects_wildcard_action_and_resource(self) -> None:
        self.policy["Statement"][0]["Action"] = "s3:*"
        self.policy["Statement"][0]["Resource"] = "*"
        self.assertTrue(validate_policy(self.policy))


if __name__ == "__main__":
    unittest.main()
