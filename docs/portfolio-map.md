# Portfolio map and provenance

## Repository layout

| Path | Purpose | Provenance |
| --- | --- | --- |
| `assignments/week-01-...` through `week-12-...` | Weekly narrative and evidence boundary | Portfolio summaries with retained-source claims marked for owner verification, plus clearly labeled added work |
| `evidence/` | Public gallery, CSV manifest, and validation records | Sanitized derivatives or actual local/hosted check records |
| `demos/` and `tests/` | Small local engineering examples with tests | Added standard-library demonstrations; personal authorship is not asserted by the classification |
| `scripts/aws_audit/` | Read-only EC2/security-group/S3 snapshot CLI | Added boto3 tool; tests use synthetic responses and make no AWS calls |
| `samples/` | Example audit report files | Synthetic data only; no account output |
| `diagrams/` | Week 5, Week 9, and capstone explanatory flows | Independent reconstructions; not AWS exports |
| `assignments/week-12-talentflow-ai/infrastructure/terraform/` | Reconstructed baseline | Terraform reconstruction, not recovered Week 7 or capstone implementation |
| `docs/` and `cross-cutting/` | Timeline, evidence, scope, security, governance, cost | Added portfolio documentation; source-dependent claims remain owner-verification items |

## Public and private materials

The repository publishes nine selected screenshot derivatives from Weeks 2, 5, 7, 8, 9, 10, and 12. All have captions and manifest entries. The public set includes no raw source PDF or archive. Budget/Cost Explorer screenshots, incomplete Well-Architected review capture, person-like DynamoDB sample record, raw endpoint/resource identifiers, and the Week 7 open-SSH launch-form screenshot are described as withheld in the existing portfolio record; verify source-related details against private originals. The relevant interpretation is documented.

`recovery-audit/`, `.local-review/`, and local Terraform state/cache directories are private or generated. `.gitignore` excludes them and credentials; they are not release artifacts. Local audit inventories may contain source paths and must remain outside Git.

## Authorship and source attribution

The existing portfolio record treats the Week 11/12 briefing as planning context for Week 12 and describes the copies as duplicates; verify those source details against the private originals. It also describes a retained report titled “Final Submission” but no portal receipt for upload or acceptance. The original application and Terraform source were not recovered according to that record. The upstream TalentFlow AI project is linked rather than copied.

The public repository contains evidence curation, portfolio summaries, local examples/tests, explanatory diagrams, validation automation, and a Terraform reconstruction. Those additions are not represented as employer-provided source or deployment evidence.

## Claims deliberately not made

- No claim that all 12 weeks have original assignment submissions.
- No claim that a Week 11 submission exists.
- No claim that TalentFlow AI is live, deployed, production-ready, or independently authored.
- No claim that the independent Terraform baseline has been applied.
- No claim that a plan, architecture diagram, or screenshot alone proves complete AWS behavior.
- No claim that schedule progress, portal status, or report titles constitute a portal receipt.
