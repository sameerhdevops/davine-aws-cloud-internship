# Week 7 - Infrastructure as code

## Evidence status

**Strongly supported probable assignment.** A terminal capture labels a CloudFormation template as Week 7. Related terminal captures display Terraform configuration and an interactive apply result.

## Objective

Practice expressing infrastructure declaratively and inspect the difference between an infrastructure definition, a plan, and observed resource state.

## What was observed

- Terraform configuration was displayed in a terminal, including a security-group and EC2 resource definition.
- An interactive Terraform execution screen reported a completed change.
- A CloudFormation template screen described an S3 bucket for a Week 7 activity.
- A console capture displayed EC2 instances associated with Terraform-related tags.

## Accuracy boundary

The source files themselves are not present in this portfolio. A Terraform plan is not proof of deployment, and displayed terminal output is historical capture-time evidence only. This section deliberately does not provide deployment commands or claim a reproducible environment.

## Improvement path

To make this project reproducible, retain sanitized `main.tf`, `variables.tf`, provider constraints, a README, a redacted plan, and a teardown record. Use non-public SSH rules and remove resource identifiers before publication.
