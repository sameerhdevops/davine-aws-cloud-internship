# =============================================================================
# TalentFlow AI — Core Baseline Infrastructure
# Provenance: Newly reconstructed Terraform configuration codifying the
# VPC networking, tiered security groups, private S3 storage, least-privilege
# IAM role, CloudWatch logging/alarming, and SNS alerting. This is independently
# reconstructed portfolio code; it is not a recovered internship source file.
#
# Cost boundary:
# - Declares no EC2 instances, RDS databases, ALBs, or NAT Gateways.
# - Other declared resources may incur charges if this configuration is applied.
# - Automatic public IPv4 assignment is disabled on all subnets. This setting
#   does not prevent other public IPv4 addresses or resources from incurring charges.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. VPC & Internet Gateway
# -----------------------------------------------------------------------------

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "${var.project_name}-vpc"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-igw"
  }
}

# -----------------------------------------------------------------------------
# 2. Multi-AZ Public & Isolated Private Subnets
# -----------------------------------------------------------------------------

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)

  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = false

  tags = {
    Name = "${var.project_name}-subnet-public${count.index + 1}-${var.availability_zones[count.index]}"
    Tier = "Public"
  }
}

resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidrs)

  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.private_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = false

  tags = {
    Name = "${var.project_name}-subnet-private${count.index + 1}-${var.availability_zones[count.index]}"
    Tier = "Private"
  }
}

# -----------------------------------------------------------------------------
# 3. Route Tables & Associations (No NAT Gateway to Prevent Hourly Charges)
# -----------------------------------------------------------------------------

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-rtb-public"
  }
}

resource "aws_route" "public_internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.main.id
}

resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public)

  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  count = length(aws_subnet.private)

  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-rtb-private${count.index + 1}-${var.availability_zones[count.index]}"
  }
}

resource "aws_route_table_association" "private" {
  count = length(aws_subnet.private)

  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# A gateway endpoint keeps private-subnet access to the resume bucket on the
# AWS network without adding a NAT Gateway or public egress route.
resource "aws_vpc_endpoint" "s3" {
  vpc_id            = aws_vpc.main.id
  service_name      = "com.amazonaws.${var.aws_region}.s3"
  vpc_endpoint_type = "Gateway"
  route_table_ids   = aws_route_table.private[*].id

  tags = {
    Name = "${var.project_name}-S3-Gateway-Endpoint"
  }
}

# -----------------------------------------------------------------------------
# 4. Tiered Security Groups (ALB -> EC2 -> RDS)
# -----------------------------------------------------------------------------

# 4A. Application Load Balancer Security Group
resource "aws_security_group" "alb" {
  name        = "${var.project_name}-ALB-SG"
  description = "Allows inbound HTTP/HTTPS traffic from the internet and forwards HTTP to the VPC."
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-ALB-SG"
  }
}

resource "aws_vpc_security_group_ingress_rule" "alb_http" {
  security_group_id = aws_security_group.alb.id
  description       = "Allow inbound HTTP from internet"
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  ip_protocol       = "tcp"
  to_port           = 80
}

resource "aws_vpc_security_group_ingress_rule" "alb_https" {
  security_group_id = aws_security_group.alb.id
  description       = "Allow inbound HTTPS from internet"
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

resource "aws_vpc_security_group_egress_rule" "alb_to_vpc_http" {
  security_group_id            = aws_security_group.alb.id
  description                  = "Allow outbound HTTP traffic only to the application tier"
  referenced_security_group_id = aws_security_group.ec2.id
  from_port                    = 80
  ip_protocol                  = "tcp"
  to_port                      = 80
}

# 4B. EC2 Application Tier Security Group
resource "aws_security_group" "ec2" {
  name        = "${var.project_name}-EC2-SG"
  description = "Allows inbound HTTP strictly from the ALB security group; optional /32 SSH."
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-EC2-SG"
  }
}

resource "aws_vpc_security_group_ingress_rule" "ec2_http_from_alb" {
  security_group_id            = aws_security_group.ec2.id
  description                  = "Allow inbound HTTP solely from TalentFlow-ALB-SG"
  referenced_security_group_id = aws_security_group.alb.id
  from_port                    = 80
  ip_protocol                  = "tcp"
  to_port                      = 80
}

resource "aws_vpc_security_group_ingress_rule" "ec2_ssh_restricted" {
  count = var.enable_ssh_ingress ? 1 : 0

  security_group_id = aws_security_group.ec2.id
  description       = "Allow restricted SSH access from a single /32 administrator IP"
  cidr_ipv4         = var.allowed_ssh_cidr
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_egress_rule" "ec2_to_rds_mysql" {
  security_group_id            = aws_security_group.ec2.id
  description                  = "Allow outbound MySQL traffic only to the database tier"
  referenced_security_group_id = aws_security_group.rds.id
  from_port                    = 3306
  ip_protocol                  = "tcp"
  to_port                      = 3306
}

resource "aws_vpc_security_group_egress_rule" "ec2_https_to_s3" {
  security_group_id = aws_security_group.ec2.id
  description       = "Allow HTTPS only to the regional S3 gateway endpoint prefix list"
  prefix_list_id    = aws_vpc_endpoint.s3.prefix_list_id
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

# 4C. RDS Database Tier Security Group
resource "aws_security_group" "rds" {
  name        = "${var.project_name}-RDS-SG"
  description = "Allows inbound MySQL (3306) strictly from TalentFlow-EC2-SG; zero public access."
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-RDS-SG"
  }
}

resource "aws_vpc_security_group_ingress_rule" "rds_mysql_from_ec2" {
  security_group_id            = aws_security_group.rds.id
  description                  = "Allow inbound MySQL traffic exclusively from TalentFlow-EC2-SG"
  referenced_security_group_id = aws_security_group.ec2.id
  from_port                    = 3306
  ip_protocol                  = "tcp"
  to_port                      = 3306
}

# -----------------------------------------------------------------------------
# 5. Private Encrypted Amazon S3 Bucket for Candidate Resumes
# -----------------------------------------------------------------------------

resource "aws_s3_bucket" "resumes" {
  bucket        = var.s3_bucket_name
  force_destroy = false

  tags = {
    Name    = var.s3_bucket_name
    Purpose = "CandidateResumeStorage"
  }
}

resource "aws_s3_bucket_ownership_controls" "resumes" {
  bucket = aws_s3_bucket.resumes.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_public_access_block" "resumes" {
  bucket = aws_s3_bucket.resumes.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

data "aws_iam_policy_document" "resumes_bucket_policy" {
  statement {
    sid     = "DenyInsecureTransport"
    effect  = "Deny"
    actions = ["s3:*"]

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    resources = [
      aws_s3_bucket.resumes.arn,
      "${aws_s3_bucket.resumes.arn}/*",
    ]

    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }
}

resource "aws_s3_bucket_policy" "resumes" {
  bucket = aws_s3_bucket.resumes.id
  policy = data.aws_iam_policy_document.resumes_bucket_policy.json
}

resource "aws_s3_bucket_versioning" "resumes" {
  bucket = aws_s3_bucket.resumes.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "resumes" {
  bucket = aws_s3_bucket.resumes.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
    # S3 Bucket Keys apply to SSE-KMS, not SSE-S3 (AES256). This baseline
    # deliberately uses cost-conscious SSE-S3 and therefore does not set one.
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "resumes" {
  bucket = aws_s3_bucket.resumes.id

  rule {
    id     = "cleanup-noncurrent-versions-and-incomplete-uploads"
    status = "Enabled"
    filter {}

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }

    noncurrent_version_expiration {
      noncurrent_days = 30
    }
  }

  depends_on = [aws_s3_bucket_versioning.resumes]
}

# -----------------------------------------------------------------------------
# 6. Least-Privilege IAM Role & Policy (Scoped to TalentFlow Resume Bucket)
# -----------------------------------------------------------------------------

data "aws_iam_policy_document" "ec2_assume_role" {
  statement {
    sid     = "AllowEC2ServiceAssumeRole"
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "ec2_s3_role" {
  name               = "${var.project_name}-EC2-S3-Role"
  description        = "Least-privilege IAM role allowing EC2 instances to read objects only from the TalentFlow resume bucket."
  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json

  tags = {
    Name = "${var.project_name}-EC2-S3-Role"
  }
}

data "aws_iam_policy_document" "s3_least_privilege" {
  statement {
    sid       = "AllowListResumeBucket"
    effect    = "Allow"
    actions   = ["s3:ListBucket", "s3:GetBucketLocation"]
    resources = [aws_s3_bucket.resumes.arn]
  }

  statement {
    sid       = "AllowReadResumeObjects"
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:GetObjectVersion"]
    resources = ["${aws_s3_bucket.resumes.arn}/*"]
  }
}

resource "aws_iam_role_policy" "ec2_s3_least_privilege" {
  name   = "${var.project_name}-S3-Resume-ReadOnly-Policy"
  role   = aws_iam_role.ec2_s3_role.id
  policy = data.aws_iam_policy_document.s3_least_privilege.json
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "${var.project_name}-EC2-Instance-Profile"
  role = aws_iam_role.ec2_s3_role.name
}

# -----------------------------------------------------------------------------
# 7. CloudWatch Log Group, SNS Topic, and CloudWatch Storage Alarm
# -----------------------------------------------------------------------------

resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/talentflow/${var.environment}/application"
  retention_in_days = var.log_retention_days

  tags = {
    Name = "${var.project_name}-App-LogGroup"
  }
}

resource "aws_sns_topic" "alerts" {
  name              = "${var.project_name}-Alerts"
  kms_master_key_id = "alias/aws/sns"

  tags = {
    Name = "${var.project_name}-Alerts"
  }
}

resource "aws_cloudwatch_metric_alarm" "storage_warning" {
  alarm_name          = "${var.project_name}-Storage-Warning"
  alarm_description   = "Triggers when the TalentFlow S3 resume bucket exceeds the configured byte threshold."
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "BucketSizeBytes"
  namespace           = "AWS/S3"
  period              = 86400
  statistic           = "Average"
  threshold           = var.s3_storage_warning_threshold_bytes
  treat_missing_data  = "notBreaching"

  dimensions = {
    BucketName  = aws_s3_bucket.resumes.id
    StorageType = "StandardStorage"
  }

  alarm_actions = [aws_sns_topic.alerts.arn]

  tags = {
    Name = "${var.project_name}-Storage-Warning"
  }
}
