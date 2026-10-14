"""Validate a small illustrative subnet and route plan; this does not call AWS."""

from __future__ import annotations

import json
import sys
from ipaddress import ip_network
from pathlib import Path
from typing import Any


def validate_plan(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        vpc = ip_network(plan["vpc_cidr"], strict=True)
    except (KeyError, ValueError, TypeError) as exc:
        return [f"invalid vpc_cidr: {exc}"]

    networks = []
    names: set[str] = set()
    for index, subnet in enumerate(plan.get("subnets", [])):
        name = str(subnet.get("name", f"subnet-{index}"))
        if name in names:
            errors.append(f"duplicate subnet name: {name}")
        names.add(name)
        try:
            network = ip_network(subnet["cidr"], strict=True)
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f"{name}: invalid CIDR: {exc}")
            continue
        if network.version != vpc.version or not network.subnet_of(vpc):
            errors.append(f"{name}: {network} is not contained by {vpc}")
        for previous_name, previous_network in networks:
            if network.overlaps(previous_network):
                errors.append(f"{name}: {network} overlaps {previous_name} ({previous_network})")
        networks.append((name, network))

        exposure = subnet.get("exposure")
        routes = set(subnet.get("routes", []))
        if "local" not in routes:
            errors.append(f"{name}: route set must include the VPC-local route")
        if exposure == "public" and "internet-gateway" not in routes:
            errors.append(f"{name}: public subnet is missing its Internet Gateway route")
        if exposure == "private" and "internet-gateway" in routes:
            errors.append(f"{name}: private subnet must not route directly to the Internet Gateway")
        if exposure not in {"public", "private"}:
            errors.append(f"{name}: exposure must be public or private")

    if not plan.get("subnets"):
        errors.append("plan must contain at least one subnet")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("network-plan.json")
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Could not read plan: {exc}", file=sys.stderr)
        return 2
    errors = validate_plan(plan)
    if errors:
        print("Illustrative VPC plan has issues:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Illustrative plan is internally consistent: {len(plan['subnets'])} subnets within {plan['vpc_cidr']}. No AWS API was called.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
