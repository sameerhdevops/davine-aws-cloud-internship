# Week 5 — High availability and Auto Scaling

## Objective

I wanted to study a web pattern where an Application Load Balancer forwards requests to EC2 targets and an Auto Scaling group maintains capacity across Availability Zones.

## What I did or implemented

The portfolio’s August report notes and console captures describe an ALB, target group, launch template, Auto Scaling group, and browser response. One target-group view showed one healthy and one unhealthy target while the ALB detail view still showed Provisioning. The published activity crop records a replacement launch dated 2026-08-20; it does not establish sustained availability or the replacement’s health. The [diagram](../../diagrams/week-05-high-availability.svg) is an explanatory drawing, not an AWS export.

## Key concepts

- **Health and replacement:** An unhealthy target can result from bootstrap time, a wrong health-check path or port, security-group rules, or an application failure; compare the target reason with host checks and logs.
- **Availability boundaries:** Multi-AZ placement reduces dependence on one zone, but it does not remove application, database, DNS, quota, or rollout failures.
- **Capacity and cost:** Set scaling bounds and alarms, and include compute, load-balancer, and data-transfer costs in the lab cleanup plan.

## Evidence and links

![Auto Scaling activity crop showing a launch after an unhealthy instance; the instance identifier is redacted.](../../evidence/assets/week-05-high-availability/week-05-asg-replacement-event.png)

*The crop shows one replacement activity, not sustained availability or the health of the replacement.* See the [gallery entry](../../evidence/README.md#week-5-high-availability-and-auto-scaling).

## Limitations

The repository does not contain the original launch template, target configuration, application source, or infrastructure code needed to reproduce the described environment. The screenshot does not establish a measured availability objective or current service state.

## Next improvements

A local example could model target health and capacity replacement as separate transitions, including a replacement that never becomes healthy.
