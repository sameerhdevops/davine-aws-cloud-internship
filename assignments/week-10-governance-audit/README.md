# Week 10 — Governance, security, and cost

## Objective

Review account-level security signals, governance findings, policy scope, and billing context without treating a dashboard tile as a complete assessment.

## What I did or implemented

Retained audit/activity reports and screenshots cover root-account signals, Trusted Advisor checks, Well-Architected review state, and billing views. The available portal information marks Week 10 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

## Key concepts

The Well-Architected capture shows 0 of 57 questions answered and 0 issues recorded; it does not support a completed-review claim. Billing captures represent different contexts: a selected Cost Explorer view reported $0 for its filters and date range, while a budget view reported spend above its $1 budget and a higher forecast. Those figures are not combined into a single cost statement. The audit report and dashboard also differ on some root-account details, so they do not establish one current state.

Use budgets and alerts before labs, tag owner and environment, identify idle public addresses and endpoints, and include teardown. For access review, evaluate identity and resource policies, trust relationships, conditions, boundaries, service control policies, and effective permissions rather than relying on one dashboard tile.

## Evidence and links

![Sanitized IAM dashboard crop reporting root MFA enabled and no active root access keys at capture time.](../../evidence/assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png)

*Sanitized derivative described in the existing portfolio record as an original screenshot; capture date is unknown. It shows dashboard-reported root controls only, not who configured them, present state, or least privilege across other identities.*

![Sanitized Trusted Advisor crop reporting zero public EBS and RDS snapshots in the displayed checks.](../../evidence/assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png)

*Sanitized derivative described in the existing portfolio record as an original screenshot; capture date is unknown. It does not establish a complete account-wide review or the unexpanded S3 check.*

The added [example policy](../../demos/week10_governance/example-policy.json) and [policy checker](../../demos/week10_governance/policy_check.py) implement a bounded static check for Version 2012-10-17, explicit Allow, the s3:GetObject/s3:PutObject object-action allow-list, and named-bucket object ARNs. The checker accepts a documented subset of general-purpose bucket names, rejects wildcard bucket scope and unsupported fields, and is not a full AWS naming validator or IAM evaluator. Run the standard unittest suite from the repository root. See the [gallery](../../evidence/README.md#week-10-governance-security-and-cost), [cross-cutting review](../../cross-cutting/aws-security-governance-cost/README.md), and [demo catalog](../../demos/README.md).

## Limitations

The screenshots are historical observations. Billing and raw review captures with account-specific financial or identifying details are withheld. The static checker does not predict authorization, replace IAM simulation or Access Analyzer, or serve as a security gate for real policies.

## Next improvements

Extend the policy example only when another construct has a concrete test case, and continue to label every unsupported IAM feature explicitly. For cost review, record the selected billing period and filters alongside any future observation.
