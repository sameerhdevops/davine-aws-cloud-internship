# Portfolio map

## Repository layout

| Path | Purpose | What it contains |
| --- | --- | --- |
| `assignments/week-01-...` through `week-12-...` | Weekly narrative and technical context | Notes about internship material alongside clearly identified portfolio examples |
| `evidence/` | Public gallery, CSV manifest, and validation records | Published screenshot crops and actual local or hosted check records |
| `demos/` and `tests/` | Small local engineering examples | Python demonstrations and tests with synthetic input |
| `scripts/aws_audit/` | Read-only EC2/security-group/S3 snapshot CLI | A boto3 tool; tests use synthetic responses and make no AWS calls |
| `samples/` | Example audit report files | Synthetic data only; no account output |
| `diagrams/` | Week 5, Week 9, and capstone flows | Explanatory diagrams, not AWS exports |
| `assignments/week-12-talentflow-ai/infrastructure/terraform/` | Portfolio Terraform baseline | Selected infrastructure configuration, not recovered Week 7 or capstone source |
| `docs/` and `cross-cutting/` | Timeline, evidence, scope, security, governance, and cost | Portfolio documentation; source-dependent details follow repository notes |

## Public and private materials

The repository publishes nine selected screenshot crops from Weeks 2, 5, 7, 8, 9, 10, and 12. Each has a caption and manifest entry. Raw source PDFs and archives are not included. Existing repository notes say that billing views, an incomplete Well-Architected capture, a person-like DynamoDB sample record, raw endpoint/resource identifiers, and a Week 7 open-SSH launch-form image were withheld; the private source details behind those decisions are not available in the repository.

`recovery-audit/`, `.local-review/`, and local Terraform state/cache directories are private or generated. `.gitignore` excludes them and credentials; they are not release artifacts. Local inventories may contain source paths and must remain outside Git.

## Source and implementation

Existing repository notes treat the Week 11/12 briefing as Week 12 planning context and describe the two named files as matching copies; the private source files were not opened to confirm that account. The notes also describe a report titled “Final Submission” without a portal receipt for upload or acceptance. They say that the original application and Terraform source were not recovered. The upstream TalentFlow AI project is linked rather than copied.

The public repository contains evidence curation, weekly summaries, local examples and tests, explanatory diagrams, validation automation, and a portfolio Terraform baseline. These items are not presented as employer-provided source or proof of deployment.

## Claims not made

- That all 12 weeks have original assignment submissions.
- That a Week 11 submission exists.
- That TalentFlow AI is live, deployed, production-ready, or personally authored.
- That the portfolio Terraform baseline has been applied.
- That a plan, diagram, or screenshot alone proves complete AWS behavior.
- That a completed week or a report titled “Final Submission” proves upload or acceptance.
