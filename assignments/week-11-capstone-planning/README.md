# Week 11 — Capstone briefing and planning

## Objective

I wanted to use the capstone briefing to identify request flows, synchronous and asynchronous work, data boundaries, and operational questions before discussing implementation.

## What I did or implemented

Week 11 focused on the TalentFlow AI capstone briefing and planning. This stage of the internship covered request flows, synchronous and asynchronous work, data boundaries, security, operations, and cost before the technical implementation work. The proposed stack includes Route 53, CloudFront, an ALB, EC2/Auto Scaling, RDS, S3, API Gateway/Lambda, SQS/SNS, EventBridge, CloudWatch, IAM, CloudTrail/Config, and Terraform. The briefing provides the design context for the completed internship project.

## Key concepts

- **Request boundaries:** Decide which actions need an immediate response and which can be queued, retried, or handled asynchronously.
- **Data ownership:** Identify the source of truth for candidate, job, and application data, and define how resume objects are protected and retained.
- **Operations before implementation:** Plan public ingress, alerts, quotas, failure handling, and cost controls alongside the service layout.

## Evidence and links

See the shared [evidence guide](../../docs/evidence-and-validation.md), [timeline](../../docs/internship-timeline.md), [intended architecture diagram](../../diagrams/talentflow-intended-architecture.svg), and smaller [Week 12 Terraform project](../week-12-talentflow-ai/infrastructure/terraform/README.md). The diagram explains a proposed design, not an implementation.

## Limitations

The public repository presents Week 11 as capstone planning context and links it to the Week 12 project page and architecture diagram.

## Next improvements

A useful design exercise could trace one request and event flow with explicit identity, data-retention, failure, monitoring, and cost boundaries.
