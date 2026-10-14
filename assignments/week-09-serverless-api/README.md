# Week 9 — Serverless integration and scaling

## Objective and workflow

The retained Week 9 activity reports describe combining a web path (Route 53, ALB, Auto Scaling and EC2) with a serverless API path (API Gateway, Lambda and DynamoDB), plus related RDS and workflow topics. The independently redrawn [workflow diagram](../../diagrams/week-09-serverless-api.svg) is explanatory, not a deployment export.

![Sanitized Lambda test-result crop showing Status: Succeeded for a saved console test event; account and function context are outside the crop.](../../evidence/assets/week-09-integration/week-09-lambda-test-result.png)

*Original internship screenshot, sanitized derivative. The capture date is unknown. It shows a console test result only; it does not establish API Gateway integration, durable storage, or end-to-end business behavior.*

![Sanitized Auto Scaling row showing one instance at desired capacity and 1/1 healthy across a displayed three-AZ group configuration.](../../evidence/assets/week-09-integration/week-09-asg-capacity-health.png)

*Original internship screenshot, sanitized derivative. Capture date is unknown. It is a point-in-time group view, not continuous availability or proof of the Week 5 deployment.*

**Portal schedule:** Week 9 is marked Completed as reported by the user. No saved portal screenshot/export was found; the portal submission history separately says “No weekly submissions yet.” The activity reports and captures do not establish portal upload or reviewer acceptance.

## Integration and reliability decisions

Keep API request validation at the boundary, return a clear synchronous response, and move work that can be retried into an asynchronous path where the user experience allows it. Define a stable partition key and access pattern before choosing DynamoDB; use conditional writes or a durable idempotency record to handle retries. Monitor Lambda errors/throttles/duration, API 4xx/5xx and latency, queue age, and downstream saturation. Avoid logging resumes or unnecessary candidate data.

[`idempotency.py`](../../demos/week09_integration/idempotency.py) is a small **reproducible demonstration** showing same-key retries reuse an in-memory result. Run the root test suite with `python -m unittest discover -s tests -v`. It is not DynamoDB, is not durable, and is not safe across concurrent processes.

The reports describe a successful Step Functions test and an Available RDS state, but the original application/API/State Machine/RDS source was not recovered. Those statements remain report-described. A visible DynamoDB example row contains person-like sample data and is not published.

For an interview: “I would trace one request by a correlation identifier across API Gateway, Lambda, storage, and any queue; then verify retry/idempotency and observability at each asynchronous boundary.”

## Limitations

Historical endpoint URLs, load-balancer DNS/ARNs, resource IDs, and table data are withheld. Screenshots do not prove the services remain available. See the [gallery](../../evidence/README.md#week-9-serverless-integration-and-scaling) and [demo catalog](../../demos/README.md).

Next: [Week 10 — governance, security, and cost](../week-10-governance-audit/README.md).
