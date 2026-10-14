# Validation record index

This index points to checks that actually ran. Each record applies only to its stated commit, environment, command, and scope. A passing static check is not an AWS plan or deployment.

## Published `main` before this review

[Portfolio quality run 38516010770](https://github.com/sameerhdevops/github-portfolio/actions/runs/38516010770) completed successfully for the published `main` commit on 2026-10-14. Both the Markdown-link and Terraform jobs passed. The recorded workflow did not pin the Python minor version; this review adds an explicit Python 3.11 setup to future runs. No plan or deployment step was run. See the [commit-scoped run record](terraform/github-actions-main-2026-10-14.md).

## Final-polish local review

The [local validation record](final-polish-local-2026-10-14.md) applies to source commit `b8511cbe428a2f9b2541fa97b3973e73f1789f35`. Python, Ruff, Markdown, portfolio, and Terraform formatting/backend-free initialization checks passed. Windows `terraform validate` failed before schema validation because the provider process did not answer; this matches the baseline environment failure. The record separates local results from the current branch's hosted checks.

## Pull request validation

The initial PR run [38531004190](https://github.com/sameerhdevops/github-portfolio/actions/runs/38531004190) passed both jobs for commit `27e437238c17b56acb7b48e4da3394b83e4fb3ed`. Its exact scope is recorded in [the PR validation record](github-actions-pr-3-2026-10-14.md). The commit adding that record must be evaluated by its own PR run.

## Earlier local and hosted records

| Record | Scope |
| --- | --- |
| [Local demonstration tests](local-demo-tests-2026-10-14.md) | Historical baseline before the final-review branch; 11 tests on Windows/Python 3.14.7. |
| [Final-review local checks](final-review-2026-10-14.md) | Review checks against source commit `19080df`; 35 tests and repository checks passed, while Windows Terraform schema validation was blocked by the provider process. |
| [Windows Terraform validation](terraform/local-validation-2026-10-14.md) | Formatting and backend-free initialization passed; provider schema process failed before validation. |
| [Published main Terraform validation](terraform/github-actions-main-2026-10-13.md) | Earlier hosted run for its recorded commit; formatting, initialization, and validation succeeded. |
| [Earlier release-branch run](terraform/github-actions-release-2026-10-14.md) | Hosted validation for the exact branch commit in that record; it predates this review branch. |

The final-review record separates local results from the pull request's hosted checks. Its 35 passing Python tests are not an AWS service-conformance result; its Windows Terraform failure is not a configuration validation pass.

The pull request's latest hosted checks are surfaced on its Checks tab. Each check applies only to the exact commit listed with that result.
