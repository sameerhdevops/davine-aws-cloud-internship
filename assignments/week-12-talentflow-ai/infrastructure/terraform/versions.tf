# =============================================================================
# TalentFlow AI — Terraform Version and Provider Constraints
# Provenance: Newly reconstructed Infrastructure as Code for portfolio use.
# =============================================================================

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 6.0"
    }
  }
}
