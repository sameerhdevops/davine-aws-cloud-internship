# TalentFlow AI — reconstructed Terraform baseline

This is independent portfolio source written after reviewing the internship materials. It is **not** a recovered copy of the original Week 7 or Week 12 Terraform files, and it has not been applied to AWS. The [architecture diagram](architecture.mmd) describes only resources declared by this configuration and labels future application tiers separately.

## What the configuration declares

- One VPC, an Internet Gateway, two public subnets with an Internet Gateway default route, and two isolated private subnets with separate route tables and local routes only.
- Three security groups modelling a future ingress → application → database chain. These are rules and groups only: there is **no** Application Load Balancer, EC2 instance, RDS instance, target group, listener, or application.
- A private S3 general-purpose bucket with all four Block Public Access settings, bucket-owner-enforced ownership, versioning, SSE-S3 (`AES256`), a deny policy for insecure transport, and a lifecycle rule for incomplete uploads and noncurrent versions. The example bucket name must be replaced by an available, globally unique name before any real deployment.
- An EC2-trust IAM role, a bucket-scoped read-only policy, and an instance profile for a future EC2 workload. No instance is created or attached.
- A CloudWatch log group with bounded retention, an SNS topic, and a daily S3 `BucketSizeBytes` alarm for `StandardStorage`. No log producer, notification subscription, or application is configured.

## Network boundary

The public route table has `0.0.0.0/0` through the Internet Gateway, but `map_public_ip_on_launch` is disabled. This makes those subnets routable to the Internet Gateway, but does not itself give future instances public addresses. Any future public-facing tier needs an explicit addressing/load-balancing design.

Each private subnet has its own route table with no NAT Gateway, egress route, or VPC endpoint. It is intentionally isolated and cannot reach public package repositories or public AWS endpoints. The EC2 security group's HTTPS egress rule does not create a network route. Add NAT or service-specific VPC endpoints only when a real workload requires them and their security and cost implications have been reviewed.

The ALB, EC2, and RDS security groups are preparatory configuration resources. Their rules do not expose a running load balancer, application, or database because this configuration creates no matching compute, load-balancer, or database resources.

## Security and cost considerations

- Replace `s3_bucket_name` in [`terraform.tfvars.example`](terraform.tfvars.example) with an available, globally unique name before any real deployment. Never commit credentials, account IDs, state files, or a real `.tfvars` file.
- SSE-S3 is deliberately selected. S3 Bucket Keys apply to SSE-KMS, so `bucket_key_enabled` is omitted from this SSE-S3 configuration. See the [AWS S3 Bucket Keys guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) and the [Terraform provider resource reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_server_side_encryption_configuration).
- The bucket enforces public-access blocks, bucket-owner-enforced ownership, and TLS-only transport through an explicit deny policy. The IAM role is scoped to list/read operations on this bucket. The role is not attached to a created instance.
- The S3 `BucketSizeBytes` metric is daily and supports the `Average` statistic for the `StandardStorage` dimension, so the alarm is not a real-time storage monitor. It requires the bucket's daily metric data to arrive. The resource treats missing data as not breaching, so it does not detect a missing metric stream. The SNS topic has no subscription, so no recipient is configured. See [S3 metric dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html) and the [alarm configuration](main.tf).
- If applied, S3 storage, requests, retained object versions, CloudWatch alarm/log ingestion and retention, SNS delivery, and any future network or compute resources can incur charges. This project makes no precise cost estimate. Check current AWS pricing before any separately authorized deployment.
- No AWS credentials are needed for formatting or provider-schema validation. `terraform init -backend=false` may download the provider, but does not configure a remote state backend.

## Local validation

From this directory, the checks are:

```powershell
terraform fmt -check
terraform init -backend=false -input=false
terraform validate
```

The latest Windows run on 2026-10-13 used Terraform v1.16.5 and the locked AWS provider v5.100.0. Formatting and initialization passed. Validation could not load the provider schema because the local provider plugin did not respond. The exact outcome is in the [local validation record](../../../../evidence/validation/terraform/local-validation-2026-10-13.md). GitHub Actions independently runs all three checks on Ubuntu; the root README records the result after a real run completes.

Do not run `terraform plan`, `terraform apply`, or `terraform destroy` for this portfolio review. A separately recorded earlier plan invocation failed before producing a plan because valid AWS credentials were unavailable; this update did not run a plan. No cloud resource should be created to inspect or validate this code.

## Files

- [Architecture source](architecture.mmd)
- [Provider/version constraints](versions.tf)
- [Inputs](variables.tf) and [safe example values](terraform.tfvars.example)
- [Resources](main.tf) and [outputs](outputs.tf)
- [Terraform-specific ignore rules](.gitignore)
