# Evidence and validation policy

The [evidence gallery](../evidence/README.md) displays selected screenshot derivatives described in the existing portfolio record and links the [CSV manifest](../evidence/manifest.csv). The [12-week timeline](internship-timeline.md) keeps portal schedule status separate from retained artifacts and local demonstrations.

## Terms and source limits

**Retained internship material** means source reports, briefings, and screenshots described in the existing portfolio record. **Added portfolio work** means the repository’s demonstrations, tests, explanatory diagrams, validation scripts, and documentation; these labels do not assert who authored each item. **Reconstructed Terraform** is a configuration assembled for the portfolio because the original infrastructure source was not recovered. **Validated** applies only to the specific command, code, environment, and result recorded; it does not mean planned or deployed.

The public documentation relies on existing portfolio records for source-dependent descriptions. Private internship originals have not been inspected, so artifact identity, dates, duplicate-PDF classification, report contents, screenshot correspondence, redactions, and withholding reasons have not been independently checked against those files. Provenance should be confirmed before an item is presented as personally authored or as a submission record. The public manifest records these limits.

## Classification standard

| Classification | Meaning in this portfolio |
| --- | --- |
| Original internship artifact | A report, screenshot, or record described in existing portfolio records as originating in the internship source set. Private source details have not been independently checked. |
| Sanitized evidence derivative | A separate publication crop/redaction described in existing records as derived from an original; source correspondence and redactions have not been checked against private originals. |
| Independent reconstruction | A reasoned diagram or configuration assembled for the portfolio from incomplete source material. It does not establish deployment or imply personal authorship. |
| Reproducible demonstration | Added local code or a test that demonstrates one bounded behavior; the label does not assert who authored it. |
| Independently validated | A specific check actually run, with command, environment, result, and limitations recorded. |
| Not established by retained evidence | No retained source or reproducible check supports the claim. |

## Portal schedule versus submission evidence

The supplied portal information lists Weeks 1–11 as Completed, Week 12 as Current/Final, and schedule progress as 92%. It also lists “No weekly submissions yet.” No portal screenshot/export is retained in the repository, so the portal details are not screenshot-verified. Schedule progress is not proof of weekly assignment submission, acceptance, or technical deployment.

## Public release boundary

- Public screenshots are publication derivatives described by existing portfolio records. Their visible content can be inspected in the published files, but source correspondence and claims that originals were unchanged have not been checked against private files.
- Original PDFs, ZIPs, and unredacted console images are not included. Existing records give privacy, attribution, and interpretation reasons for withholding; those source-specific details have not been independently checked against private materials.
- Existing records classify the Week 11/12 architecture PDFs as byte-identical copies of a Week 12 briefing, not a Week 11 assignment. The private originals have not been inspected to recheck that classification.
- Prior records describe a capstone report titled “Final Submission,” a plan rather than an apply, an `Insufficient data` alarm, and an SNS subscription pending confirmation. The title does not itself prove upload/acceptance; confirm these source details against the report before relying on them.
- TalentFlow AI upstream code is linked rather than copied. No source code or third-party assets are included in the portfolio.

## Validation boundaries

The local demonstrations are tested with:

```powershell
python -m unittest discover -s tests -v
```

Their local tests validate only the included Python functions and assertions; they do not call AWS APIs or emulate complete AWS services. The run record is [local-demo-tests-2026-10-14.md](../evidence/validation/local-demo-tests-2026-10-14.md).

Terraform checks are `terraform fmt -check`, `terraform init -backend=false`, and `terraform validate`. See the [validation index](../evidence/validation/README.md) for the Windows and Ubuntu records, tested commits, and limitations. Neither static validation result proves a plan or deployment. No plan, apply, destroy, authenticated AWS CLI call, or cloud resource operation was performed.

The Markdown check verifies repository-relative links and heading fragments, while ignoring link-like text in fenced and inline code. The portfolio check verifies all 12 weekly pages, standard headings, manifest field completeness, unique IDs, classifications, public paths, and prohibited internal-review markers. Neither script proves technical correctness by itself; code/configuration was reviewed separately, and source claims remain limited to the available repository records.
