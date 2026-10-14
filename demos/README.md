# Added local demonstrations

The repository includes six small, standard-library demonstrations as added portfolio work. They are separate from internship submissions and are not AWS service emulators or evidence of cloud deployment. They make a few design checks reproducible without AWS credentials or charges; the portfolio does not use the label to claim personal authorship.

From the repository root, run the full local suite with Python 3.11 or newer:

```powershell
python -m unittest discover -s tests -v
```

Run the VPC example directly:

```powershell
python demos/week03_vpc/validate.py
```

| Week | Demonstration | What is checked | What is not modeled |
| --- | --- | --- | --- |
| 3 | [`network-plan.json`](week03_vpc/network-plan.json) and [`validate.py`](week03_vpc/validate.py) | CIDR containment, overlap, local routes, and the public/private Internet Gateway route distinction | AWS route propagation, network ACLs, security groups, endpoint policies, or deployed resources |
| 4 | [`health_threshold.py`](week04_alb/health_threshold.py) | Consecutive success/failure thresholds and recovery in a small state machine | ALB probes, connection draining, matcher codes, timing, fail-open behavior, or target registration |
| 6 | [`handler.py`](week06_serverless/handler.py) | S3-shaped event validation and URL-decoded object keys | Lambda runtime, IAM, S3 notifications, retries, API Gateway, or AWS networking |
| 8 | [`alarm_math.py`](week08_observability/alarm_math.py) | A simple numeric M-of-N threshold decision | CloudWatch aggregation, missing-data policies, metric delivery, alarm actions, or notification delivery |
| 9 | [`idempotency.py`](week09_integration/idempotency.py) | Same-key retries reuse an in-process result | DynamoDB, durability, expiry, concurrent requests, exactly-once delivery, or Step Functions |
| 10 | [`policy_check.py`](week10_governance/policy_check.py) | A narrow allow-list check against the accompanying named-bucket example | IAM policy evaluation, trust policies, conditions, SCPs, Access Analyzer, or AWS authorization results |

The Week 10 checker supports only the two listed object actions and a named-bucket object ARN in the AWS partition. It intentionally accepts a smaller bucket-name subset: lowercase letters, digits, and internal hyphens, with S3-reserved prefixes and suffixes rejected. Dotted names and account-regional bucket names are out of scope; this check does not establish global name availability. See the [current S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).

Each weekly page links the relevant code and records its assumptions. These examples test the repository code only.
