# Security notes

## AWS activity boundary

This repository does not require AWS credentials to run unit tests, local demonstrations, Markdown checks, Python lint/format checks, or Terraform formatting and schema validation. The Terraform is not applied. The AWS audit tool issues only read operations: EC2 `DescribeInstances` and `DescribeSecurityGroups`; S3 `ListBuckets`, `GetBucketLocation`, `GetBucketTagging`, `GetPublicAccessBlock`, `GetBucketPolicyStatus`, and `GetBucketAcl`.

The audit does not create CloudWatch metrics or resources. AWS service request pricing may still apply; check [current AWS pricing](https://aws.amazon.com/vpc/pricing/) and service-specific pricing before running any audit at scale. Use a role with only the required read permissions listed in the [audit guide](../scripts/aws_audit/README.md).

## Report and evidence handling

Audit reports contain bucket names, instance IDs, security-group IDs, tag-key names, and detected rule details. They are written only when an output path is requested, and the CLI requires an explicit acknowledgement for report files. Keep real reports private and review them before sharing. The committed sample reports are synthetic and do not contain account data.

No AWS credential, account ID, live endpoint, private key, Terraform state, plan file, or original internship source file is required or included for local checks. Do not commit `.env`, real `.tfvars`, credentials, generated AWS reports, or Terraform state.

## Audit limitations

The AWS audit is a bounded configuration snapshot. It does not evaluate effective IAM permissions, SCPs, account-level S3 Block Public Access, every object ACL, cross-account access, network routes, NACLs, application behavior, or findings outside the selected Region for EC2/security groups. `UNKNOWN` and `NOT_CONFIGURED` results require review; they are never reported as passes. See [scope](SCOPE.md).
