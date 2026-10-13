# TalentFlow AI — reconstructed Terraform baseline

This is independently reconstructed portfolio code, added after the internship evidence review. It is **not** a recovered copy of the original Week 7 or Week 12 Terraform files, and it has not been applied to AWS.

## What it declares if applied

- One VPC, internet gateway, two route-table-associated public subnets, and two isolated private subnets across two Availability Zones.
- Three security groups modelling a future ingress → application → database chain. They are rules and groups only: this configuration creates **no** Application Load Balancer, EC2 instance, RDS instance, target group, listener, or application.
- A private S3 general-purpose bucket with public-access blocks, bucket-owner-enforced ownership, versioning, SSE-S3 (`AES256`), a deny policy for insecure transport, and a lifecycle rule for incomplete uploads and noncurrent versions.
- An EC2-trust IAM role, its read-only S3 policy, and an instance profile for a future EC2 workload. No EC2 instance is attached to it.
- A CloudWatch Log Group with bounded retention, an SNS topic, and a daily S3 `BucketSizeBytes` alarm for the `StandardStorage` dimension. No log producer or SNS subscription is configured.

## Network boundary and limitations

The public route table has `0.0.0.0/0` through the Internet Gateway, but `map_public_ip_on_launch` is disabled. A future public-facing workload would need a deliberate addressing/load-balancing design. Each private subnet has its own route table with no NAT Gateway or outbound route; it is intentionally isolated and cannot reach package repositories or public AWS endpoints. Add a NAT Gateway or VPC endpoints only when an actual workload requires them and their cost/security trade-offs are accepted.

The ALB, EC2, and RDS security groups are preparatory configuration resources. The public HTTP/HTTPS rules do not expose a running load balancer because no load balancer or network interface is created by this code.

## Security and cost notes

- Replace `s3_bucket_name` in [`terraform.tfvars.example`](terraform.tfvars.example) with an available, globally unique name before any real deployment. Never add credentials, account IDs, state files, or real `.tfvars` files to Git.
- SSE-S3 is deliberately used. S3 Bucket Keys are an SSE-KMS feature, so `bucket_key_enabled` is not configured. See [AWS guidance on S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html).
- The storage alarm uses S3 daily storage metrics; `BucketSizeBytes` supports `Average` and the `StandardStorage` dimension. Metric timing is not real-time. See [S3 metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html).
- Applying this configuration can incur AWS charges for S3 storage/requests/versioned objects, CloudWatch alarm and log ingestion/retention, SNS notifications/delivery, and any future resources. No precise estimate is claimed here; consult current service pricing before deployment.

## Local validation only

Run these non-deploying commands from this directory. On 2026-10-13 with Terraform v1.16.5, all three passed locally after a lifecycle-configuration `filter {}` correction; results are recorded in [validation-checklist.md](validation-checklist.md).

```powershell
terraform fmt -check
terraform init -backend=false
terraform validate
```

`init -backend=false` may download the pinned AWS provider but does not configure remote state. Do not run `terraform plan`, `terraform apply`, or `terraform destroy` for this portfolio review.

## Files

- [Architecture source](architecture.mmd)
- [Provider/version constraints](versions.tf)
- [Inputs](variables.tf) and [safe example values](terraform.tfvars.example)
- [Resources](main.tf) and [outputs](outputs.tf)
- [Terraform-specific ignore rules](.gitignore)
