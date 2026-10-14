# Cross-cutting review — security, governance, and cost

This page consolidates the Week 10 audit observations and security/cost reasoning. Source reports and raw screenshots remain private; selected sanitized screenshots are embedded in the [Week 10 page](../../assignments/week-10-governance-audit/README.md) and [evidence gallery](../../evidence/README.md).

## Evidence interpretation

- **IAM dashboard:** one screenshot reports root MFA enabled and no active root access keys at an unknown capture time. A report and another console view differ on some root-account details. The capture dates/context do not resolve the difference, so no single current-state conclusion is asserted.
- **Trusted Advisor:** the displayed checks report zero public EBS snapshots and zero public RDS snapshots. The S3 check is not expanded; this is not a clean account-wide assessment.
- **Well-Architected Tool:** the screenshot shows 0 of 57 questions answered and 0 issues displayed. It is not evidence of a completed review.
- **Billing:** the Cost Explorer capture shows $0 under its selected date/filter view. A separate budget capture shows spend above a $1 budget and a higher forecast, with exceeded alerts. These are different screens and contexts; the amounts are not combined into a monthly or account-wide claim. Billing screenshots are withheld.

These are historical observations, not current account state. The portal schedule marks Week 10 Completed only in the user-reported status; no portal screenshot/export was found, and the supplied submission history says “No weekly submissions yet.”

## Independent least-privilege example

The [Week 10 policy example](../../demos/week10_governance/example-policy.json) permits `GetObject` and `PutObject` on object ARNs under one named example bucket. The adjacent Python checker enforces only a deliberately narrow static allow-list. It is not the AWS IAM policy simulator, Access Analyzer, or a substitute for reviewing trust policies, conditions, permissions boundaries, SCPs, resource policies, and effective access.

## Operational checklist

1. Inventory identity and resource policies, trust relationships, MFA, root access keys, and long-lived credentials.
2. Scope storage permissions to required buckets/prefixes and review public-access controls independently from encryption.
3. Enable relevant audit/metric/log sources and verify that alert actions are deliverable; `Insufficient data` is not an alert success.
4. Set budgets/notifications before experiments, review selected dates/filters, and tag resources for owner and cleanup.
5. Recheck bills, unattached public IPs, storage versions, logs, alarms, and any temporary network path during teardown.

The audit artifacts do not establish production operation, complete account coverage, or employer endorsement. See the [evidence manifest](../../evidence/manifest.csv) and [classification policy](../../docs/evidence-and-validation.md).
