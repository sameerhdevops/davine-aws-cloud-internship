# Week 4 — Application Load Balancing

## Objective

Understand listener-to-target-group routing, health checks, and how an Application Load Balancer distributes traffic across registered targets.

## What I did or implemented

No Week 4-specific brief, report, screenshot, source configuration, or submission is retained. The available portal information marks Week 4 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is available. Week 5 evidence is kept with its own date and is not used to fill this gap.

The added [health_threshold.py](../../demos/week04_alb/health_threshold.py) is a local state machine for consecutive successful and failed observations. It demonstrates threshold transitions and recovery behavior.

## Key concepts

An ALB health check depends on listener rules, protocol, port and path, matcher codes, thresholds, interval, timeout, target registration, security-group paths, and connection draining. An unhealthy target may be removed from routing. Auto Scaling replacement is a separate control loop driven by instance health and group policy, so the two signals should be diagnosed independently.

Expose only required listener protocols, terminate production TLS with a managed certificate, and permit target ingress from the load balancer security group rather than the Internet. Load balancers and data transfer can incur cost even at low request volume; a lab needs a budget and cleanup plan.

## Evidence and links

Run the local regression suite from the repository root:

    python -m unittest discover -s tests -v

See the [demo catalog](../../demos/README.md) and the separately dated [Week 5 evidence](../week-05-high-availability/README.md).

## Limitations

The health-threshold example is a reproducible demonstration, not an ALB emulator. Its tests cover deterministic state transitions, not probe timing, HTTP response semantics, DNS, fail-open behavior, or AWS control-plane state. No Week 4 internship deliverable is established by retained material.

## Next improvements

If the example is extended, model health-check observations separately from target registration and Auto Scaling replacement. Keep timing and AWS-specific behavior explicitly outside the local state machine unless a reproducible service fixture is added.
