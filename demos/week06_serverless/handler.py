"""Parse S3-shaped event records locally; this is not an AWS Lambda deployment."""

from __future__ import annotations

from urllib.parse import unquote_plus
from typing import Any


def handle(event: dict[str, Any], context: object | None = None) -> list[dict[str, str]]:
    del context  # The local demonstration does not use the Lambda runtime context.
    records = event.get("Records")
    if not isinstance(records, list):
        raise ValueError("event must contain a Records list")
    parsed: list[dict[str, str]] = []
    for index, record in enumerate(records):
        try:
            bucket = record["s3"]["bucket"]["name"]
            key = record["s3"]["object"]["key"]
        except (KeyError, TypeError) as exc:
            raise ValueError(f"record {index} is missing S3 bucket or object data") from exc
        if not isinstance(bucket, str) or not isinstance(key, str):
            raise ValueError(f"record {index} bucket and key must be strings")
        parsed.append({"bucket": bucket, "key": unquote_plus(key)})
    return parsed
