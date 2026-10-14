# Evidence and validation policy

The [evidence gallery](../evidence/README.md) displays selected screenshot derivatives described in the existing portfolio record and links the [CSV manifest](../evidence/manifest.csv). The [12-week timeline](internship-timeline.md) keeps portal schedule status separate from retained artifacts and local demonstrations.

## Terms and owner verification

**Retained internship material** means source reports, briefings, and screenshots described in the existing portfolio record. **Added portfolio work** means the repository’s demonstrations, tests, explanatory diagrams, validation scripts, and documentation; these labels do not assert who authored each item. **Reconstructed Terraform** is a configuration assembled for the portfolio because the original infrastructure source was not recovered. **Validated** applies only to the specific command, code, environment, and result recorded; it does not mean planned or deployed.

**OWNER TO VERIFY:** this final review inspected only files inside the public repository and did not reopen private internship originals. Source-dependent statements carried forward here—including artifact identity, dates, duplicate-PDF classification, report contents, screenshot-to-original correspondence, redactions, and withheld-material descriptions—were not independently rechecked against those originals during this pass. Confirm them against the private materials before presenting them as first-person work or a submission record. The public manifest marks source-derived provenance accordingly.

## Classification standard

| Classification | Meaning in this portfolio |
| --- | --- |
| Original internship artifact | A report, screenshot, or record described in the existing source audit. Its source details require owner verification in this review. |
| Sanitized evidence derivative | A separate publication crop/redaction described as derived from an original; verify correspondence and redactions against the private original. |
| Independent reconstruction | A reasoned diagram or configuration assembled for the portfolio from incomplete source material. It does not establish deployment or imply personal authorship. |
| Reproducible demonstration | Added local code or a test that demonstrates one bounded behavior; the label does not assert who authored it. |
| Independently validated | A specific check actually run, with command, environment, result, and limitations recorded. |
| Not established by retained evidence | No retained source or reproducible check supports the claim. |

## Portal schedule versus submission evidence

The user supplied portal state reports Weeks 1–11 as Completed, Week 12 as Current/Final, and schedule progress as 92%. The same supplied portal history says “No weekly submissions yet.” No portal screenshot/export is recorded in the existing portfolio; this review did not inspect the private source collection. Portal facts are attributed to the user rather than independently screenshot-verified. Schedule progress is not proof of weekly assignment submission, acceptance, or technical deployment.

## Public release boundary

- Public screenshots are publication derivatives described by prior portfolio records. Their visible crops and redactions were inspected in this pass; source correspondence and prior claims that originals were unchanged are **OWNER TO VERIFY**.
- Original PDFs, ZIPs, and unredacted console images are not included. Prior records give privacy, attribution, and interpretation reasons for withholding; verify those source-specific reasons against private materials.
- Prior records classify the Week 11/12 architecture PDFs as byte-identical copies of a Week 12 briefing, not a Week 11 assignment; **OWNER TO VERIFY** against the private originals.
- Prior records describe a capstone report titled “Final Submission,” a plan rather than an apply, an `Insufficient data` alarm, and an SNS subscription pending confirmation. The title does not itself prove upload/acceptance, and those details require owner verification against the report.
- TalentFlow AI upstream code is linked rather than copied. No source code or third-party assets are included in the portfolio.

## Validation boundaries

The dependency-free demonstrations are tested with:

```powershell
python -m unittest discover -s tests -v
```

Their local tests validate only the included Python functions and assertions; they do not call AWS APIs or emulate complete AWS services. The run record is [local-demo-tests-2026-10-14.md](../evidence/validation/local-demo-tests-2026-10-14.md).

Terraform checks are `terraform fmt -check`, `terraform init -backend=false`, and `terraform validate`. See the [validation index](../evidence/validation/README.md) for the actual Windows and Ubuntu records, their tested commits, and limitations. Neither static validation result proves a plan or deployment. No plan, apply, destroy, authenticated AWS CLI call, or cloud resource operation is part of this portfolio review.

The Markdown check verifies repository-relative links and heading fragments, while ignoring link-like text in fenced and inline code. The portfolio check verifies all 12 weekly pages, manifest field completeness, unique IDs, classifications, and public paths. Neither script proves technical correctness by itself; code/configuration was reviewed separately, and source claims remain subject to owner verification.
