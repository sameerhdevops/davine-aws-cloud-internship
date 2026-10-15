# AWS Cloud Engineering Portfolio

[![Portfolio quality](https://github.com/sameerhdevops/davine-aws-cloud-internship/actions/workflows/portfolio-quality.yml/badge.svg?branch=main)](https://github.com/sameerhdevops/davine-aws-cloud-internship/actions/workflows/portfolio-quality.yml?query=branch%3Amain)

I built this portfolio to show what I learned during a 12-week AWS Cloud Engineering internship and the additional projects I developed to practise those skills. It brings together weekly learning pages, selected AWS console screenshots, six Python demonstrations with tests, a read-only Boto3 audit tool, and a Terraform baseline for a proposed TalentFlow AI architecture.

This is a personal portfolio, not an official Davine Technologies repository or a company endorsement.

**Internship tracker:** Weeks 1–11 are marked Completed, Week 12 is marked Current / Final Week, and progress is shown as 92%. The submission-history panel reads “No weekly submissions yet.” A portal screenshot is not included in this repository.

## Projects and technical work

- **[Project screenshots](evidence/README.md):** selected AWS console crops with captions explaining what is visible. They show console views from the time they were captured; their match to private originals and the completeness of redactions have not been checked against those originals.
- **[Read-only AWS audit tool](scripts/aws_audit/README.md):** a Boto3 snapshot of regional EC2 and security-group settings and account-owned S3 bucket controls. The repository includes synthetic [JSON](samples/aws-audit-report.json) and [CSV](samples/aws-audit-report.csv) examples.
- **[Six Python demonstrations and tests](demos/README.md):** VPC route and CIDR checks, health-threshold transitions, S3 event parsing, alarm calculations, idempotency, and a limited S3 object-policy checker. These examples use synthetic data and make no AWS API calls.
- **[TalentFlow AI capstone](assignments/week-12-talentflow-ai/README.md):** the proposed architecture and the available project notes. The original application source is not included in this repository.
- **[Week 12 Terraform baseline](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md):** reviewable VPC, security-group, S3, IAM, logging, and monitoring configuration for part of the proposed design. It has not been applied to AWS.

## 12-week learning map

Use the weekly pages to explore each topic and find its related local examples, diagrams, or screenshots.

| Week | Focus | Schedule | Page and related work |
| --- | --- | --- | --- |
| 1 | AWS cloud fundamentals | Completed | [Week 1](assignments/week-01-aws-fundamentals/README.md) |
| 2 | EC2 and host-level security | Completed | [Week 2](assignments/week-02-ec2-web-server/README.md) · [project screenshots](evidence/README.md#week-2-ec2-and-host-level-security) |
| 3 | VPC networking | Completed | [Week 3](assignments/week-03-vpc-networking/README.md) · [CIDR and route demo](demos/week03_vpc/validate.py) |
| 4 | Application Load Balancing | Completed | [Week 4](assignments/week-04-application-load-balancing/README.md) · [health-threshold example](demos/week04_alb/health_threshold.py) |
| 5 | High availability and Auto Scaling | Completed | [Week 5](assignments/week-05-high-availability/README.md) · [architecture diagram](diagrams/week-05-high-availability.svg) |
| 6 | Serverless architecture | Completed | [Week 6](assignments/week-06-serverless-architecture/README.md) · [S3 event parser](demos/week06_serverless/handler.py) |
| 7 | Infrastructure as Code | Completed | [Week 7](assignments/week-07-infrastructure-as-code/README.md) · [console screenshots](evidence/README.md#week-7-infrastructure-as-code) |
| 8 | Observability, DNS, and CDN | Completed | [Week 8](assignments/week-08-monitoring-cdn-dns/README.md) · [alarm calculation demo](demos/week08_observability/alarm_math.py) |
| 9 | Serverless integration and scaling | Completed | [Week 9](assignments/week-09-serverless-api/README.md) · [idempotency example](demos/week09_integration/idempotency.py) |
| 10 | Governance, security, and cost | Completed | [Week 10](assignments/week-10-governance-audit/README.md) · [policy checker](demos/week10_governance/policy_check.py) |
| 11 | Capstone briefing and planning | Completed | [Week 11](assignments/week-11-capstone-planning/README.md) · planning context, not a Week 11 task or submission |
| 12 | TalentFlow AI capstone | Current / Final Week | [Week 12](assignments/week-12-talentflow-ai/README.md) · [Terraform baseline](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md) |

## Run the local checks

Prerequisites: Python 3.11 or newer and Git. Terraform 1.16.5 is needed for the Terraform checks.

From the repository root, create the virtual environment and install the development dependencies:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
```

Run the tests, demo, lint and formatting checks, and documentation checks:

```powershell
.venv\Scripts\python -m unittest discover -s tests -v
.venv\Scripts\python demos/week03_vpc/validate.py
.venv\Scripts\ruff check demos scripts tests
.venv\Scripts\ruff format --check demos scripts tests
.venv\Scripts\python scripts/check_markdown_links.py
.venv\Scripts\python scripts/check_portfolio.py
.venv\Scripts\python -m compileall -q demos scripts tests
```

To see the AWS audit tool's command options without connecting to AWS:

```powershell
.venv\Scripts\python -m scripts.aws_audit.cli --help
```

The optional audit uses read-only AWS APIs. Run it only with an appropriately scoped profile, and keep real reports private because they may contain resource identifiers. See the [audit guide](scripts/aws_audit/README.md).

For Terraform checks, first change to `assignments/week-12-talentflow-ai/infrastructure/terraform/`, then run:

```powershell
terraform fmt -check
terraform init -backend=false -input=false -lockfile=readonly
terraform validate
```

These are static checks; they do not create or deploy the application. No AWS resources were created, changed, or destroyed as part of this validation.

## Scope and deployment status

- The Python demonstrations and their tests run locally with synthetic data. They do not call AWS APIs or act as complete AWS service simulators.
- The Terraform configuration covers only selected parts of the proposed architecture. It does not include the full TalentFlow AI application, its application load balancer, database, Lambda/API implementation, or a log-producing application.
- The original TalentFlow AI application source is not in this repository, and the Terraform baseline has not been applied to AWS.
- The published screenshots are selected crops. Their relationship to private originals and any redactions have not been checked against those originals.
- The Week 11 page describes the capstone briefing as planning context, not a Week 11 task or submission.

For additional detail, see the [evidence guide](docs/EVIDENCE.md), [project scope](docs/SCOPE.md), [security notes](docs/SECURITY-NOTES.md), and [evidence gallery](evidence/README.md).

## Repository guide

| Folder | What's inside |
| --- | --- |
| `assignments/` | The 12 weekly learning pages |
| `demos/` | Small local Python examples |
| `tests/` | Unit tests for the examples and quality checks |
| `scripts/aws_audit/` | Read-only AWS audit tool |
| `evidence/` | Screenshot gallery, manifest, and validation records |
| `docs/` | Portfolio scope, evidence guidance, and security notes |

## Contact

GitHub profile: [@sameerhdevops](https://github.com/sameerhdevops).

