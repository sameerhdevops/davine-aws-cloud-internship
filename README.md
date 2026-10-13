# Davine Technologies — AWS Cloud Engineering Internship Portfolio

An evidence-led record of a 12-week AWS Cloud Engineering / DevOps internship progression. It is written for entry-level cloud and DevOps review: it separates retained evidence from curriculum framing, report claims, and proposed improvements.

> **Publication boundary:** Original PDFs, screenshots, archives, account details, and unredacted evidence are deliberately excluded. This repository contains public-safe documentation and original explanatory diagrams only.

## TalentFlow AI capstone

**Week 12 — final report retained; original application and infrastructure source, plus a deployment, are not reproducible from this repository.** TalentFlow AI is a recruitment-workflow concept covering candidate tracking, resume ingestion, pipeline management, interview scheduling, and analytics. The capstone report documents a cost-conscious AWS reference design; the separate official project repository contains a static front-end prototype, not the retained original Terraform, backend, or deployment assets.

- [Capstone review, architecture, and evidence states](assignments/week-12-talentflow-ai/README.md)
- [New reconstructed Terraform baseline](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md) — reviewed source, not applied infrastructure
- [Documented intended architecture](diagrams/talentflow-intended-architecture.svg)
- [Official TalentFlow AI reference repository](https://github.com/davinetechnologiesprojects07/TalentFlow-AI) — linked, not copied

## 12-week progression

The weekly subjects below are the supplied organizing framework, not a claim that every item is an employer-authored brief. Status measures the evidence currently retained.

| Week | Focus | Retained-evidence status | Record |
| --- | --- | --- | --- |
| 01 | AWS cloud fundamentals | Verified complete | [Read](assignments/week-01-aws-fundamentals/README.md) |
| 02 | EC2 and host-level security | Verified complete | [Read](assignments/week-02-ec2-web-server/README.md) |
| 03 | VPC networking | No recovered evidence | [Read](assignments/week-03-vpc-networking/README.md) |
| 04 | Application load balancing | No recovered evidence | [Read](assignments/week-04-application-load-balancing/README.md) |
| 05 | High availability and Auto Scaling | Verified complete | [Read](assignments/week-05-high-availability/README.md) |
| 06 | Serverless architecture | Partially present | [Read](assignments/week-06-serverless-architecture/README.md) |
| 07 | Infrastructure as Code | Partially present | [Read](assignments/week-07-infrastructure-as-code/README.md) |
| 08 | Observability, DNS, and CDN | Verified complete | [Read](assignments/week-08-monitoring-cdn-dns/README.md) |
| 09 | Serverless integration and scaling | Verified complete | [Read](assignments/week-09-serverless-api/README.md) |
| 10 | Governance, security, and cost | Verified complete | [Read](assignments/week-10-governance-audit/README.md) |
| 11 | Capstone planning | Undetermined | [Read](assignments/week-11-capstone-planning/README.md) |
| 12 | TalentFlow AI capstone | Final report retained | [Read](assignments/week-12-talentflow-ai/README.md) |

## Technical themes supported by the material

AWS IAM, EC2, VPC, S3, RDS, Lambda, API Gateway, DynamoDB, SQS, EventBridge, CloudWatch, Route 53, CloudFront, Elastic Load Balancing, Auto Scaling, Terraform, CloudFormation, Linux, Git, and GitHub. Presence in this list means the topic appears in retained reports or evidence; it does not automatically indicate a currently deployed service.

## Repository guide

- [Evidence and validation policy](docs/evidence-and-validation.md)
- [Full evidence-rated timeline](docs/internship-timeline.md)
- [Portfolio map and provenance](docs/portfolio-map.md)
- [Security, governance, and cost themes](cross-cutting/aws-security-governance-cost/README.md)
- [High-availability diagram](diagrams/week-05-high-availability.svg) and [serverless-flow diagram](diagrams/week-09-serverless-api.svg)

## Reproducing verified local components

This is primarily a documentation portfolio. A newly reconstructed [Week 12 Terraform baseline](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md) is published as reviewed source, but it has not been Terraform-CLI-validated or applied and it does not deploy the TalentFlow application. No application source, Terraform state, CloudFormation template, dependency manifest, or approved deployment configuration is published here. Diagrams can be viewed directly in GitHub; no cloud resources need to be created to review this repository.

## Security, cost, and attribution

- Do not treat historic console captures or report statements as proof of current AWS state.
- Do not run `terraform apply`, provision AWS resources, or use inferred credentials from this repository; none are supplied.
- The TalentFlow AI source remains with its owner. The upstream project has no visible licence in the inspected root, so its code and image are not redistributed here.
- This portfolio’s new material is limited to independently written summaries, navigation, explanatory diagrams, and a clearly labelled reconstructed Terraform baseline. It does not claim authorship of employer-owned reports or source code.

## Known gaps

Weeks 3 and 4 have no recovered brief, submission, source, or screenshot. Week 6 lacks standalone captures; Week 7 lacks raw IaC files; Week 11 has no explicitly labelled deliverable. See the [timeline](docs/internship-timeline.md) for the exact evidence boundaries.
