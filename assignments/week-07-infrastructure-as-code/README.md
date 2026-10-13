# Week 7 — Infrastructure as Code

## Evidence status

**Partially present.** A dated Week 7 technical report (4 September 2026) and nine recovered submission captures are retained privately. They establish the topic and show historical Terraform/CloudFormation activity, but raw `.tf` and template files were not retained.

## Purpose and learning scope

The report explains declarative provisioning, Terraform state and `init` → `plan` → `apply`, CloudFormation stacks, AWS CLI inspection, and resource tagging. The supplied weekly framework places Terraform state management on Wednesday and configuration/workflow practice on Friday.

## Evidence-backed observations

- The report compares Terraform’s HCL and explicit state with AWS-native CloudFormation templates and stack-managed state.
- Captures show a Terraform configuration/plan/apply workflow, a CloudFormation template view, and EC2 resource tags.
- The report gives example tags for a development environment and a Terraform-managed resource.

## Validation boundary

Terminal and console captures are historical observations only. They do not supply provider versions, module layout, state, a sanitized plan, or a reproducible deployment. This repository intentionally contains no reconstructed IaC presented as recovered internship work.

## Safe improvement path

With authorization, add independently authored, clearly labelled examples with version-pinned providers, variables, remote-state design, least-privilege IAM, restricted ingress, lint/validation output, and a teardown/cost-control procedure. Do not publish state files or identifiers.
