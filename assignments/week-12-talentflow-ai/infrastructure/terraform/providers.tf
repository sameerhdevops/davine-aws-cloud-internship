# =============================================================================
# TalentFlow AI — AWS Provider Configuration
# Security Note: No credentials or account IDs are hardcoded here.
# Authentication relies on the standard AWS credential provider chain
# (e.g., AWS CLI profile or environment variables).
# =============================================================================

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
      Portfolio   = "Davine-Technologies-AWS-Internship"
      Provenance  = "Reconstructed-IaC"
    }
  }
}
