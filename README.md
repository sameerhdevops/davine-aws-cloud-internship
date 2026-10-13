# Davine Technologies — AWS Cloud Engineering Internship Portfolio

This repository is a personal, evidence-rated record of a 12-week AWS Cloud Engineering / DevOps internship progression. It organizes the retained reports and observations without treating every curriculum topic as proof of completed work.

**Start here:** [Public evidence gallery](evidence/README.md) · [Evidence-rated timeline](docs/internship-timeline.md) · [Portfolio map and provenance](docs/portfolio-map.md)

This is not an official Davine Technologies repository and does not imply company endorsement. Original reports, archives, and unredacted screenshots remain private. Two cropped, public-safe Week 10 screenshot derivatives are included in the gallery; all other screenshots remain withheld.

## Highlights

- **Week 10 governance review:** two sanitized historical console captures show the root-account control summary and Trusted Advisor public-snapshot checks. Their scope and limitations are stated beside each image.
- **Week 12 TalentFlow AI:** retained report claims, upstream prototype scope, and the independently reconstructed Terraform baseline are kept distinct. The application is not deployed by this repository.
- **Reproducible source:** the Terraform baseline and its local/CI validation records are available under [Week 12](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md). No AWS resources are created by the checks.
- **Evidence-rated progression:** Weeks 3 and 4 have no recovered evidence; Weeks 6 and 7 are partial; Week 11 remains undetermined. See the [full timeline](docs/internship-timeline.md).

## 12-week progression

The week titles below are the supplied organizing framework, not a claim that every item is an employer-authored brief. Status refers to the evidence currently retained.

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

## Technical themes

The retained material discusses AWS IAM, EC2, VPC, S3, RDS, Lambda, API Gateway, DynamoDB, SQS, EventBridge, CloudWatch, Route 53, CloudFront, Elastic Load Balancing, Auto Scaling, Terraform, CloudFormation, Linux, Git, and GitHub. A topic appearing in a report or screenshot does not by itself establish that I deployed or currently operate that service.

## Reproduction and validation

This is primarily a documentation portfolio. The independently reconstructed [Week 12 Terraform baseline](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md) defines foundational network, storage, IAM, and monitoring resources, but no application compute, ALB, or database. It has not been applied to AWS.

On Windows with Terraform v1.16.5, the latest local run of `terraform fmt -check` passed and `terraform init -backend=false` succeeded using the locked AWS provider v5.100.0. Local `terraform validate` could not load the provider schema because the provider plugin did not respond; this is an environment/tooling failure, not a successful local validation result. The independent [GitHub Actions run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38402304332) on Ubuntu succeeded for commit `cb3653c345e0d7f8284ae910d92b10ece35d885d`: Markdown links, formatting, backend-free initialization, and Terraform validation all passed. See the [hosted validation record](evidence/validation/terraform/github-actions-2026-10-13.md). Neither local nor hosted checks ran a plan, apply, deployment, or AWS resource operation. A separately recorded earlier plan invocation failed before producing a plan because valid AWS credentials were unavailable; no resources were created.

## Repository guide

- [Central evidence gallery and manifest](evidence/README.md)
- [Evidence and validation policy](docs/evidence-and-validation.md)
- [Full evidence-rated timeline](docs/internship-timeline.md)
- [Portfolio map and provenance](docs/portfolio-map.md)
- [Security, governance, and cost review](cross-cutting/aws-security-governance-cost/README.md)
- [High-availability diagram](diagrams/week-05-high-availability.svg) and [serverless-flow diagram](diagrams/week-09-serverless-api.svg)

## Security, cost, and attribution

- Historical console captures are not proof of current AWS state. The gallery describes exactly what each published crop shows and does not show.
- Do not run `terraform plan`, `terraform apply`, or `terraform destroy` for this portfolio review. The infrastructure is not deployed, and applying it can incur AWS charges for storage, alarms, logging, notifications, and any future resources.
- The TalentFlow AI source remains with its owner. The inspected upstream repository had no visible licence, so its code and image are linked, not copied.
- New portfolio work consists of independently written summaries, navigation, explanatory diagrams, evidence curation, validation automation, and the clearly labelled reconstructed Terraform baseline. It is not presented as original employer source.

## Known gaps

Weeks 3 and 4 have no recovered brief, submission, source, or screenshot. Week 6 has a report but no standalone captures; Week 7 has report/capture evidence but no raw IaC; Week 11 has no explicitly labelled deliverable. The Week 12 final report is retained privately, but the original application and infrastructure source and a reproducible deployment are not available in this portfolio. The [timeline](docs/internship-timeline.md) records these limits in detail.
