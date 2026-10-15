# Week 11 — Capstone briefing and planning

## Objective

I wanted to use the capstone briefing to identify request flows, synchronous and asynchronous work, data boundaries, and operational questions before discussing implementation.

## What I did or implemented

The portfolio classifies the Week 11/12-named 34-page PDF as a Week 12 TalentFlow AI briefing and planning context. It is not a Week 11 task and not a Week 11 submission. The source PDF is not in the repository, so its contents, author metadata, and duplicate relationship cannot be confirmed from the public files. The briefing does not establish implementation. Its proposed stack includes Route 53, CloudFront, an ALB, EC2/Auto Scaling, RDS, S3, API Gateway/Lambda, SQS/SNS, EventBridge, CloudWatch, IAM, CloudTrail/Config, and Terraform. These are design components, not a verified build.

## Key concepts

- **Request boundaries:** Decide which actions need an immediate response and which can be queued, retried, or handled asynchronously.
- **Data ownership:** Identify the source of truth for candidate, job, and application data, and define how resume objects are protected and retained.
- **Operations before implementation:** Plan public ingress, alerts, quotas, failure handling, and cost controls alongside the service layout.

## Evidence and links

See the shared [evidence guide](../../docs/evidence-and-validation.md), [timeline](../../docs/internship-timeline.md), [intended architecture diagram](../../diagrams/talentflow-intended-architecture.svg), and smaller [Week 12 Terraform project](../week-12-talentflow-ai/infrastructure/terraform/README.md). The diagram explains a proposed design, not an implementation.

## Limitations

No separate Week 11 brief, submission, dated work log, or portal receipt is in the repository. The available schedule information does not establish a Week 11 deliverable.

## Next improvements

A useful design exercise could trace one request and event flow with explicit identity, data-retention, failure, monitoring, and cost boundaries.
