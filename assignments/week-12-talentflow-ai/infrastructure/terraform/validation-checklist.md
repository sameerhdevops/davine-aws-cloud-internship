# Terraform validation checklist

## Latest Windows run (2026-10-13)

Terraform v1.16.5, Windows `windows_amd64`, locked `hashicorp/aws` provider v5.100.0:

- [x] `terraform fmt -check` — passed, exit code 0.
- [x] `terraform init -backend=false -input=false -no-color` — initialized using the provider selected by `.terraform.lock.hcl`, exit code 0. No remote backend was configured.
- [ ] `terraform validate -no-color` — **not completed**. The local AWS provider plugin failed to respond to Terraform's `GetProviderSchema` request. See the verbatim safe output in the [validation record](../../../../evidence/validation/terraform/local-validation-2026-10-13.md).

An earlier validation note reported a successful local validation after a lifecycle-rule warning was corrected with an explicit empty `filter {}`. A fresh rerun in this release environment did not reproduce that result because the provider process failed before returning its schema. The earlier observation is not used as a substitute for the latest result.

The GitHub Actions workflow runs `fmt -check`, backend-free `init`, and `validate` on Ubuntu. The root README should state its result only after the run completes successfully.

## Earlier plan attempt

A separate, earlier validation record noted one `terraform plan` invocation using a temporary bucket-name value. It failed before producing a plan because valid AWS credentials were unavailable. No resource changes followed. This portfolio update did not run `terraform plan`.

## Plan and deployment status

No Terraform plan was produced. No `terraform apply`, `terraform destroy`, AWS CLI deployment, CloudFormation deployment, or cloud resource operation was run during this portfolio update. The infrastructure is **not deployed**.

`terraform validate` is static configuration/schema validation. It is not a plan and does not establish an AWS deployment. The workflow has no AWS credentials and no plan or deployment step.

## Safety limits

Before any real deployment, obtain explicit authorization, replace the example S3 bucket name with an available globally unique name, review current service pricing, configure credentials outside the repository, and inspect an approved plan. Never publish state, credentials, or real `.tfvars` values.
