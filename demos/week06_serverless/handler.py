"""Parse S3-shaped event records locally; this is not an AWS Lambda deployment."""

from __future__ import annotations

from urllib.parse import unquote_plus
from typing import Any


def handle(event: Any, context: object | None = None) -> list[dict[str, str]]:
    del context  # The local demonstration does not use the Lambda runtime context.
    if not isinstance(event, dict):
        raise ValueError("event must be an object")
    records = event.get("Records")
    if not isinstance(records, list):
        raise ValueError("event must contain a Records list")
    parsed: list[dict[str, str]] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"record {index} must be an object")
        s3 = record.get("s3")
        if not isinstance(s3, dict):
            raise ValueError(f"record {index} must contain S3 event data as an object")
        bucket_data = s3.get("bucket")
        object_data = s3.get("object")
        if not isinstance(bucket_data, dict) or not isinstance(object_data, dict):
            raise ValueError(f"record {index} bucket and object data must be objects")
        bucket = bucket_data.get("name")
        key = object_data.get("key")
        if not isinstance(bucket, str) or not bucket:
            raise ValueError(f"record {index} bucket name must be a nonempty string")
        if not isinstance(key, str) or not key:
            raise ValueError(f"record {index} object key must be a nonempty string")
        parsed.append({"bucket": bucket, "key": unquote_plus(key)})
    return parsed
