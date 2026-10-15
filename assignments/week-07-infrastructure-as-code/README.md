# Week 7 — Infrastructure as Code

## Objective

I wanted to understand how infrastructure changes are declared, reviewed, applied, and checked, while keeping state, credentials, access, and cleanup in view.

## What I did or implemented

The portfolio’s September 4 report notes discuss Terraform and CloudFormation. A published CloudShell crop shows an “Apply complete” message for one added resource, followed by a query returning a running `t3.micro`; it is not a validation result for the Week 12 Terraform project. The [original Week 7 templates are not in this repository](../../docs/portfolio-map.md), so that run cannot be reproduced here. A separate launch-form capture displayed SSH from `0.0.0.0/0` and an AWS warning, but the available record does not connect that form to the instance in the apply capture.

## Key concepts

- **Apply versus health:** An apply summary reports Terraform’s requested changes, but does not establish application health, safe IAM, secure ingress, or cleanup.
- **State and secrets:** Review plans and state handling, and keep state, credentials, and real variable files out of public version control.
- **Post-change review:** After an authorized deployment, verify resource health and exposure; the separate Week 12 portfolio configuration is limited to static checks and has not been applied.

## Evidence and links

![CloudShell crop showing one resource added and a later query returning a running t3.micro; instance and query identifiers are redacted.](../../evidence/assets/week-07-terraform/week-07-terraform-apply-observed.png)

*The crop records a reported Week 7 run; it does not show validation or deployment of the separate Week 12 Terraform baseline.* See the [gallery entry](../../evidence/README.md#week-7-infrastructure-as-code).

## Limitations

The source templates, state, and full resource scope for the described run are unavailable in the repository. The screenshot does not establish current state, state safety, or that the open-SSH form was applied to the instance.

## Next improvements

If the source becomes available and can be shared safely, review its plan, state workflow, identity scope, ingress, and cleanup before attempting reproduction.
