# Week 12 — TalentFlow AI capstone

## Objective

Describe the TalentFlow AI recruitment and talent-management goal, distinguish the proposed system from the historical observations recorded in the portfolio, and explain the smaller Terraform reconstruction without implying deployment.

## What I did or implemented

The existing portfolio record describes a 13-page report titled “Final Submission” and a 34-page architecture briefing duplicated under Week 11 and Week 12 filenames. The private source documents have not been independently inspected. The report title does not prove portal upload or acceptance. The available portal information marks Week 12 Current / Final Week and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

The report is described as covering candidate profiles, resume intake, job/application tracking, interview scheduling, evaluations, and analytics. Its proposed browser path is DNS/CDN to an Application Load Balancer, application tier, and private relational data; S3 stores resume objects. Separate API/Lambda and event-driven services support selected workflows, with queues for asynchronous work and SNS for intended notifications. The intended architecture diagram is a reconstruction from the existing portfolio descriptions, not a service-integration export.

## Key concepts

The documented target uses a /16 VPC across two Availability Zones, two public and two private subnets, an Internet Gateway route for public subnets, and private route tables with an S3 gateway endpoint but no general Internet egress. The intended application and database tiers are separated with security groups: application ingress refers to the ALB security group, and database ingress refers to the EC2 security group.

The reconstructed S3 bucket blocks public access, enables SSE-S3 and versioning, applies a TLS-only bucket policy, and defines a lifecycle rule. Its EC2-trust role grants ListBucket and GetBucketLocation on the bucket and GetObject and GetObjectVersion on objects. The instance profile is declared, but no instance is created or attached.

## Evidence and links

![Sanitized crop of a historical VPC resource map showing a named VPC, four subnets, route tables, and an Internet Gateway connection; account and route-table identifiers are redacted.](../../evidence/assets/week-12-talentflow-ai/week-12-vpc-resource-map.png)

*Sanitized derivative described in the existing portfolio record as a console image embedded in the capstone report. It shows one historical VPC map and does not prove that the portfolio Terraform created it, that the application ran there, or that every route and security control behaved as intended.*

The report is also described as showing a Terraform plan summary of 4 to add, 0 change, and 0 destroy; an alarm in Insufficient data; and an SNS subscription awaiting email confirmation. A plan is not an apply, an alarm state is not a breach, and a pending subscription does not establish delivery. See the [evidence gallery](../../evidence/README.md#week-12-talentflow-ai-capstone) and [file-level manifest](../../evidence/manifest.csv).

The [Terraform reconstruction](infrastructure/terraform/README.md) declares a VPC, Internet Gateway, four subnets, route tables, S3 gateway endpoint, tiered security groups, a private versioned/encrypted S3 bucket, an EC2-trust IAM role and instance profile, a CloudWatch log group, SNS topic, and daily S3 storage alarm. It declares no EC2 instances, ALB, RDS database, listener, target group, application, Lambda function, queue, API Gateway, or log producer. The SNS topic has no subscription.

## Limitations

The original TalentFlow AI application and original infrastructure source are not in the repository. The portfolio contains report descriptions and selected historical image derivatives, plus a limited Terraform reconstruction. It does not establish a deployed application, complete IAM review, end-to-end API integration, notification delivery, or current AWS state. The Terraform has not been applied.

The CloudWatch BucketSizeBytes metric is daily rather than real time. The log group has a seven-day default retention but no producer. The S3 gateway endpoint provides a private S3 path; private instances have no general Internet egress for package repositories. Future costs could include S3 storage and requests, retained versions, CloudWatch alarms and log ingestion/retention, SNS delivery, and any added compute, load balancing, databases, and data transfer.

## Next improvements

A future design iteration could define API and data contracts, candidate-data retention and deletion, retry/idempotency tests, a deliberate private egress path, actionable logs and alarms, and a cost/cleanup plan. Those are recommendations, not completed work. Any actual deployment would need separate authorization and a reviewed plan.

The [evidence timeline](../../docs/internship-timeline.md) and [Terraform project](infrastructure/terraform/README.md) provide related provenance and validation detail.
