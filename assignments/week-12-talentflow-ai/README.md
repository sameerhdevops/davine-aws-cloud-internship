# Week 12 — TalentFlow AI capstone

## Executive summary

**Final submission retained; reproducible application and infrastructure source are not retained locally.** TalentFlow AI is documented as a recruitment and talent-management platform for candidate tracking, resume intake, pipeline management, interview scheduling, and analytics. The private 13-page final submission is the canonical capstone deliverable; a separate 34-page architecture report gives broader design context but is not explicitly identified as a Week 11 submission.

![Documented TalentFlow AI reference architecture](../../diagrams/talentflow-intended-architecture.svg)

The diagram is an original, public-safe reconstruction of the report’s **intended** multi-tier flow. It is not a deployment diagram.

## Evidence-state ledger

| State | What is supported | What is not established |
| --- | --- | --- |
| **IMPLEMENTED** | The official reference repository contains a static browser front end (`index.html`, `style.css`, `script.js`, and an image). | It does not establish a backend, database connection, API, authentication service, AI integration, IaC, or deployment. Ownership/contribution boundaries are not established. |
| **DOCUMENTED CLOUD CONFIGURATION** | The final report describes VPC/subnet/security-group design, encrypted S3, EC2, RDS, SQS, EventBridge, IAM, CloudWatch, SNS, and Terraform planning. It includes capture-time evidence for selected controls. | The retained portfolio has no source modules, state, sanitized plan, migration, or independently verifiable configuration. |
| **TESTED (report claim)** | The report records local front-end checks and a test matrix for repository clone, authentication, VPC/subnets, security-group chaining, S3 security, and Terraform plan compilation. | No test harness, CI output, raw terminal log, source checkout, or independently rerunnable result is retained. The report’s “passed” outcomes are not promoted to independently verified tests. |
| **DEPLOYED** | The report describes selected cloud foundation configuration and cost-controlled planning for higher-cost components. | No persistent or current deployment is established. The report explicitly frames ALB and Multi-AZ RDS-style higher-cost components as plan-validated rather than continuously maintained. |

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

## Security and cost notes

- The report describes S3 encryption and Block Public Access, tiered security groups, and a bucket-scoped IAM role; those controls are not independently reproduced here.
- Its SNS subscription was recorded as pending confirmation, so alert delivery is not claimed.
- No cloud resources were created, modified, or charged while preparing this portfolio.

## How to make the capstone reproducible later

1. Obtain written approval to publish a sanitized source copy and record ownership boundaries.
2. Add a dependency manifest, local run instructions, database schema/migrations, and a safe test procedure.
3. Add reviewed Terraform with pinned providers, variables, remote-state protections, and a redacted `plan` output; never publish state or credentials.
4. Separate local checks, static validation, applied infrastructure, and current deployment evidence in a dated validation record.
