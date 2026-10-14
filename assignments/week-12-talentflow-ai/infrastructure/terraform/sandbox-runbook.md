# Future sandbox runbook

This runbook is a review checklist for a **future, separately authorized and funded** sandbox exercise. The current portfolio budget is ₹0. No deployment is part of this repository review, and this document does not authorize one.

## Before any live exercise

- [ ] Confirm written approval, account ownership, Region, and a bounded exercise window.
- [ ] Use a dedicated sandbox account with MFA and a least-privilege operator role; do not use production credentials.
- [ ] Review current VPC, EC2, S3, CloudWatch, SNS, and data-transfer pricing. Account for public IPv4 use, storage/versioning, and any later application tiers.
- [ ] Decide who pays for the exercise and configure an alert or spending control that is available in that account. A budget alert may not prevent charges.
- [ ] Confirm that the example bucket name is available and globally unique. Use synthetic data only; do not use candidate resumes or personal information.
- [ ] Decide where Terraform state will live, how it will be encrypted and access-controlled, and how concurrent state changes will be prevented. Do not commit local state or plans.
- [ ] Review the planned topology and security-group rules. Keep SSH disabled unless there is an approved, temporary `/32` administrator source.
- [ ] Decide whether the incomplete application dependencies are acceptable for the exercise. This Terraform alone cannot serve TalentFlow AI.

## Static preparation

From this directory, run only the repository's safe checks:

```powershell
terraform fmt -check
terraform init -backend=false -input=false -lockfile=readonly
terraform validate
```

These checks do not access AWS or establish a deployment plan. If a later exercise is separately approved and funded, its operator must review current provider documentation, the exact plan, expected resource changes, costs, rollback, and cleanup before any provisioning. That live workflow is intentionally outside this portfolio runbook.

## During and after an approved exercise

- [ ] Keep a private inventory of approved resources and the actual operator/session. Do not publish credentials, account identifiers, endpoints, or unredacted output.
- [ ] Confirm only the intended resources exist and that public ingress, route associations, and S3 controls match the approved design.
- [ ] Treat the S3 `BucketSizeBytes` alarm as a daily metric, not an immediate threshold monitor. Confirm metric availability and alarm configuration separately.
- [ ] Confirm an SNS subscription independently if notification delivery is part of the exercise; a topic alone does not deliver email.
- [ ] Before cleanup, identify dependent resources and protect any data that must be retained. Empty all current and noncurrent S3 object versions before attempting bucket deletion because `force_destroy` is disabled.
- [ ] Verify the final resource inventory and billing view, then retain only redacted evidence that supports a precise, time-bounded claim.

Do not check off these items from source code alone. No sandbox work is represented as completed in this repository.
