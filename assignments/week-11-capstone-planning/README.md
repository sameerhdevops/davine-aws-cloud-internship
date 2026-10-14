# Week 11 — Capstone briefing and planning

## Objective

Use the capstone briefing as planning context: identify request flows, synchronous and asynchronous work, data boundaries, and operational questions before treating a proposed architecture as an implementation.

## What I did or implemented

The available portal information marks Week 11 Completed and separately reports “No weekly submissions yet”; no portal screenshot or Week 11 assignment submission is retained. Schedule progress and a deliverable are separate facts.

Existing repository records describe a 34-page TalentFlow AI architecture briefing stored under Week 11 and Week 12 filenames, with matching SHA-256 values and PDF metadata naming another author. The private source documents have not been independently inspected. Under the existing classification, the file is Week 12 capstone planning context, not a Week 11 task; it is also not a Week 11 submission. It does not establish authorship or implementation. The briefing is not redistributed.

## Key concepts

The recorded briefing describes a proposed recruitment workflow and target AWS stack spanning Route 53, CloudFront, an Application Load Balancer, EC2/Auto Scaling, RDS, S3, API Gateway/Lambda, SQS/SNS, EventBridge, CloudWatch, IAM, CloudTrail/Config, and Terraform. These are proposed components, not a verified build.

Planning questions include: which actions need a synchronous response; which can be queued; what is the source of truth for candidate, job, and application data; how resume objects are protected and retained; which tier owns public ingress; and how alerts, quotas, and cost limits are defined.

## Evidence and links

The [intended-architecture diagram](../../diagrams/talentflow-intended-architecture.svg) is a reconstruction from descriptions in the existing portfolio record. It is an explanatory design, not proof that each component was implemented. The [Week 12 Terraform baseline](../week-12-talentflow-ai/infrastructure/terraform/README.md) is a separate, smaller reconstruction and has not been deployed.

See the [evidence policy](../../docs/evidence-and-validation.md), [timeline](../../docs/internship-timeline.md), and [Week 12 capstone page](../week-12-talentflow-ai/README.md).

## Limitations

No separate Week 11 brief, submission, dated work log, or portal receipt is retained. The source briefing has not been rechecked against private originals, and it does not establish a Week 11 deliverable or implementation.

## Next improvements

Before describing the briefing as personal work, verify its provenance and dates against the private source materials. For the design itself, document one end-to-end request and event flow with explicit identity, data-retention, failure, monitoring, and cost boundaries.
