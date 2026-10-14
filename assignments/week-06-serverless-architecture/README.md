# Week 6 — Serverless architecture

## Objective

Review event-driven compute, API entry points, asynchronous processing, retries, idempotency, and least-privilege execution roles.

## What I did or implemented

A dated two-page Week 6 report titled “Serverless & Event-Driven Architecture” discusses Lambda, API Gateway, asynchronous processing, and least privilege. The available portal information marks Week 6 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

The added [handler.py](../../demos/week06_serverless/handler.py) accepts a small S3-notification-shaped event, validates its record structure, URL-decodes object keys, and returns bucket/key pairs. It runs locally using the standard library.

## Key concepts

Separate a synchronous API response from work that can run asynchronously. API Gateway can provide an HTTP entry point; Lambda handles bounded event-driven compute; a queue can absorb bursts and support retries. A dead-letter path helps isolate poison messages, while idempotency protects side effects from duplicate delivery. Execution roles should grant only the actions and resources required.

Validate input, use correlation identifiers without logging applicant data, set timeouts and measured memory, and bound concurrency when downstream capacity is limited. Monitor errors, throttles, duration, and queue age. Cost depends on request volume, duration, provisioned concurrency, transfer, logging, and downstream services.

## Evidence and links

Run the regression suite from the repository root:

    python -m unittest discover -s tests -v

The local tests cover event parsing and malformed-input handling. See the [demo catalog](../../demos/README.md) and [evidence gallery](../../evidence/README.md).

## Limitations

No standalone execution capture, API definition, Lambda package, IAM policy, or test harness from the internship exercise is retained. The local parser is not deployed Lambda code and does not test AWS event delivery, runtime behavior, IAM, retries, API Gateway, or notification delivery. Report descriptions do not establish portal upload or deployed behavior.

## Next improvements

Add a local fixture for duplicate event delivery and document where a durable idempotency record would be required before processing events with real side effects.
