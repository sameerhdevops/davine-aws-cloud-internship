# Week 4 — Application Load Balancing

## Objective

I wanted to understand how an Application Load Balancer sends requests from listeners to target groups and uses health checks when routing traffic.

## What I did or implemented

No Week 4-specific brief, report, screenshot, or source configuration is published, and Week 5 material is kept with its own date. The local [health-threshold example](../../demos/week04_alb/health_threshold.py) models state changes after consecutive successful or failed observations. Its tests cover deterministic transitions; it is not an ALB emulator.

## Key concepts

- **Health-check configuration:** Protocol, port, path, matcher, thresholds, timeout, target registration, and security-group paths all affect target health.
- **Separate control loops:** An ALB can stop routing to an unhealthy target, while Auto Scaling decides whether to replace capacity; diagnose their signals separately.
- **Secure listeners:** Expose only required listener protocols, use managed TLS for production traffic, and permit target ingress from the load-balancer tier rather than the Internet.

## Evidence and links

Run `python -m unittest discover -s tests -v` from the repository root. See the [demo catalog](../../demos/README.md) and separately dated [Week 5 page](../week-05-high-availability/README.md).

## Limitations

The example does not model probe timing, HTTP response semantics, DNS, fail-open behavior, or AWS control-plane state. No Week 4 internship deliverable is established in the repository.

## Next improvements

A follow-up could model health observations separately from target registration and Auto Scaling replacement, keeping AWS-specific timing outside the local state machine.
