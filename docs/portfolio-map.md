# Portfolio map and provenance

## What is public here

| Material | Classification | Rationale |
| --- | --- | --- |
| Markdown summaries in `assignments/`, `docs/`, and `cross-cutting/` | ALLOW_PUBLIC | Independently written, public-safe descriptions that preserve evidence boundaries. |
| SVG diagrams in `diagrams/` | ALLOW_PUBLIC | Original explanatory diagrams; labelled as documented or intended rather than deployment evidence. |
| Original internship PDFs, screenshots, and archives | EXCLUDE | They may expose account/resource identifiers, endpoints, personal data, or employer-owned content. |
| `recovery-audit/` and `.local-review/` | ALLOW_PRIVATE_ONLY | Local forensic and release-review records. Git-ignored. |
| TalentFlow AI upstream code and assets | NEEDS_PERMISSION | The inspected repository has no visible licence. It is linked, not copied. |

## Authorship boundary

The internship reports and source evidence are preserved privately in their original locations. This repository adds curation, safe technical summaries, links, and explanatory diagrams. It does not claim ownership of Davine Technologies materials or upstream TalentFlow AI code.

## Deliberate omissions

- No unredacted screenshots, reports, ZIP files, source archives, Terraform state, environment files, or credentials.
- No reconstructed Terraform or CloudFormation templates: the original source files were not retained, and an independent example would not be a recovered internship artifact.
- No Week 3 or Week 4 completion claim.
- No claim that the capstone is live, currently deployed, or independently authored.
