# Local Terraform validation record

Date: 2026-10-14

Platform: Windows, `windows_amd64`

Terraform: v1.16.5

AWS provider selected by the committed lock file: `hashicorp/aws` v5.100.0

These non-deploying checks inspected the independent Week 12 Terraform baseline. No AWS credentials were configured or sought. The run did not execute a plan, apply, destroy, AWS CLI operation, or resource deployment.

## `terraform fmt -check`

Exit code: `0`

```text
(no stdout/stderr)
```

## `terraform init -backend=false -input=false -no-color`

Exit code: `0`

```text
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v5.100.0

Terraform has been successfully initialized!
```

This did not configure a remote backend. The provider was already present in the local Terraform working directory.

## `terraform validate -no-color`

Exit code: `1`. The provider plugin did not return its schema, so this local run did **not** validate the configuration.

```text
Error: Failed to load plugin schemas

Error while loading schemas for plugin components: Failed to obtain provider
schema: Could not load the schema for provider
registry.terraform.io/hashicorp/aws: failed to retrieve schema from provider
"registry.terraform.io/hashicorp/aws": Plugin did not respond: The plugin
encountered an error, and failed to respond to the
plugin.(*GRPCProvider).GetProviderSchema call. The plugin logs may contain
more details...
```

This is an environment/provider-process limitation, not evidence that the HCL is valid or invalid. The separate Ubuntu GitHub Actions workflow is the independent schema-validation result; it is recorded with its exact run and commit. Formatting and initialization are not substitutes for `validate`.

No workaround attempted to obtain credentials or deploy infrastructure. No Terraform plan was generated.
