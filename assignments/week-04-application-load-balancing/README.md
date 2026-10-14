# Week 4 — Application Load Balancing

## Objective and evidence boundary

The supplied weekly framework places load balancing, listener-to-target-group routing, health checks, and multi-AZ traffic distribution here. **No Week 4-specific brief, report, screenshot, source configuration, or submission was recovered.** The portal schedule reports Week 4 as Completed; that does not establish a retained Week 4 deliverable. No portal screenshot/export was saved. Week 5’s later ALB/Auto Scaling evidence is not backdated to fill this gap.

## Reproducible health-threshold demonstration

[`health_threshold.py`](../../demos/week04_alb/health_threshold.py) is a small local state machine. It shows how consecutive successful and failed observations can cross illustrative healthy/unhealthy thresholds and how recovery takes additional successful observations. It is a **reproducible demonstration**, not an ALB emulator or internship screenshot.

```powershell
python -m unittest discover -s tests -v
```

An actual ALB health check also depends on listener rules, protocol/port/path, matcher codes, thresholds, interval, timeout, target registration, security-group paths, and connection draining. A failed health check may remove a target from routing; Auto Scaling replacement is a separate control loop that responds to instance health and group policy. These components should be diagnosed independently.

## Security, cost, and interview reasoning

Expose only the listener protocols required, terminate TLS with a managed certificate for production traffic, and allow target ingress from the load balancer security group instead of the Internet. ALBs and data transfer can incur cost even when request volume is low; lab designs should use a budget and a cleanup plan.

“I would check listener/rule matching, target registration and health reason, then compare the ALB-to-target security-group path and application response. A green listener does not prove the target is healthy.”

## Limits and links

The demo tests deterministic state transitions only; it does not simulate probe timing, HTTP response semantics, DNS, fail-open behavior, or AWS control-plane state. See [Week 5](../week-05-high-availability/README.md) for later, separately dated evidence and the [demo catalog](../../demos/README.md).

Next: [Week 5 — high availability and Auto Scaling](../week-05-high-availability/README.md).
