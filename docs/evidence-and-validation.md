# Evidence and validation policy

The [evidence gallery](../evidence/README.md) displays selected, sanitized original screenshots and links the [CSV manifest](../evidence/manifest.csv). The [12-week timeline](internship-timeline.md) keeps portal schedule status separate from retained artifacts and local demonstrations.

## Classification standard

| Classification | Meaning in this portfolio |
| --- | --- |
| Original internship artifact | A report, screenshot, or record found in the supplied source collection. It remains private unless an identified derivative is published. |
| Sanitized evidence derivative | A separate crop/redaction of an original artifact, with the technical observation unchanged and redactions documented. |
| Independent reconstruction | A reasoned diagram or configuration written for the portfolio from incomplete source material. It does not establish deployment. |
| Reproducible demonstration | New local code, diagram, or test written to demonstrate one bounded behavior. |
| Independently validated | A specific check actually run, with command, environment, result, and limitations recorded. |
| Not established by retained evidence | No retained source or reproducible check supports the claim. |

## Portal schedule versus submission evidence

The user supplied portal state reports Weeks 1–11 as Completed, Week 12 as Current/Final, and schedule progress as 92%. The same supplied portal history says “No weekly submissions yet.” No saved portal screenshot/export was found in the inspected source materials, so this information is attributed to the user rather than independently screenshot-verified. Schedule progress is not proof of weekly assignment submission, acceptance, or technical deployment.

## Public release boundary

- Public screenshots are selected derivatives, not source originals. Redactions are visible, originals were left unchanged, and each image’s limitation appears adjacent to the image and in the manifest.
- Original PDFs, ZIPs, and unredacted console images are not included. They contain account/resource identifiers, endpoints, personal context, billing details, or unsupported/third-party material.
- The Week 11/12 architecture PDF files are byte-identical copies of a Week 12 briefing; neither is a Week 11 assignment submission.
- The capstone final report is retained privately. Its title does not prove a portal upload or acceptance; a plan is not an apply; an `Insufficient data` alarm and pending SNS confirmation do not prove alert delivery.
- TalentFlow AI upstream code is linked rather than copied because the inspected repository had no visible licence.

## Validation boundaries

The dependency-free demonstrations are tested with:

```powershell
python -m unittest discover -s tests -v
```

Their local tests validate only the included Python functions and assertions; they do not call AWS APIs or emulate complete AWS services. The run record is [local-demo-tests-2026-10-14.md](../evidence/validation/local-demo-tests-2026-10-14.md).

Terraform checks are `terraform fmt -check`, `terraform init -backend=false`, and `terraform validate`. The latest Windows record is [local-validation-2026-10-14.md](../evidence/validation/terraform/local-validation-2026-10-14.md): formatting and initialization passed; the provider process did not return its schema, so validation failed before configuration validation. The last published-main [Ubuntu run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38403674986) passed its recorded link, formatting, backend-free initialization, and validate steps for `1d75790fa9a37e29b1f2afb65603567070e3404b`; the [run record](../evidence/validation/terraform/github-actions-main-2026-10-13.md) explains that it predates this branch. The current branch must pass its own CI. Neither static validation result proves a plan or deployment. No plan, apply, destroy, authenticated AWS CLI call, or cloud resource operation is part of this portfolio review.

The Markdown check verifies repository-relative links and heading fragments. The additional portfolio check validates all 12 weekly pages, public manifest paths, allowed classification values, and common public-path/status requirements. Neither check proves technical correctness by itself; the weekly content and source claims were separately reviewed.
