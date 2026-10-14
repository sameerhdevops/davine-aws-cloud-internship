"""Narrow static checks for an example policy; this is not the AWS IAM simulator."""

from __future__ import annotations

from typing import Any


ALLOWED_ACTIONS = {"s3:GetObject", "s3:PutObject"}


def validate_policy(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    statements = policy.get("Statement")
    if isinstance(statements, dict):
        statements = [statements]
    if not isinstance(statements, list) or not statements:
        return ["policy must contain one or more Statement entries"]
    for index, statement in enumerate(statements):
        if not isinstance(statement, dict):
            errors.append(f"statement {index} must be an object")
            continue
        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])
        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]
        if statement.get("Effect") != "Allow":
            errors.append(f"statement {index} must use Effect Allow")
        if not isinstance(actions, list) or not actions or any(a not in ALLOWED_ACTIONS for a in actions):
            errors.append(f"statement {index} contains an action outside the example allow-list")
        if not isinstance(resources, list) or not resources or any(
            not isinstance(resource, str) or not resource.startswith("arn:aws:s3:::") or resource == "*"
            for resource in resources
        ):
            errors.append(f"statement {index} must target a named S3 bucket or object ARN")
        if any(isinstance(resource, str) and resource.endswith("/*") and ":s3:::*" in resource for resource in resources):
            errors.append(f"statement {index} must not target every S3 bucket")
    return errors
