# AWS security, governance, and cost review

This section links the retained Week 10 review to the two public-safe screenshot derivatives in the [central evidence gallery](../../evidence/README.md). The images are historical observations. They do not establish current AWS state, the identity of the operator, or a complete account-wide assessment.

## Published evidence

| Topic | Public artifact | What it shows | What it does not prove |
| --- | --- | --- | --- |
| IAM root-account controls | [Sanitized IAM dashboard capture](../../evidence/assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png) | At capture time, the dashboard reported root MFA enabled and no active root access keys. | Who configured the controls, current status, or least-privilege across all users and roles. |
| Trusted Advisor snapshot checks | [Sanitized public-snapshot checks](../../evidence/assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png) | At capture time, the displayed checks reported zero public EBS snapshots and zero public RDS snapshots. | Absence of all other findings or current account status. The adjacent S3 check is not expanded. |

The crops remove account identity and surrounding console context. Capture dates are unknown. The original screenshots were preserved privately and not modified. Both published copies were flattened and visually reviewed after sanitization.

## Other reviewed subjects

The private Week 10 activity and audit reports and screenshots also cover AWS Budgets, Cost Explorer, a Well-Architected review, and remediation discussion. Those images are not published: budget and cost views expose account-specific financial details; the Well-Architected review is incomplete; and the before/after image contains identifiers and remediation claims that are not independently substantiated. No public screenshot currently demonstrates a CloudWatch alarm or a completed remediation.

## Interpretation and practical lessons

- Treat each console capture as a dated-in-unknown-time observation, not a present-day security attestation.
- Root MFA and the absence of active root access keys are important account safeguards, but they do not assess identity-level permissions or prove that least privilege is implemented.
- Trusted Advisor's visible zero counts apply only to the two expanded public-snapshot checks in that capture.
- Budget and Cost Explorer observations are intentionally not reproduced because they expose private account and spend context.
- Monitoring, IAM, and remediation topics also appear in the [Week 10 record](../../assignments/week-10-governance-audit/README.md); report descriptions remain distinguished from direct screenshot observations.

The complete public inventory and limitations are in the [evidence manifest](../../evidence/manifest.csv). The internship evidence does not establish that the reviewed account remains configured this way today.
