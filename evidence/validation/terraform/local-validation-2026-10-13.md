# Local Terraform validation record

Date: 2026-10-13

Platform: Windows, `windows_amd64`

Terraform: v1.16.5

AWS provider selected by the lock file: `hashicorp/aws` v5.100.0

These are non-deploying checks against the reconstructed Week 12 Terraform source. The commands supplied no AWS credentials and were limited to formatting, backend-free initialization, and validation. No plan, apply, destroy, or AWS resource operation was run.

## `terraform version`

```text
Terraform v1.16.5
on windows_amd64
+ provider registry.terraform.io/hashicorp/aws v5.100.0
```

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

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

## `terraform validate -no-color`

Exit code: `1`. The provider plugin did not return its schema to Terraform, so this run did **not** validate the configuration.

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

This is a local provider-process/schema handshake failure. It is not evidence that the Terraform source is valid or invalid. The repository's Ubuntu CI workflow performs an independent non-deploying validation; its actual result must be checked in GitHub Actions. Do not treat `fmt` or `init` as a substitute for `validate`.
