"""Command-line interface for the read-only AWS posture audit."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from .audit import build_report, report_exit_code


def _csv_rows(report: dict[str, Any]) -> list[dict[str, str]]:
    rows = []
    for finding in report["findings"]:
        rows.append(
            {
                "check_id": finding["check_id"],
                "resource_type": finding["resource_type"],
                "resource_id": finding["resource_id"],
                "region": finding["region"],
                "status": finding["status"],
                "summary": finding["summary"],
                "details_json": json.dumps(finding["details"], sort_keys=True),
            }
        )
    return rows


def _write_json(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")


def _write_csv(path: Path, report: dict[str, Any]) -> None:
    fieldnames = [
        "check_id",
        "resource_type",
        "resource_id",
        "region",
        "status",
        "summary",
        "details_json",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(_csv_rows(report))


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect a read-only snapshot of selected AWS security and tagging settings."
    )
    parser.add_argument(
        "--region", required=True, help="AWS Region to audit for EC2 instances and security groups"
    )
    parser.add_argument("--profile", help="Optional AWS shared-config profile name")
    parser.add_argument(
        "--required-tags",
        default="Owner,Environment,Project",
        help="Comma-separated required tag keys (default: Owner,Environment,Project)",
    )
    parser.add_argument(
        "--json-output", type=Path, help="Write the complete report to this JSON file"
    )
    parser.add_argument("--csv-output", type=Path, help="Write finding rows to this CSV file")
    parser.add_argument(
        "--acknowledge-sensitive-output",
        action="store_true",
        help="Required when writing a report file because it can contain resource names and IDs",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = make_parser()
    args = parser.parse_args(argv)
    if (args.json_output or args.csv_output) and not args.acknowledge_sensitive_output:
        parser.error(
            "report files can contain resource names and IDs; pass --acknowledge-sensitive-output"
        )
    required_tags = tuple(key.strip() for key in args.required_tags.split(",") if key.strip())
    if not required_tags:
        parser.error("--required-tags must contain at least one nonempty tag key")
    if len(set(required_tags)) != len(required_tags):
        parser.error("--required-tags must not contain duplicate keys")
    output_paths = [path.resolve() for path in (args.json_output, args.csv_output) if path]
    if len(set(output_paths)) != len(output_paths):
        parser.error("JSON and CSV output paths must be different")
    existing = [str(path) for path in output_paths if path.exists()]
    if existing:
        print(
            f"Refusing to overwrite existing report file(s): {', '.join(existing)}", file=sys.stderr
        )
        return 2

    try:
        session = boto3.Session(profile_name=args.profile, region_name=args.region)
        report = build_report(session, region=args.region, required_tags=required_tags)
    except (BotoCoreError, ClientError) as error:
        print(f"Could not start AWS audit: {type(error).__name__}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"Could not write report: {error}", file=sys.stderr)
        return 2

    try:
        if args.json_output:
            _write_json(args.json_output, report)
        if args.csv_output:
            _write_csv(args.csv_output, report)
    except OSError as error:
        print(f"Could not write report file: {error}", file=sys.stderr)
        return 2

    summary = report["summary"]
    print(
        "AWS audit completed without changing resources: "
        f"{summary.get('PASS', 0)} pass, {summary.get('FINDING', 0)} finding, "
        f"{summary.get('UNKNOWN', 0)} unknown, {summary.get('NOT_CONFIGURED', 0)} not configured."
    )
    for path in (args.json_output, args.csv_output):
        if path:
            print(f"Report written to {path}")
    return report_exit_code(report)


if __name__ == "__main__":
    raise SystemExit(main())
