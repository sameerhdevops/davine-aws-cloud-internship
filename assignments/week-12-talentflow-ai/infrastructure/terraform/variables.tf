# =============================================================================
# TalentFlow AI — Input Variables and Security Validations
# =============================================================================

variable "aws_region" {
  description = "AWS region for deploying TalentFlow AI baseline infrastructure."
  type        = string
  default     = "ap-south-1"

  validation {
    condition     = can(regex("^[a-z0-9]{2,4}(-[a-z0-9]+)*-[0-9]+$", var.aws_region))
    error_message = "Use a lowercase AWS-style region identifier, for example ap-south-1; this check does not verify region availability."
  }
}

variable "project_name" {
  description = "Project prefix applied to resource names and tags."
  type        = string
  default     = "TalentFlow"

  validation {
    condition     = can(regex("^[A-Za-z0-9-]+$", var.project_name))
    error_message = "The project_name may only contain alphanumeric characters and hyphens."
  }
}

variable "environment" {
  description = "Deployment environment identifier (dev, staging, or prod)."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "The environment must be one of: dev, staging, prod."
  }
}

variable "vpc_cidr" {
  description = "Primary IPv4 CIDR block for the TalentFlow VPC."
  type        = string
  default     = "10.0.0.0/16"

  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0)) && can(cidrnetmask(var.vpc_cidr))
    error_message = "The vpc_cidr must be a valid IPv4 CIDR block."
  }
}

variable "availability_zones" {
  description = "List of two Availability Zones within the selected region for high-availability subnet placement."
  type        = list(string)
  default     = ["ap-south-1a", "ap-south-1b"]

  validation {
    condition     = length(var.availability_zones) == 2 && length(distinct(var.availability_zones)) == 2
    error_message = "Exactly two distinct Availability Zones must be provided."
  }
}

variable "public_subnet_cidrs" {
  description = "Two distinct IPv4 CIDR blocks for the public subnets; cross-subnet overlap and containment are not checked."
  type        = list(string)
  default     = ["10.0.0.0/20", "10.0.16.0/20"]

  validation {
    condition = (
      length(var.public_subnet_cidrs) == 2 &&
      length(distinct(var.public_subnet_cidrs)) == 2 &&
      alltrue([for cidr in var.public_subnet_cidrs : can(cidrhost(cidr, 0)) && can(cidrnetmask(cidr))])
    )
    error_message = "Provide two distinct, valid IPv4 CIDR blocks for public_subnet_cidrs."
  }
}

variable "private_subnet_cidrs" {
  description = "Two distinct IPv4 CIDR blocks for the private subnets; cross-subnet overlap and containment are not checked."
  type        = list(string)
  default     = ["10.0.128.0/20", "10.0.144.0/20"]

  validation {
    condition = (
      length(var.private_subnet_cidrs) == 2 &&
      length(distinct(var.private_subnet_cidrs)) == 2 &&
      alltrue([for cidr in var.private_subnet_cidrs : can(cidrhost(cidr, 0)) && can(cidrnetmask(cidr))])
    )
    error_message = "Provide two distinct, valid IPv4 CIDR blocks for private_subnet_cidrs."
  }
}

variable "s3_bucket_name" {
  description = "A globally unique private TalentFlow resume-bucket name using this module's lowercase alphanumeric/hyphen subset."
  type        = string

  validation {
    condition = (
      can(regex("^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$", var.s3_bucket_name)) &&
      !startswith(var.s3_bucket_name, "xn--") &&
      !startswith(var.s3_bucket_name, "sthree-") &&
      !startswith(var.s3_bucket_name, "amzn-s3-demo-") &&
      !endswith(var.s3_bucket_name, "-s3alias") &&
      !endswith(var.s3_bucket_name, "--ol-s3") &&
      !endswith(var.s3_bucket_name, "--x-s3") &&
      !endswith(var.s3_bucket_name, "--table-s3") &&
      !endswith(var.s3_bucket_name, "-an")
    )
    error_message = "Use 3-63 lowercase letters, numbers, or internal hyphens; avoid reserved S3 prefixes/suffixes. This subset excludes dotted and account-regional names."
  }
}

variable "enable_ssh_ingress" {
  description = "Whether to enable restricted SSH (port 22) ingress on the EC2 security group. Disabled by default."
  type        = bool
  default     = false
}

variable "allowed_ssh_cidr" {
  description = "Single-host /32 IPv4 CIDR permitted for SSH when enable_ssh_ingress is true. Unrestricted 0.0.0.0/0 is prohibited."
  type        = string
  default     = "127.0.0.1/32"

  validation {
    condition     = can(cidrhost(var.allowed_ssh_cidr, 0)) && can(cidrnetmask(var.allowed_ssh_cidr)) && var.allowed_ssh_cidr != "0.0.0.0/0" && endswith(var.allowed_ssh_cidr, "/32")
    error_message = "For security, allowed_ssh_cidr must be a single-host /32 CIDR block and must never be 0.0.0.0/0."
  }
}

variable "log_retention_days" {
  description = "Number of days to retain logs in the TalentFlow CloudWatch Log Group to control storage costs."
  type        = number
  default     = 7

  validation {
    condition     = contains([1, 3, 5, 7, 14, 30], var.log_retention_days)
    error_message = "The log_retention_days value must be one of: 1, 3, 5, 7, 14, or 30."
  }
}

variable "s3_storage_warning_threshold_bytes" {
  description = "Byte threshold for the TalentFlow-Storage-Warning CloudWatch alarm (default is 1 GiB = 1073741824 bytes)."
  type        = number
  default     = 1073741824

  validation {
    condition     = var.s3_storage_warning_threshold_bytes > 0
    error_message = "The s3_storage_warning_threshold_bytes value must be greater than zero."
  }
}
