# AWS Cloud Engineering Internship Portfolio

A recruiter-facing record of a 12-week AWS Cloud Engineering internship with Davine Technologies and the TalentFlow AI capstone. This repository separates **portal schedule status**, **retained internship evidence**, and **independent technical demonstrations** so that a topic, report, screenshot, or Terraform file is not mistaken for something it does not prove.

**Start here:** [12-week map](#12-week-map) · [Evidence gallery](evidence/README.md) · [Evidence timeline](docs/internship-timeline.md) · [Reproducible demos](demos/README.md) · [Week 12 Terraform](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md)

This is a personal portfolio, not an official Davine Technologies repository or company endorsement.

## At a glance

- **Internship schedule, as reported by the user:** Weeks 1–11 marked Completed; Week 12 marked Current / Final Week; schedule progress shown as 92%.
- **Portal submission history, as reported by the user:** “No weekly submissions yet.” No saved portal screenshot or export was found, so portal state is not independently screenshot-verified.
- **Retained technical evidence:** original reports, briefings, and console captures exist for multiple weeks. Only selected, redacted screenshot derivatives are public; they show historical observations with narrow captions.
- **Independent work in this repository:** six small, standard-library demonstrations with tests; explanatory diagrams; and a reconstructed Week 12 Terraform baseline. These are not original internship submissions.
- **Deployment status:** the reconstructed Terraform has not been applied. Nothing in this repository establishes a deployed TalentFlow AI application.

## Strongest inspectable work

1. [Historical evidence gallery](evidence/README.md): genuine, sanitized console captures from Weeks 2, 5, 7, 8, 9, 10, and 12, each captioned with what it shows and does not establish.
2. [Local engineering demonstrations](demos/README.md): CIDR/route checks, a health-threshold state machine, event parsing, alarm math, retry/idempotency behavior, and a narrow static policy example. Run them with `python -m unittest discover -s tests -v`.
3. [TalentFlow AI capstone record](assignments/week-12-talentflow-ai/README.md): the proposed architecture, actual report observations, the independent Terraform subset, validation status, and explicit implementation gaps.
4. [Terraform source and validation record](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md): a non-deployed VPC/S3/IAM/monitoring baseline with backend-free static checks; no credentials or AWS deployment are required for the documented validation workflow.

## 12-week map

The schedule column reflects only the user-supplied portal state. It is not evidence of a submission. “Retained work” describes source artifacts found in the supplied materials; independent portfolio work is listed separately.

| Week | Focus | Portal schedule (reported) | Retained internship evidence | Portfolio page and independent work |
| --- | --- | --- | --- | --- |
| 1 | AWS cloud fundamentals | Completed | Named report, brief, and service-console captures; no public-safe standalone image selected | [Week 1](assignments/week-01-aws-fundamentals/README.md) |
| 2 | EC2 and host-level security | Completed | Brief, dated report, and EC2/Linux/network/alarm captures; one redacted status capture is public | [Week 2](assignments/week-02-ec2-web-server/README.md) |
| 3 | VPC networking | Completed | No week-specific original brief, submission, screenshot, or source recovered | [Week 3](assignments/week-03-vpc-networking/README.md) · VPC route/CIDR demo |
| 4 | Application Load Balancing | Completed | No Week 4 deliverable recovered; Week 5 evidence is not backdated | [Week 4](assignments/week-04-application-load-balancing/README.md) · health-threshold demo |
| 5 | High availability and Auto Scaling | Completed | Report, diagram, console captures, and browser response; one replacement-event crop is public | [Week 5](assignments/week-05-high-availability/README.md) |
| 6 | Serverless architecture | Completed | Dated two-page report; no standalone execution capture or source | [Week 6](assignments/week-06-serverless-architecture/README.md) · event-parser demo |
| 7 | Infrastructure as Code | Completed | Report and historical apply/EC2 screenshot; raw templates not recovered | [Week 7](assignments/week-07-infrastructure-as-code/README.md) |
| 8 | Observability, DNS, and CDN | Completed | Brief, report versions, and CloudWatch captures; one alarm crop is public | [Week 8](assignments/week-08-monitoring-cdn-dns/README.md) · alarm-math demo |
| 9 | Serverless integration and scaling | Completed | Activity reports and Lambda/Auto Scaling captures; two narrow crops are public | [Week 9](assignments/week-09-serverless-api/README.md) · idempotency demo |
| 10 | Governance, security, and cost | Completed | Audit/activity reports and IAM/Trusted Advisor/billing/review captures; two sanitized images are public | [Week 10](assignments/week-10-governance-audit/README.md) · static policy example |
| 11 | Capstone briefing and planning | Completed | No Week 11 assignment/submission; a duplicated 34-page Week 12 capstone briefing is planning context only | [Week 11](assignments/week-11-capstone-planning/README.md) |
| 12 | TalentFlow AI capstone | Current / Final Week | Final report and partial console evidence retained; no portal receipt or full original application/IaC source | [Week 12](assignments/week-12-talentflow-ai/README.md) · independent Terraform baseline |

## Reproduce the independent work

From a local clone with Python 3.11 or newer:

```powershell
python -m unittest discover -s tests -v
python demos/week03_vpc/validate.py
```

The tests are local and dependency-free. They call no AWS APIs and are not AWS service simulators. Scope and limitations for every lab are in the [demo catalog](demos/README.md).

From `assignments/week-12-talentflow-ai/infrastructure/terraform/`, the safe source checks are:

```powershell
terraform fmt -check
terraform init -backend=false -input=false
terraform validate
```

On Windows with Terraform v1.16.5 and the locked AWS provider v5.100.0, the current [local validation record](evidence/validation/terraform/local-validation-2026-10-14.md) shows `terraform fmt -check` and backend-free initialization passing; `terraform validate` failed before schema output because the provider plugin did not respond. The last published-main Ubuntu run passed its recorded link/format/init/validate jobs for commit `1d75790fa9a37e29b1f2afb65603567070e3404b` ([run record](evidence/validation/terraform/github-actions-main-2026-10-13.md)). The release branch’s CI result will be recorded after GitHub evaluates it. **No plan, apply, AWS CLI deployment, or cloud resource operation was run for this portfolio update.**

## Evidence and technical limits

- A completed portal week does not prove that a weekly assignment was submitted. The supplied portal state says no weekly submissions are listed; no portal screenshot/export was found.
- The “Week 11” architecture PDF is a duplicate of the “Week 12” PDF and is a capstone briefing, not a Week 11 task or submission.
- Historical screenshots show only the visible state at their capture time. They do not prove current resources, continuous availability, or ownership of every configuration.
- The capstone report’s `4 to add` Terraform plan was not an apply. Its alarm was `Insufficient data`, and the SNS email subscription was pending confirmation.
- The Week 12 Terraform source is an **independent reconstruction**, not original internship code. It does not provision EC2, an ALB, RDS, application code, Lambda, queues, API Gateway, or a log producer.
- Original PDFs, archives, unredacted screenshots, billing views, personal sample data, and unsafe configuration captures are withheld. The [gallery](evidence/README.md) and [manifest](evidence/manifest.csv) state why.
- TalentFlow AI upstream source is linked, not copied; the inspected repository had no visible licence.

## Repository guide

- [Evidence gallery and publication manifest](evidence/README.md)
- [Evidence-rated timeline](docs/internship-timeline.md)
- [Evidence classification and validation policy](docs/evidence-and-validation.md)
- [Portfolio provenance map](docs/portfolio-map.md)
- [Independent demonstrations and test command](demos/README.md)
- [Security, governance, and cost review](cross-cutting/aws-security-governance-cost/README.md)
- [Terraform architecture source](assignments/week-12-talentflow-ai/infrastructure/terraform/architecture.mmd)
