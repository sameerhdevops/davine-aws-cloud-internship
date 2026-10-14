# Week 6 — Serverless architecture

## Objective and recovered material

A dated, two-page Week 6 report titled “Serverless & Event-Driven Architecture” discusses Lambda and API Gateway, asynchronous processing, and least-privilege access. No standalone execution screenshot, API definition, Lambda package, IAM policy, or test harness from that internship exercise was retained.

**Portal schedule:** Week 6 is marked Completed in the portal state reported by the user. No saved portal screenshot/export was found; the supplied portal history separately says “No weekly submissions yet.” The report is evidence of documented exploration, not proof of upload or deployed behavior.

## Local S3 event-parser demonstration

[`handler.py`](../../demos/week06_serverless/handler.py) accepts a small S3-notification-shaped event, validates its record structure, URL-decodes object keys, and returns bucket/key pairs. It uses only Python’s standard library and runs locally; it is not deployed Lambda code.

```powershell
python -m unittest discover -s tests -v
```

The broader serverless design separates a synchronous API response from asynchronous work. API Gateway can authenticate/throttle HTTP entry points; Lambda handles bounded event-driven compute; a queue can absorb bursts and support retries; a dead-letter path and idempotency strategy are needed for poison messages and duplicate delivery. IAM execution roles should grant only the actions needed on the required resources.

## Operations, security, and cost

Retries can repeat side effects, so handlers should validate input, log correlation identifiers without exposing applicant data, and make writes idempotent. Set timeouts and memory based on measured work, bound concurrency when downstream capacity is limited, and alarm on errors, throttles, duration, and queue age. Request and duration pricing can be attractive at low utilization, but high volume, provisioned concurrency, data transfer, logs, and downstream services affect cost.

“I would decide whether a request needs an immediate response or can be queued, then set retry, idempotency, timeout, and observability behavior around that boundary.”

## Validation and limits

The local tests verify event parsing and malformed-input handling only. They do not test AWS event delivery, Lambda runtime behavior, IAM, API Gateway, retries, or notification delivery. The Week 6 report’s described concepts remain report-described. See [independent demonstrations](../../demos/README.md) and the [gallery](../../evidence/README.md).

Next: [Week 7 — Infrastructure as Code](../week-07-infrastructure-as-code/README.md).
