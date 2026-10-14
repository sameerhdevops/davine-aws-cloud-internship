# Week 12 — TalentFlow AI capstone

## Project goal and source boundary

**OWNER TO VERIFY:** report, screenshot, date, and source-provenance descriptions below are carried forward from the existing portfolio record; this review did not reopen private originals. Confirm those details against the originals before presenting them as first-person work or a submission.

TalentFlow AI is described in the retained final report as a recruitment and talent-management platform for candidate profiles, resume intake, job/application tracking, interview scheduling, evaluations, and analytics. A separate 34-page briefing—duplicated under Week 11 and Week 12 filenames—describes the target architecture. It is planning context for this capstone, not a Week 11 submission and not proof that the proposed stack was deployed.

The source set includes a 13-page report titled “Final Submission,” but the report’s title does not prove that it was uploaded to the portal or accepted. No portal screenshot/export was found; the user-reported portal state says Week 12 is the Current/Final Week and the submission history says “No weekly submissions yet.” The report itself contains technical claims and screenshots; the public evidence below is deliberately limited to sanitized crops that support narrow historical observations.

## Proposed workflow and security boundaries

The report’s intended user-facing path is browser → DNS/CDN → ALB → application tier → private relational data. Resume documents use S3 object storage. Separate API/Lambda and event-driven services support selected workflows; queues decouple work and SNS is intended for notifications. CloudWatch, IAM, audit/configuration services, and Terraform are cross-cutting operational controls. The [reconstructed diagram](../../diagrams/talentflow-intended-architecture.svg) shows this **documented intended architecture**, not verified service integration.

![Sanitized crop of the capstone report’s historical VPC resource map showing a named VPC, four subnets, route tables, and an Internet Gateway connection; account and route-table identifiers are redacted.](../../evidence/assets/week-12-talentflow-ai/week-12-vpc-resource-map.png)

*Sanitized derivative of an original console image embedded in the capstone report. It shows one historical VPC console map. It does not prove that the portfolio Terraform created it, that the app ran there, or that every route/security control behaved as intended.*

The reconstructed design uses a `/16` VPC across two AZs, two public and two private subnets, a public route through an Internet Gateway, and private route tables with an S3 gateway endpoint but no general Internet egress. The intended public ingress/application/database tiers are separated by security groups; the app ingress refers to the ALB security group and the RDS ingress refers to the EC2 security group. The S3 bucket blocks public access, uses SSE-S3, versioning, a TLS-only bucket policy, and a lifecycle rule. Its EC2-trust role grants `ListBucket`/`GetBucketLocation` on the bucket and `GetObject`/`GetObjectVersion` on objects; the instance profile exists in source but no instance is created or attached.

The captured report page also shows five security groups, an S3 bucket created but empty, and partial IAM/network configuration. These are observations from the report, not a complete resource inventory.

## What the report captures establish—and do not

The final report includes a Terraform plan summary of `4 to add, 0 change, 0 destroy`; that is a **plan**, not an apply. It shows a CloudWatch alarm in `Insufficient data` and an SNS subscription awaiting email confirmation, so neither alarm firing nor email delivery is established. The original screenshots expose account/resource identifiers and are not published unredacted. The public VPC crop is a sanitized historical derivative only.

The report describes a broader application and service stack, but the local portfolio does not contain the original application or IaC source needed to reproduce it. In particular, this repository does not establish a deployed TalentFlow ALB, EC2 app tier, RDS database, API integration, completed IAM review, or production workload.

## Independent Terraform reconstruction

The [`infrastructure/terraform`](infrastructure/terraform/README.md) project is newly reconstructed portfolio code, not recovered internship source. It currently declares a VPC, IGW, two public and two isolated private subnets, route tables, an S3 gateway endpoint for private S3 access, tiered security groups, a private versioned/encrypted S3 bucket, an EC2-trust read-only IAM role/profile, a CloudWatch log group, SNS topic, and a daily S3 storage alarm. It declares **no** EC2 instances, ALB, RDS database, listener, target group, application, Lambda function, queue, API Gateway, or log producer. The SNS topic has no subscription. No configuration is deployed.

From the repository root, run the local demos with:

```powershell
python -m unittest discover -s tests -v
```

For Terraform, see its [safe inspection and validation commands](infrastructure/terraform/README.md). This task runs only format, backend-free initialization, and validation; it does not run `plan`, `apply`, `destroy`, authenticated AWS CLI commands, or cloud deployment.

## Operations, cost, and next improvements

The reconstructed monitoring source declares a CloudWatch log group with seven-day default retention but no log producer. Its daily `BucketSizeBytes` alarm uses a one-day period; missing data is treated as not breaching, and the SNS topic has no subscription/recipient. This is not end-to-end alert validation. The daily metric is not real-time. The S3 gateway endpoint avoids NAT for the bucket path; future private instances still cannot reach public package repositories without a separately designed egress path. Costs would include S3 storage/requests and retained versions, CloudWatch alarm/log ingestion/retention, SNS delivery, and future compute/load balancing/database/data transfer if added. Check current pricing and define teardown before any separately authorized deployment.

Reasonable next steps are to recover/licence-review the application source, define API/data contracts and candidate-data retention, add tests for object access and event retries, decide private egress, configure actionable metric/log/alert behavior, and validate a deployment plan in a separate approved environment. These are recommendations, not completed work.

Explain the distinction between the proposed capstone architecture, the report observations recorded in the portfolio, and the smaller Terraform reconstruction present in the repository. The recorded baseline validation is source/schema validation only; it was not applied and does not provision the application.

See the [central evidence gallery](../../evidence/README.md#week-12-talentflow-ai-capstone), [evidence timeline](../../docs/internship-timeline.md), and [Terraform project](infrastructure/terraform/README.md).
