# Week 9 — Serverless integration and scaling

## Objective

Trace a web request and an event-driven API workflow across their boundaries, then reason about retries, state, scaling, and observability.

## What I did or implemented

Retained Week 9 activity reports describe a web path using Route 53, ALB, Auto Scaling, and EC2 alongside an API path using API Gateway, Lambda, and DynamoDB; RDS and workflow topics also appear. The available portal information marks Week 9 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

The [workflow diagram](../../diagrams/week-09-serverless-api.svg) is an explanatory redraw, not a deployment export. The added [idempotency.py](../../demos/week09_integration/idempotency.py) shows how repeated same-key requests reuse a result in process memory.

## Key concepts

Validate API requests at the boundary and return a clear synchronous response. Move work that can be retried into an asynchronous path when the user experience allows it. Define a stable partition key and access pattern before choosing DynamoDB; conditional writes or a durable idempotency record can protect retries. Monitor Lambda errors, throttles and duration, API errors and latency, queue age, and downstream saturation. Avoid logging resumes or unnecessary candidate data.

The reports describe a successful Step Functions test and an Available RDS state, but original application, API, state-machine, and RDS source code is not in the repository. Those statements remain report-described, not locally reproducible results.

## Evidence and links

![Sanitized Lambda test-result crop showing Status: Succeeded for a saved console test event; account and function context are outside the crop.](../../evidence/assets/week-09-integration/week-09-lambda-test-result.png)

*Sanitized derivative described in the existing portfolio record as an internship screenshot. The capture date is unknown. It shows a console test result only; it does not establish API Gateway integration, durable storage, or end-to-end behavior.*

![Historical Auto Scaling summary row with group and launch-template names redacted; it displays one instance at desired capacity and 1/1 healthy.](../../evidence/assets/week-09-integration/week-09-asg-capacity-health.png)

*The existing portfolio record identifies this as an internship screenshot derivative; the private source was not independently inspected. Capture date is unknown. It is a point-in-time view, not continuous availability or proof of the Week 5 deployment.*

See the [gallery entry](../../evidence/README.md#week-9-serverless-integration-and-scaling), [demo catalog](../../demos/README.md), and [validation tests](../../tests/test_labs.py).

## Limitations

The idempotency example uses process-local memory. It is not durable, is not safe across concurrent processes, and does not guarantee exactly-once processing. Historical endpoint URLs, resource IDs, table data, and other identifiers are withheld. The screenshots do not prove that services remain available, and the visible DynamoDB example row is not published.

## Next improvements

A follow-up could use a local durable store or conditional-write interface to test retries across process restarts, while keeping the current in-memory example as the smaller baseline.
