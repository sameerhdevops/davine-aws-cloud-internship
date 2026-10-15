# Week 10 — Governance, security, and cost

## Objective

I wanted to review account-level security signals, governance findings, policy scope, and billing context without treating a dashboard tile as a complete assessment.

## What I did or implemented

The portfolio’s audit and activity notes cover root-account signals, Trusted Advisor checks, Well-Architected review state, and billing views. One capture reports 0 of 57 Well-Architected questions answered and 0 issues recorded, not a completed review. The billing views used different filters and periods: one Cost Explorer view reported $0, while a budget view reported spend above its $1 budget and a higher forecast, so those values should not be combined. The local [policy checker](../../demos/week10_governance/policy_check.py) and [example policy](../../demos/week10_governance/example-policy.json) validate a bounded subset: `Version` 2012-10-17, explicit `Allow`, `s3:GetObject` or `s3:PutObject`, and named-bucket object ARNs. It rejects unsupported fields and wildcard bucket scope, but is neither a full bucket-name validator nor an IAM evaluator.

## Key concepts

- **Effective access:** Review identity and resource policies, trust relationships, conditions, boundaries, service control policies, and effective permissions rather than relying on a single dashboard tile.
- **Cost context:** Read billing values with their period and filters; set budgets, tag ownership and environment, and include cleanup in lab planning.
- **Policy-checking scope:** A small static checker can catch cases it explicitly supports, but passing it does not predict whether AWS would authorize a request.

## Evidence and links

![IAM dashboard crop reporting root MFA enabled and no active root access keys at capture time.](../../evidence/assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png)

*The crop shows dashboard-reported root controls at that time, not who configured them or least privilege across other identities.*

![Trusted Advisor crop reporting zero public EBS and RDS snapshots in the displayed checks.](../../evidence/assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png)

*The crop shows the displayed checks only; it does not establish a complete account review or the unexpanded S3 check.* See the [gallery](../../evidence/README.md#week-10-governance-security-and-cost), [governance notes](../../cross-cutting/aws-security-governance-cost/README.md), and [demo catalog](../../demos/README.md).

## Limitations

Billing and raw review captures with account-specific financial or identifying details are not published. The static checker does not predict authorization, replace IAM simulation or Access Analyzer, or serve as a security gate for real policies.

## Next improvements

Extend the policy example only when another construct has a concrete test case, and record billing periods and filters alongside future cost observations.
