# Evidence and provenance

This page explains what the public materials support. The **OWNER TO VERIFY** items below refer to source-dependent descriptions carried forward from the existing portfolio record. This review was limited to tracked repository files; private internship originals were not opened.

## Three kinds of project status

- **Portal schedule:** the reported schedule state is Weeks 1–11 marked Completed, Week 12 marked Current / Final Week, and 92% progress. The reported submission-history panel says “No weekly submissions yet.” No portal screenshot or export is retained in this repository, so these are user-reported facts, not screenshot-verified facts.
- **Retained internship material:** original reports and screenshots are described in the existing portfolio records. Titles such as “Final Submission” do not establish portal upload or acceptance.
- **Added portfolio work:** local examples, tests, diagrams, validation scripts, and documentation are clearly marked as portfolio additions. Their presence does not establish authorship beyond the provenance statement attached to each artifact.

## Classification

| Label | Meaning |
| --- | --- |
| Original internship artifact | A report, screenshot, or record described as originating in the internship source set. The exact source-to-description mapping remains **OWNER TO VERIFY** because those private originals were not inspected in this review. |
| Sanitized evidence derivative | A published crop or redacted copy described by the existing record as derived from a source image. Public copies were visually checked in this review; the private-source match and redaction fidelity remain **OWNER TO VERIFY**. |
| Independent reconstruction | A reasoned diagram or configuration assembled from incomplete descriptions. This label describes provenance, not personal authorship or deployment. |
| Reproducible demonstration | Added local code or data that a reviewer can run. It demonstrates only the behavior described with it. |
| Independently validated | A specified command was run against an identified revision and environment; the validation record states its scope and result. |
| Not established by retained evidence | The available repository material is insufficient to support the claim. |

## Week 11 and Week 12

Existing portfolio records describe the duplicated 34-page PDF named approximately `AWS_Project_Architecture_Report__TalentFlow_AI` as a **Week 12 capstone briefing**. It is planning context, not a separate Week 11 assignment or submission. The original PDF was not available for review in this pass; its page count, duplicate relationship, author metadata, and interpretation are **OWNER TO VERIFY** against the private file.

The capstone report description and historical screenshots likewise remain source-dependent. A plan summary is not an apply; an alarm in `Insufficient data` is not a threshold breach; a pending SNS subscription is not a delivered notification; and a Terraform configuration is not a deployed service.

## Public screenshots

Nine screenshots are embedded in the [evidence gallery](../evidence/README.md) and relevant weekly pages. The public derivatives were visually reviewed for visible account identifiers, resource IDs, IP addresses, endpoints, credentials, personal information, billing data, and content/caption mismatches. No visible credential or personal contact detail was observed. This image-only review does not establish correspondence with private originals, the completeness of the crop, or whether the original file was left unchanged: those source-provenance claims are **OWNER TO VERIFY**.

Do not read a gallery image as current account state. Each caption limits the claim to the visible historical observation. Original PDFs, archives, unredacted screenshots, billing views, and images containing unrelated personal or resource details remain withheld.

## Validation records

The [validation index](../evidence/validation/README.md) separates local tests and static checks from hosted CI. A passing Python test, Markdown check, Terraform format/init/validate command, or GitHub job does not establish an AWS plan, application deployment, continuous availability, or live resource state.
