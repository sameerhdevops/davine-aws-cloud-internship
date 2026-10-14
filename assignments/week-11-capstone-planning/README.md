# Week 11 — Capstone briefing and planning

## Portal schedule and retained evidence

The user-reported portal state marks Week 11 **Completed**. The same supplied portal history says “No weekly submissions yet,” and no saved portal screenshot/export or Week 11 assignment submission was recovered. Schedule completion and a retained deliverable are separate facts.

The local source collection contains a 34-page **TalentFlow AI capstone architecture briefing** in two files labeled “week 11” and “week 12.” The files have identical SHA-256 content and describe the project that follows in Week 12. PDF metadata identifies another author. The briefing is therefore treated as **capstone planning context**; it is not a Week 11 task and is not a Week 11 submission. It does not establish that the user authored or implemented the design. The original briefing is not redistributed.

## Planning concepts supported by the briefing

The document outlines a proposed recruitment workflow and a target AWS stack spanning Route 53, CloudFront, an Application Load Balancer, EC2/Auto Scaling, RDS, S3, API Gateway/Lambda, SQS/SNS, EventBridge, CloudWatch, IAM, CloudTrail/Config, and Terraform. These names identify proposed components, not a verified build. The planning stage is useful for asking which components are synchronous, which are asynchronous, where candidate data is stored, and where identity, network, monitoring, and cost controls apply.

The portfolio’s [intended-architecture diagram](../../diagrams/talentflow-intended-architecture.svg) is an **independent reconstruction** from the later final report. It does not prove that all boxes were implemented. The [Week 12 Terraform baseline](../week-12-talentflow-ai/infrastructure/terraform/README.md) is a separate, independently authored subset and was not deployed.

## Interview-ready design questions

- Which user journeys require a synchronous response, and which can be queued?
- What are the source of truth and access patterns for candidate, job, and application data?
- How are resume objects protected, retained, and deleted?
- Which tier owns public ingress, and which security-group references control tier-to-tier flows?
- What signals show user impact, queue backlog, failed uploads, or exhausted downstream capacity?
- How are spend limits and cleanup verified in a short-lived lab?

## Limits and links

No separate Week 11 assignment brief, submission, dated work log, or portal receipt is retained. The project briefing does not establish a Week 11 deliverable or implementation. See the [evidence policy](../../docs/evidence-and-validation.md), [timeline](../../docs/internship-timeline.md), and [Week 12 capstone](../week-12-talentflow-ai/README.md).
