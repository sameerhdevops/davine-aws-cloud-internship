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

## Independently reconstructed follow-on

The [Week 12 Terraform baseline](../week-12-talentflow-ai/infrastructure/terraform/README.md) is new portfolio code reconstructed after the evidence review. It is separate from, and must not be described as, the missing Week 7 source submission. Its scope, security controls, non-deploying validation status, and limitations are documented alongside the code.

## Safe improvement path

With authorization, add independently authored, clearly labelled examples with version-pinned providers, variables, remote-state design, least-privilege IAM, restricted ingress, lint/validation output, and a teardown/cost-control procedure. Do not publish state files or identifiers.

## Evidence

The nine Week 7 captures and report remain private; the captures are historical and do not provide reproducible source. The [Week 12 Terraform baseline](../week-12-talentflow-ai/infrastructure/terraform/README.md) is independent follow-on code, not recovered Week 7 work. The [central evidence gallery](../../evidence/README.md) records the public evidence and validation limits.
