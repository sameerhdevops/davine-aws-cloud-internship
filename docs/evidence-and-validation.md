# Evidence and validation guide

The [evidence gallery](../evidence/README.md) displays selected console images and links the [CSV manifest](../evidence/manifest.csv). The [12-week timeline](internship-timeline.md) keeps the program schedule distinct from source files and local demonstrations.

## How to read project claims

**Internship material** refers to reports, briefings, and screenshots described in repository notes. **Added portfolio work** refers to local examples, tests, explanatory diagrams, validation scripts, and documentation; these labels do not establish who authored an item. **Portfolio Terraform baseline** means configuration assembled for the portfolio because the original infrastructure source is not in the repository. **Validated** applies only to the specific command, code, environment, and result recorded; it does not mean planned or deployed.

Descriptions tied to private files follow existing repository notes. The source originals are not in the repository, so their identity, dates, contents, screenshot matches, redactions, and withholding details cannot be checked here. Do not present an item as personally authored or as a submission record based only on a repository description.

<a id="classification-standard"></a>

## Evidence labels

| Label | Meaning in this portfolio |
| --- | --- |
| Original internship file (as described in repository notes) | An item identified by the existing notes as originating in the internship source set. Private source details were not checked in this pass. |
| Sanitized screenshot copy | A separate crop or redacted image described as coming from an original screenshot; its source match and redaction have not been checked against the private original. |
| Portfolio design based on project descriptions | A diagram or configuration assembled from incomplete descriptions; it does not imply deployment or personal authorship. |
| Reproducible demonstration | Local code or a test showing one bounded behavior; it is not a complete AWS service emulator. |
| Validated check | A specific check actually run, with command, environment, result, and scope recorded. |
| Not established | No available source or reproducible check supports the claim. |

## Internship completion

The Davine Technologies AWS Cloud Engineering internship is complete. All 12 weeks and the assigned weekly work are finished. This guide explains how the internship material, local demonstrations, screenshots, and infrastructure configuration relate to one another.

## Public files

- Published screenshots are crops described in the existing repository notes. Their visible contents can be reviewed here, but their source match and the handling of private originals remain unverified.
- Original PDFs, archives, and unredacted console images are not included. Existing notes describe reasons for withholding them, but the supporting private materials are not available in the repository.
- Existing notes classify the Week 11/12 architecture PDFs as matching copies of a Week 12 briefing, not a Week 11 assignment. The source files were not opened to recheck that classification.
- Notes describe a capstone report titled “Final Submission,” a plan rather than an apply, an `Insufficient data` alarm, and a subscription awaiting confirmation. The report title does not prove upload or acceptance; confirm source details before relying on them.
- TalentFlow AI upstream code is linked rather than copied. The repository does not include the original application source.

## What validation means

The local demonstrations are tested with:

```powershell
python -m unittest discover -s tests -v
```

Those tests check the included Python functions and assertions; they do not call AWS APIs or emulate full AWS services. The run record is [local-demo-tests-2026-10-14.md](../evidence/validation/local-demo-tests-2026-10-14.md).

Terraform checks are `terraform fmt -check`, `terraform init -backend=false`, and `terraform validate`. See the [validation index](../evidence/validation/README.md) for Windows and Ubuntu records, tested commits, and scope. Neither static validation result proves a plan or deployment. No plan, apply, destroy, authenticated AWS CLI call, or cloud resource operation was performed.

The Markdown check verifies repository-relative links and heading fragments while ignoring link-like text inside fenced and inline code. The portfolio check verifies weekly pages, headings, manifest fields, unique IDs, labels, public paths, and internal-review markers. Neither script proves technical correctness by itself; code and configuration still need to be read, and claims tied to private files remain limited to what repository records describe.
