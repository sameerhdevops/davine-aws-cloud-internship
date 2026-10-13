# Evidence and validation

The [central evidence gallery](../evidence/README.md) is the index for the public-safe screenshot derivatives and reproducible validation records. Each item states what it supports and what it cannot establish. The [manifest](../evidence/manifest.csv) contains the same records in a machine-readable form.

## Evidence levels

| Level | Meaning used here |
| --- | --- |
| Directly observed | A report page or screenshot visibly shows the stated screen, configuration field, output, or diagram. |
| Documented claim | A report describes a component or workflow. It is not independently verified by source code. |
| Independent portfolio work | Documentation, diagrams, code, or checks authored for this portfolio after the internship evidence review. |
| Inference | A cautious grouping based on labels and closely related evidence. |
| Unknown | The available materials do not establish the fact. |

## Publication boundary

- Two Week 10 screenshot derivatives are public after cropping and visual review. Their original source images remain private and unchanged. The images are dated only as unknown historical captures; neither establishes current AWS state.
- Other original screenshots, reports, and archives are not included. They can expose account/resource identifiers, endpoints, personal context, or financial details, and employer/third-party redistribution permission is not established for the original documents.
- The TalentFlow AI upstream repository is linked, not copied. Its inspected root had no visible licence.
- The Week 12 Terraform baseline is independently reconstructed source. It is not a recovered internship file and is not deployed.

## Validation status

The local Windows record is in [`evidence/validation/terraform/`](../evidence/validation/terraform/local-validation-2026-10-13.md): `terraform fmt -check` and `terraform init -backend=false` passed; a fresh `terraform validate` attempt did not obtain the AWS provider schema because the provider plugin failed to respond. That is an incomplete local validation result, not a pass. The [GitHub Actions run](https://github.com/sameerhdevops/github-portfolio/actions/runs/38402304332) succeeded for commit `cb3653c345e0d7f8284ae910d92b10ece35d885d`; hosted Markdown-link checking, formatting, backend-free initialization, and Terraform validation all passed. The [hosted output record](../evidence/validation/terraform/github-actions-2026-10-13.md) preserves the run identity and scope.

The GitHub Actions workflow runs `terraform fmt -check`, `terraform init -backend=false`, and `terraform validate` on Ubuntu, without AWS credentials, a plan, or a deployment. It also checks repository-relative Markdown links. The linked run passed; it is static/schema validation, not a plan or proof of deployment.

Terraform validation checks source consistency against installed provider schemas. It does not produce an execution plan or prove AWS deployment. Historical screenshots and report claims also do not prove current cloud configuration.
