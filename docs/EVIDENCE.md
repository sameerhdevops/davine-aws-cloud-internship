# Reading the evidence

This page explains what the repository records and demonstrations support. Descriptions of private internship files follow existing notes in the repository; those files were not opened for this writing pass.

## Three kinds of project information

- **Internship tracker:** Weeks 1–11 are marked Completed, Week 12 is marked Current / Final Week, and progress is shown as 92%. The submission-history panel reads “No weekly submissions yet.” A portal screenshot or export is not included here.
- **Internship material:** Existing notes describe reports, briefings, and console images from the internship. A report title such as “Final Submission” does not establish portal upload or acceptance.
- **Portfolio work:** Local examples, tests, diagrams, validation scripts, and documentation are included as technical work in this repository. A file’s presence alone does not establish who authored it.

## Labels used in this portfolio

| Label | Meaning |
| --- | --- |
| Original internship file (as described in repository notes) | A report, screenshot, or record identified by existing notes as originating in the internship source set. The private source mapping has not been checked in this pass. |
| Sanitized screenshot copy | A published crop or redacted image described in the existing notes as coming from an internship screenshot. Its match to the private source and the completeness of its redaction have not been checked here. |
| Portfolio design based on project descriptions | A reasoned diagram or configuration assembled from incomplete descriptions. It does not show deployment or establish personal authorship. |
| Reproducible demonstration | Local code or data a reviewer can run to observe the behavior described on its page. |
| Validated check | A named command run against identified code or configuration; the record states its environment, result, and scope. |
| Not established | The available repository files do not support the claim. |

## Week 11 and Week 12

Existing repository notes classify the PDF named approximately `AWS_Project_Architecture_Report__TalentFlow_AI` as a Week 12 capstone briefing, not as a Week 11 task or submission. The source PDF is not in the repository, so its page count, duplicate relationship, author metadata, and contents cannot be confirmed from the published files. The briefing is planning context, not proof of implementation.

The same distinction applies to other project descriptions: a plan summary is not an apply; an alarm in `Insufficient data` is not a threshold breach; a subscription awaiting confirmation is not a delivered notification; and a Terraform file is not a deployed service.

## Published screenshots

The [evidence gallery](../evidence/README.md) embeds selected console images with captions, and the weekly pages link to relevant views. A screenshot records only what was visible at its capture time; it does not establish current account state or sustained operation. Reviewing the published copy cannot confirm whether it matches a private original or whether the full original was safely handled. Those source checks remain for the owner.

Original PDFs, archives, unredacted screenshots, billing views, and images containing unrelated personal or resource details are not published. See the [file-level manifest](../evidence/manifest.csv) for each public item and its stated scope.

## Validation records

The [validation index](../evidence/validation/README.md) separates local checks from hosted CI. A passing Python test, Markdown check, Terraform format/init/validate command, or GitHub job does not establish an AWS plan, application deployment, continuous availability, or live resource state.
