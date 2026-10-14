# Validation record index

This index points to checks that actually ran. Each record applies only to its stated commit, environment, command, and scope. A passing static check is not an AWS plan or deployment.

## Published `main` before this review

[Portfolio quality run 38516010770](https://github.com/sameerhdevops/github-portfolio/actions/runs/38516010770) completed successfully for the published `main` commit on 2026-10-14. Both the Markdown-link and Terraform jobs passed. The recorded workflow did not pin the Python minor version; this review adds an explicit Python 3.11 setup to future runs. No plan or deployment step was run. See the [commit-scoped run record](terraform/github-actions-main-2026-10-14.md).

## Earlier local and hosted records

| Record | Scope |
| --- | --- |
| [Local demonstration tests](local-demo-tests-2026-10-14.md) | Historical baseline before the final-review branch; 11 tests on Windows/Python 3.14.7. |
| [Windows Terraform validation](terraform/local-validation-2026-10-14.md) | Formatting and backend-free initialization passed; provider schema process failed before validation. |
| [Published main Terraform validation](terraform/github-actions-main-2026-10-13.md) | Earlier hosted run for its recorded commit; formatting, initialization, and validation succeeded. |
| [Earlier release-branch run](terraform/github-actions-release-2026-10-14.md) | Hosted validation for the exact branch commit in that record; it predates this review branch. |

The final local checks for this review will be recorded only after they run, with the exact tested commit and any Windows Terraform limitation. The pull request's hosted checks will remain the relevant validation of its exact pushed commit.

The current pull request’s checks, if created, are the relevant hosted result for this change set and appear in the pull-request Checks tab.
