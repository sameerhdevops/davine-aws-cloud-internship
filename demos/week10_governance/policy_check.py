"""Narrow static checks for an example S3 object policy, not an IAM evaluator."""

from __future__ import annotations

import re
from typing import Any


ALLOWED_ACTIONS = {"s3:GetObject", "s3:PutObject"}
SUPPORTED_POLICY_FIELDS = {"Version", "Statement"}
SUPPORTED_STATEMENT_FIELDS = {"Sid", "Effect", "Action", "Resource"}
BUCKET_NAME = re.compile(r"^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$")
RESERVED_BUCKET_PREFIXES = ("xn--", "sthree-", "amzn-s3-demo-")
RESERVED_BUCKET_SUFFIXES = ("-s3alias", "--ol-s3", "--x-s3", "--table-s3", "-an")


def _nonempty_strings(value: Any) -> list[str] | None:
    """Normalize one string or a nonempty list of strings without hashing input."""
    if isinstance(value, str):
        values = [value]
    elif isinstance(value, list):
        values = value
    else:
        values = []

    if not values:
        return None
    if any(not isinstance(item, str) or not item for item in values):
        return None
    return values


def _is_supported_object_arn(resource: str) -> bool:
    """Accept only an AWS-partition object ARN with a bounded bucket name.

    This teaching subset intentionally excludes valid dotted bucket names,
    access points, directory buckets, other partitions, and IAM wildcard scope.
    Wildcards in the object-key portion are allowed because the bucket remains
    explicit; the checker does not determine the authorization effect of them.
    """
    prefix = "arn:aws:s3:::"
    if not resource.startswith(prefix):
        return False

    bucket_and_key = resource[len(prefix) :]
    bucket, separator, key = bucket_and_key.partition("/")
    if not separator or not key or not BUCKET_NAME.fullmatch(bucket):
        return False
    if bucket.startswith(RESERVED_BUCKET_PREFIXES) or bucket.endswith(RESERVED_BUCKET_SUFFIXES):
        return False
    return True


def validate_policy(policy: Any) -> list[str]:
    """Check a deliberately small, single-bucket S3 object-policy example.

    A clean result means only that this bounded example passed these static
    checks. It does not model AWS IAM evaluation or predict authorization.
    """
    if not isinstance(policy, dict):
        return ["policy must be an object"]

    errors: list[str] = []
    unknown_policy_fields = set(policy) - SUPPORTED_POLICY_FIELDS
    if unknown_policy_fields:
        errors.append(
            f"policy contains unsupported fields: {', '.join(sorted(map(str, unknown_policy_fields)))}"
        )

    if policy.get("Version") != "2012-10-17":
        errors.append('policy Version must be the supported string "2012-10-17"')

    statements = policy.get("Statement")
    if isinstance(statements, dict):
        statements = [statements]
    if not isinstance(statements, list) or not statements:
        errors.append("policy must contain one or more Statement entries")
        return errors

    for index, statement in enumerate(statements):
        if not isinstance(statement, dict):
            errors.append(f"statement {index} must be an object")
            continue

        unknown_fields = set(statement) - SUPPORTED_STATEMENT_FIELDS
        if unknown_fields:
            errors.append(
                f"statement {index} contains unsupported fields: {', '.join(sorted(map(str, unknown_fields)))}"
            )

        if "Effect" not in statement or statement.get("Effect") != "Allow":
            errors.append(f"statement {index} must use Effect Allow")

        if "Sid" in statement and (not isinstance(statement["Sid"], str) or not statement["Sid"]):
            errors.append(f"statement {index} Sid must be a nonempty string")

        actions = _nonempty_strings(statement.get("Action"))
        if actions is None:
            errors.append(
                f"statement {index} Action must be a nonempty string or list of nonempty strings"
            )
        elif any(action not in ALLOWED_ACTIONS for action in actions):
            errors.append(f"statement {index} contains an action outside the example allow-list")

        resources = _nonempty_strings(statement.get("Resource"))
        if resources is None:
            errors.append(
                f"statement {index} Resource must be a nonempty string or list of nonempty strings"
            )
        elif any(not _is_supported_object_arn(resource) for resource in resources):
            errors.append(
                f"statement {index} must target named-bucket S3 object ARNs in the supported subset"
            )

    return errors
