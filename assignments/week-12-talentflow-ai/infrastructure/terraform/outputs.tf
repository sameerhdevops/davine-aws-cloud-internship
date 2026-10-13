# =============================================================================
# TalentFlow AI — Terraform Outputs
# =============================================================================

output "vpc_id" {
  description = "ID of the dedicated TalentFlow VPC."
  value       = aws_vpc.main.id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway attached to the TalentFlow VPC."
  value       = aws_internet_gateway.main.id
}

output "public_subnet_ids" {
  description = "List of IDs for the multi-AZ public subnets."
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "List of IDs for the multi-AZ isolated private subnets."
  value       = aws_subnet.private[*].id
}

output "alb_security_group_id" {
  description = "ID of the Application Load Balancer tier Security Group (TalentFlow-ALB-SG)."
  value       = aws_security_group.alb.id
}

output "ec2_security_group_id" {
  description = "ID of the EC2 compute tier Security Group (TalentFlow-EC2-SG)."
  value       = aws_security_group.ec2.id
}

output "rds_security_group_id" {
  description = "ID of the RDS database tier Security Group (TalentFlow-RDS-SG)."
  value       = aws_security_group.rds.id
}

output "s3_resume_bucket_name" {
  description = "Name of the private, encrypted S3 bucket for candidate resumes."
  value       = aws_s3_bucket.resumes.id
}

output "s3_resume_bucket_arn" {
  description = "ARN of the private, encrypted S3 bucket for candidate resumes."
  value       = aws_s3_bucket.resumes.arn
}

output "iam_role_name" {
  description = "Name of the least-privilege IAM Role for EC2 S3 read access."
  value       = aws_iam_role.ec2_s3_role.name
}

output "iam_role_arn" {
  description = "ARN of the least-privilege IAM Role for EC2 S3 read access."
  value       = aws_iam_role.ec2_s3_role.arn
}

output "cloudwatch_log_group_name" {
  description = "Name of the CloudWatch Log Group with bounded retention."
  value       = aws_cloudwatch_log_group.app_logs.name
}

output "sns_alerts_topic_arn" {
  description = "ARN of the encrypted SNS topic for operational alerts."
  value       = aws_sns_topic.alerts.arn
}

output "cloudwatch_storage_alarm_name" {
  description = "Name of the S3 storage warning CloudWatch Metric Alarm."
  value       = aws_cloudwatch_metric_alarm.storage_warning.alarm_name
}
