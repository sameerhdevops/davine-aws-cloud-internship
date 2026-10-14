# Terraform validation checklist

## Latest Windows run (2026-10-14)

Terraform v1.16.5, Windows `windows_amd64`, locked `hashicorp/aws` provider v5.100.0:

- [x] `terraform fmt -check` — passed, exit code 0.
- [x] `terraform init -backend=false -input=false -no-color` — initialized using the provider selected by `.terraform.lock.hcl`, exit code 0. No remote backend was configured.
- [ ] `terraform validate -no-color` — **not completed**. The local AWS provider plugin failed to respond to Terraform's `GetProviderSchema` request. See the verbatim safe output in the [validation record](../../../../evidence/validation/terraform/local-validation-2026-10-14.md).

An earlier validation note reported a successful local validation after a lifecycle-rule warning was corrected with an explicit empty `filter {}`. A fresh rerun in this release environment did not reproduce that result because the provider process failed before returning its schema. The earlier observation is not used as a substitute for the latest result.

The release-branch [GitHub Actions run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38515781949) passed formatting, backend-free initialization, and validation for commit `33ef86f22bb362894d9460fd6bce2aae0bb9a480`; the [run record](../../../../evidence/validation/terraform/github-actions-release-2026-10-14.md) documents the full scope. This validates the Terraform source against provider schemas only. It does not produce a plan or establish deployed resources.

## Earlier plan attempt

A separate, earlier validation record noted one `terraform plan` invocation using a temporary bucket-name value. It failed before producing a plan because valid AWS credentials were unavailable. No resource changes followed. This portfolio update did not run `terraform plan`.

## Plan and deployment status

No Terraform plan was produced. No `terraform apply`, `terraform destroy`, AWS CLI deployment, CloudFormation deployment, or cloud resource operation was run during this portfolio update. The infrastructure is **not deployed**.

`terraform validate` is static configuration/schema validation. It is not a plan and does not establish an AWS deployment. The workflow has no AWS credentials and no plan or deployment step.

## Safety limits

Before any real deployment, obtain explicit authorization, replace the example S3 bucket name with an available globally unique name, review current service pricing, configure credentials outside the repository, and inspect an approved plan. Never publish state, credentials, or real `.tfvars` values.

## Future sandbox evidence checklist

This section is intentionally empty. No live sandbox was created or inspected. Only complete items after a separately authorized and funded exercise, and keep source records private until checked for publication.

- [ ] Record approved account/Region scope in a private log; do not publish account IDs.
- [ ] Record the exact source commit, Terraform/provider versions, and operator window.
- [ ] Capture the approved change summary with sensitive identifiers redacted.
- [ ] Verify the created resource inventory, routes, security groups, S3 controls, IAM role/profile relationships, and any data-retention behavior.
- [ ] If notification testing is in scope, verify subscription confirmation and delivery separately from topic/alarm creation.
- [ ] Record cleanup verification and the final billing review.
- [ ] Publish only a reviewed derivative whose caption states what it shows and does not show.
