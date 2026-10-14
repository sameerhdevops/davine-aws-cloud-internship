# Week 5 — High availability and Auto Scaling

## Objective

Study a web-serving pattern in which an Application Load Balancer forwards requests to an EC2 target group and an Auto Scaling group maintains capacity across Availability Zones.

## What I did or implemented

The retained August report and captures describe an ALB, target group, launch template, Auto Scaling group, and browser response. One target-group view showed one healthy and one unhealthy target; the ALB detail view was still Provisioning. The available portal information marks Week 5 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

The [diagram](../../diagrams/week-05-high-availability.svg) is an explanatory redraw, not an AWS export.

## Key concepts

The public listener and instance targets are separate tiers. Health checks provide the load balancer with a routing signal, while Auto Scaling applies its own replacement policy and records activities. Multi-AZ placement reduces dependence on one zone but does not remove application, database, DNS, quota, or rollout failures. A target can be unhealthy because of bootstrap time, a wrong path or port, security-group rules, or the application process.

Before changing capacity, compare the target health reason, instance status checks, application logs, and scaling activity. Increased capacity can raise compute, load-balancer, and transfer costs; set bounds and alarms and plan cleanup.

## Evidence and links

![Historical Auto Scaling activity showing a successful launch after an unhealthy instance; the instance identifier is redacted.](../../evidence/assets/week-05-high-availability/week-05-asg-replacement-event.png)

*Sanitized derivative described in the existing portfolio record as a Week 5 console capture dated 2026-08-20. It records one replacement activity, not sustained availability, replacement health, or current state.* See the [gallery entry](../../evidence/README.md#week-5-high-availability-and-auto-scaling).

## Limitations

The repository does not contain the original launch template, target configuration, application source, or infrastructure code needed to reproduce the historical environment. The screenshot demonstrates one recovery action, not a measured availability objective. The local [Week 4 health-threshold example](../week-04-application-load-balancing/README.md) is only a conceptual state machine.

## Next improvements

A useful follow-up demonstration would model target health and capacity replacement as separate transitions, then test the case where a replacement launches but never becomes healthy.
