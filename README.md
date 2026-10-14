# AWS Cloud Engineering Internship Portfolio

A recruiter-facing record of a 12-week AWS Cloud Engineering internship with Davine Technologies and the TalentFlow AI capstone. It separates **portal schedule status**, **retained internship material**, and **added portfolio work** so a topic, report, screenshot, or Terraform file is not mistaken for something it does not prove.

**Start here:** [Strongest work](#strongest-inspectable-work) · [12-week map](#12-week-map) · [Evidence gallery](evidence/README.md) · [Reproducible demos and tests](demos/README.md) · [Week 12 Terraform](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md) · [Validation index](evidence/validation/README.md)

This is a personal portfolio, not an official Davine Technologies repository or company endorsement.

## At a glance

- **Internship schedule, as reported by the user:** Weeks 1–11 marked Completed; Week 12 marked Current / Final Week; schedule progress shown as 92%.
- **Portal submission history, as reported by the user:** “No weekly submissions yet.” No saved portal screenshot or export was found, so portal state is not independently screenshot-verified.
- **Retained technical evidence:** the existing portfolio record describes reports, briefings, and console captures for multiple weeks. Selected screenshot derivatives are public and show historical observations with scoped captions. Source provenance and redactions require owner verification; see the [evidence policy](docs/evidence-and-validation.md).
- **Added portfolio work:** six standard-library demonstrations with tests, explanatory diagrams, and a reconstructed Week 12 Terraform baseline. These are separate from internship submissions and do not make an authorship claim about the retained source material.
- **Deployment status:** the reconstructed Terraform has not been applied. Nothing in this repository establishes a deployed TalentFlow AI application.

## Strongest inspectable work

1. [Historical evidence gallery](evidence/README.md): selected screenshot derivatives described by the prior portfolio record, with captions for the visible observation and its limits. Source correspondence and redactions remain **OWNER TO VERIFY** against private originals.
2. [Local engineering demonstrations](demos/README.md): CIDR/route checks, a health-threshold state machine, event parsing, alarm math, retry/idempotency behavior, and a narrow static policy example. Run them with `python -m unittest discover -s tests -v`.
3. [TalentFlow AI capstone record](assignments/week-12-talentflow-ai/README.md): the proposed architecture, report observations as recorded in the portfolio, the reconstructed Terraform subset, validation status, and implementation gaps.
4. [Terraform source and validation record](assignments/week-12-talentflow-ai/infrastructure/terraform/README.md): a non-deployed VPC/S3/IAM/monitoring baseline with backend-free static checks; no credentials or AWS deployment are required for the documented validation workflow.

## 12-week map

The schedule column reflects only the user-supplied portal state. It is not evidence of a submission. Source-dependent descriptions below are carried forward from the existing portfolio record and require owner verification against the private originals; added portfolio work is listed separately.

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

## Reproduce the added demonstrations

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

The [validation index](evidence/validation/README.md) links the dated local and hosted records and distinguishes a Windows provider-process failure from successful Ubuntu schema validation. Those checks do not establish an AWS plan or deployment. **No plan, apply, AWS CLI deployment, or cloud resource operation was run for this portfolio update.**

## Evidence and technical limits

- A completed portal week does not prove that a weekly assignment was submitted. The supplied portal state says no weekly submissions are listed; no portal screenshot/export was found.
- Existing portfolio records classify the duplicated “Week 11/12” architecture PDF as a Week 12 capstone briefing, not a Week 11 task or submission; verify that source classification against the private original before relying on it.
- Historical screenshots show only the visible state at their capture time. They do not prove current resources, continuous availability, or ownership of every configuration.
- The prior portfolio record describes a capstone report with a `4 to add` Terraform plan, an `Insufficient data` alarm, and an SNS email subscription pending confirmation. **OWNER TO VERIFY** those source-dependent details; a plan is not an apply, and the described state does not establish notification delivery.
- The Week 12 Terraform is a **reconstruction**, not recovered internship code. It does not provision EC2, an ALB, RDS, application code, Lambda, queues, API Gateway, or a log producer.
- Original PDFs, archives, unredacted screenshots, billing views, personal sample data, and unsafe configuration captures are withheld. The [gallery](evidence/README.md) and [manifest](evidence/manifest.csv) state why.
- TalentFlow AI upstream source is linked rather than copied.

## Repository guide

- [Evidence gallery and publication manifest](evidence/README.md)
- [Evidence-rated timeline](docs/internship-timeline.md)
- [Evidence classification and validation policy](docs/evidence-and-validation.md)
- [Portfolio provenance map](docs/portfolio-map.md)
- [Independent demonstrations and test command](demos/README.md)
- [Security, governance, and cost review](cross-cutting/aws-security-governance-cost/README.md)
- [Terraform architecture source](assignments/week-12-talentflow-ai/infrastructure/terraform/architecture.mmd)
