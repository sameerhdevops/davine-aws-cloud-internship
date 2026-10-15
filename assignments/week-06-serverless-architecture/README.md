# Week 6 — Serverless architecture

## Objective

I wanted to review event-driven compute, API entry points, asynchronous processing, retries, idempotency, and least-privilege execution roles.

## What I did or implemented

The portfolio’s dated two-page Week 6 report discusses Lambda, API Gateway, asynchronous processing, and least privilege. The local [handler](../../demos/week06_serverless/handler.py) accepts a small S3-notification-shaped event, checks its record structure, decodes object keys, and returns bucket/key pairs using the Python standard library.

## Key concepts

- **Synchronous and asynchronous work:** An API can return quickly while a queue absorbs bursts and supports retries for work that can finish later.
- **Duplicate delivery:** Event consumers should be safe to retry; idempotency protects side effects when a message is delivered more than once.
- **Execution roles:** Grant a function only the actions and resources it needs, and monitor errors, throttles, duration, and queue age without logging applicant data.

## Evidence and links

Run `python -m unittest discover -s tests -v` from the repository root. Tests cover event parsing and malformed-input handling. See the [demo catalog](../../demos/README.md).

## Limitations

The local parser is not deployed Lambda code and does not test AWS event delivery, runtime behavior, IAM, retries, API Gateway, or notification delivery. No standalone execution capture or source package for the internship exercise is in the repository.

## Next improvements

A local fixture could test duplicate event delivery and explain where durable idempotency state is needed before processing real side effects.
