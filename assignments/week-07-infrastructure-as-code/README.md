# Week 7 — Infrastructure as Code

## Objective

Understand how infrastructure changes are declared, reviewed, applied, and checked after creation, while keeping source, state, credentials, and cleanup in scope.

## What I did or implemented

The retained September 4 report and screenshots discuss Terraform and CloudFormation. One historical CloudShell crop displays “Apply complete! Resources: 1 added, 0 changed, 0 destroyed” followed by an EC2 query returning a t3.micro in running state. The available portal information marks Week 7 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

The original Week 7 Terraform/YAML source is not present. The Week 12 Terraform project is a separate reconstruction and is documented on its own page.

## Key concepts

A successful apply reports that Terraform completed requested changes; it does not independently establish application health, secure IAM, safe ingress, or cleanup. Review the plan and state handling, then verify resource health and exposure after an apply. Never commit Terraform state, credentials, or real variable files.

A separate historical launch-form capture displayed SSH ingress from 0.0.0.0/0 and AWS’s all-addresses warning. It does not establish that this rule was applied to the instance shown in the apply capture. The configuration is withheld from the public gallery; the security lesson is to use managed access or tightly scoped temporary ingress.

## Evidence and links

![Historical CloudShell output showing one Terraform resource added and a subsequent query returning a running t3.micro; instance and query identifiers are redacted.](../../evidence/assets/week-07-terraform/week-07-terraform-apply-observed.png)

*Sanitized derivative described in the existing portfolio record as a Week 7 capture dated 2026-09-04. It is not validation or deployment evidence for the Week 12 reconstruction.* See the [gallery entry](../../evidence/README.md#week-7-infrastructure-as-code) and [portfolio provenance map](../../docs/portfolio-map.md).

## Limitations

The historical apply cannot be reproduced from the files in this repository; the source templates, state, and full resource scope are unavailable. The screenshot does not establish current state, state safety, or that the open-SSH form was applied to the created instance.

## Next improvements

If the original source becomes available and can be safely shared, review its plan, state workflow, identity scope, ingress, and cleanup before attempting any reproduction. The existing Week 12 reconstruction remains a separate static-validation-only project.
