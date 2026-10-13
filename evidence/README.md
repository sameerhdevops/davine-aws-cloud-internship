# Public evidence gallery

This is the single index for public screenshots and reproducible validation records in the portfolio. The [CSV manifest](manifest.csv) gives each artifact an identifier, provenance, scope, and limitation; every `public_path` is relative to the repository root. Evidence is historical unless explicitly stated otherwise.

## Week 10 — security and governance

### Root-account security summary

![Sanitized AWS IAM dashboard crop showing root MFA enabled and no active root access keys at capture time; account identity and surrounding console context are removed.](assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png)

[Open the cropped image](assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png). This is a sanitized derivative of an original internship screenshot. It shows that the IAM dashboard reported root MFA enabled and no active root access keys when captured. The capture date is unknown. It does not identify who configured the controls, prove their present state, or establish that all IAM permissions were least-privilege.

### Trusted Advisor public-snapshot checks

![Sanitized Trusted Advisor crop showing zero public EBS and RDS snapshots in the displayed review; account identity and console header are removed.](assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png)

[Open the cropped image](assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png). This is a sanitized derivative of an original internship screenshot. The visible checks report zero public EBS snapshots and zero public RDS snapshots at capture time. The capture date is unknown. It does not prove the broader account had no security findings, and the adjacent S3 check is not expanded.

The original screenshots have not been modified. The public copies are cropped derivatives with identifying headers excluded; they were flattened and visually reviewed. See the [Week 10 record](../assignments/week-10-governance-audit/README.md) for the broader evidence boundary.

## Reproducible validation

- [Latest local Terraform output](validation/terraform/local-validation-2026-10-13.md): formatting and backend-free initialization passed on Windows; validation could not load the AWS provider schema because the local plugin did not respond.
- The [GitHub Actions run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38402304332) passed for commit `cb3653c345e0d7f8284ae910d92b10ece35d885d`: the Markdown-link check and Ubuntu Terraform format, backend-free initialization, and validation jobs succeeded. The workflow does not use AWS credentials and does not run a plan or deployment. See the [hosted validation record](validation/terraform/github-actions-2026-10-13.md).

## Withheld evidence

Other original screenshots, PDFs, and ZIP archives remain private. Many console captures include account identifiers, resource IDs, hostnames, IP addresses, account aliases, personal context, or spend details. The budget and Cost Explorer images also reveal account-specific financial information. The Well-Architected capture is an incomplete review, and the remediation comparison image contains sensitive identifiers and claims that are not independently substantiated. No original internship report or archive is redistributed here.

## Evidence labels

- **Internship capture, sanitized derivative:** a public crop made from a privately retained source screenshot. It is still a historical observation, not a current-state attestation.
- **Independent portfolio work:** documentation, diagrams, code, and validation created for this portfolio after the internship evidence review.
- **Report-described:** a claim recorded in a private report, not independently verified by source code or a reproducible test.

The portfolio uses these labels to avoid conflating a report, a screenshot, validated source, and deployed infrastructure.
