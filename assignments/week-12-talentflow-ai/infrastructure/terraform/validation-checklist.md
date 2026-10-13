# Local validation checklist

## Commands and results (2026-10-13, Terraform v1.16.5)

- [x] `terraform fmt -check` — passed (exit code 0; it also passed before the lifecycle correction below).
- [x] `terraform init -backend=false` — succeeded; installed `hashicorp/aws` provider v5.100.0, pinned in `.terraform.lock.hcl`.
- [x] `terraform validate` — passed: `Success! The configuration is valid.` with no warnings, after the correction below.

## Lifecycle-warning correction

The first validation cycle reported a lifecycle-configuration warning for `aws_s3_bucket_lifecycle_configuration.resumes`. An explicit empty `filter {}` was added to the rule `cleanup-noncurrent-versions-and-incomplete-uploads` in `main.tf`. The rule's behavior is unchanged: incomplete multipart uploads are aborted after 7 days and noncurrent object versions expire after 30 days. `terraform fmt` then completed successfully and `terraform validate` passed with no warnings. A backup of the pre-correction file (`main.tf.backup-20261013-131006`) is preserved outside the repository.

## Plan/apply status

A `terraform plan` attempt was made once on 2026-10-13 using a temporary S3 bucket-name value; it failed before producing any plan because valid AWS credentials were unavailable. No plan output was generated, no `terraform apply` or `terraform destroy` was run, and no AWS resources were created, modified, or charged.

Validating Terraform syntax locally is not the same as planning or deploying. No plan has been produced and this infrastructure is not deployed.

## Restrictions for this portfolio review

For this review, do not run `terraform plan`, `terraform apply`, or `terraform destroy`, do not configure AWS credentials, and do not create or modify AWS resources by any means. Applying this configuration would incur AWS charges (see the [Terraform README](README.md)); any deployment is out of scope until separately authorized.
