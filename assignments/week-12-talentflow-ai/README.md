# Week 12 — TalentFlow AI capstone

## Executive summary

**Final submission retained privately; original application and infrastructure source are not retained in this portfolio.** TalentFlow AI is documented as a recruitment and talent-management platform for candidate tracking, resume intake, pipeline management, interview scheduling, and analytics. A separate 34-page architecture report gives broader design context but is not explicitly identified as a Week 11 submission. The Terraform source below is an independent reconstruction, not original capstone code.

![Documented TalentFlow AI reference architecture](../../diagrams/talentflow-intended-architecture.svg)

This is an original, public-safe diagram of the report's intended multi-tier flow. It is not a deployment diagram.

## Evidence-state ledger

| State | What is supported | What is not established |
| --- | --- | --- |
| **IMPLEMENTED** | The official reference repository contains a static browser front end (`index.html`, `style.css`, `script.js`, and an image). | It does not establish a backend, database connection, API, authentication service, AI integration, IaC, or deployment. Ownership/contribution boundaries are not established. |
| **DOCUMENTED CLOUD CONFIGURATION** | The final report describes VPC/subnet/security-group design, encrypted S3, EC2, RDS, SQS, EventBridge, IAM, CloudWatch, SNS, and Terraform planning. | The portfolio has no original source modules, state, sanitized plan, or independently verifiable original configuration. The baseline in this repository is a later reconstruction. |
| **TESTED (report claim)** | The report records local front-end checks and a test matrix for repository clone, authentication, VPC/subnets, security-group chaining, S3 security, and Terraform plan compilation. | No test harness, CI output, raw terminal log, source checkout, or independently rerunnable result from that report is retained. The report's outcomes are not promoted to independently verified tests. |
| **DEPLOYED** | The report describes selected cloud foundation configuration and cost-controlled planning for higher-cost components. | No persistent or current deployment is established. The report frames some higher-cost components as plan-validated rather than continuously maintained. |

## Documented architecture and data flow

The capstone report describes these intended stages:

1. A browser reaches an internet-facing Application Load Balancer in public subnets.
2. The load balancer sends HTTP traffic to EC2 application instances in private subnets.
3. The application tier reads and writes recruitment records to a private RDS MySQL tier.
4. Resume files are stored in an encrypted, non-public S3 bucket.
5. An EventBridge-to-SQS path is intended to decouple document-processing work.

The report also discusses IAM boundaries, CloudWatch/SNS monitoring, multi-AZ design, and Terraform. These are documented design/implementation claims, not source-verified deployment facts.

## Read-only upstream review and attribution

The [official TalentFlow AI repository](https://github.com/davinetechnologiesprojects07/TalentFlow-AI) was inspected read-only on 2026-10-13. Its root contains a static HTML/CSS/JavaScript front end and image, with no visible licence file, backend, dependency manifest, Terraform/IaC, cloud configuration, test suite, or deployment guide. No source code or image is copied into this portfolio.

The upstream repository should be treated as employer-associated reference material. Written permission and clear authorship/contribution boundaries are required before any reuse or redistribution.

## Evidence

The [central evidence gallery](../../evidence/README.md) contains two sanitized Week 10 captures; it does not contain original Week 12 screenshots. Week 12 evidence is limited to private reports and the source observations documented here. The architecture graphic is an independent diagram, not an observed screenshot.

## Security and cost notes

- The report describes S3 encryption and Block Public Access, tiered security groups, and a bucket-scoped IAM role; those controls are not independently reproduced here as recovered internship source.
- The report records an SNS subscription as pending confirmation, so alert delivery is not claimed.
- No cloud resources were created, modified, or charged while preparing this portfolio.

## Independently reconstructed Terraform baseline

The [`infrastructure/terraform`](infrastructure/terraform/README.md) directory contains new source written for this portfolio. It declares VPC/subnet/route-table resources, security groups modelling future tiers, a private versioned SSE-S3 bucket, an EC2-trust S3 read role and instance profile, a CloudWatch log group, SNS topic, and daily S3 storage alarm.

It deliberately creates **no** EC2 instances, RDS database, Application Load Balancer, target group, listener, NAT Gateway, application code, database schema, event processor, or SNS subscription. The ALB, EC2, and RDS security groups are configuration resources only. The private subnets have no NAT route or VPC endpoints and therefore no outbound path to public package repositories or AWS service endpoints.

On 2026-10-13, local Terraform v1.16.5 `fmt -check` passed and `init -backend=false` succeeded with AWS provider v5.100.0. A fresh local `validate` attempt failed before schema validation because the provider plugin did not respond. This local result is recorded as incomplete, not as a pass. Separately, the [GitHub Actions run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38402304332) succeeded on Ubuntu for commit `cb3653c345e0d7f8284ae910d92b10ece35d885d`; its link check, Terraform formatting, backend-free initialization, and validation jobs passed. These checks did not run a plan, apply, or deployment. A separately recorded earlier plan invocation failed before producing a plan because valid AWS credentials were unavailable. No AWS resources were created. See the [local validation record](../../evidence/validation/terraform/local-validation-2026-10-13.md), [hosted validation record](../../evidence/validation/terraform/github-actions-2026-10-13.md), and [checklist](infrastructure/terraform/validation-checklist.md).

## How to make the capstone reproducible later

1. Obtain written approval to publish a sanitized source copy and record ownership boundaries.
2. Add a dependency manifest, local run instructions, database schema/migrations, and a safe test procedure.
3. Use the non-deploying Terraform checks and retain only safe output; never publish state or credentials.
4. Separate local checks, static validation, applied infrastructure, and current deployment evidence in a dated validation record.
