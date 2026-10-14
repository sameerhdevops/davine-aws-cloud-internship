"""Validate a small illustrative subnet and route plan; this does not call AWS."""

from __future__ import annotations

import json
import sys
from ipaddress import ip_network
from pathlib import Path
from typing import Any


def validate_plan(plan: Any) -> list[str]:
    if not isinstance(plan, dict):
        return ["plan must be an object"]

    errors: list[str] = []
    cidr = plan.get("vpc_cidr")
    if not isinstance(cidr, str):
        return ["invalid vpc_cidr: expected an IPv4 CIDR string"]
    try:
        vpc = ip_network(cidr, strict=True)
    except ValueError as exc:
        return [f"invalid vpc_cidr: {exc}"]
    if vpc.version != 4:
        return ["invalid vpc_cidr: this example supports IPv4 only"]

    subnets = plan.get("subnets")
    if not isinstance(subnets, list):
        return ["subnets must be a list"]
    if not subnets:
        return ["plan must contain at least one subnet"]

    networks = []
    names: set[str] = set()
    for index, subnet in enumerate(subnets):
        if not isinstance(subnet, dict):
            errors.append(f"subnet {index} must be an object")
            continue

        name = subnet.get("name", f"subnet-{index}")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"subnet {index} name must be a nonempty string")
            continue
        if name in names:
            errors.append(f"duplicate subnet name: {name}")
        names.add(name)

        subnet_cidr = subnet.get("cidr")
        if not isinstance(subnet_cidr, str):
            errors.append(f"{name}: invalid CIDR: expected a string")
            continue
        try:
            network = ip_network(subnet_cidr, strict=True)
        except ValueError as exc:
            errors.append(f"{name}: invalid CIDR: {exc}")
            continue
        if network.version != 4 or not network.subnet_of(vpc):
            errors.append(f"{name}: {network} is not contained by {vpc}")
        for previous_name, previous_network in networks:
            if network.overlaps(previous_network):
                errors.append(f"{name}: {network} overlaps {previous_name} ({previous_network})")
        networks.append((name, network))

        if "az" in subnet and (not isinstance(subnet["az"], str) or not subnet["az"].strip()):
            errors.append(f"{name}: az must be a nonempty string when provided")

        exposure = subnet.get("exposure")
        if not isinstance(exposure, str) or exposure not in {"public", "private"}:
            errors.append(f"{name}: exposure must be public or private")

        routes = subnet.get("routes")
        if not isinstance(routes, list) or any(not isinstance(route, str) or not route for route in routes):
            errors.append(f"{name}: routes must be a list of nonempty strings")
            continue
        if len(routes) != len(set(routes)):
            errors.append(f"{name}: route labels must not be duplicated")
        unsupported_routes = set(routes) - {"local", "internet-gateway"}
        if unsupported_routes:
            errors.append(f"{name}: unsupported illustrative route label(s): {', '.join(sorted(unsupported_routes))}")
        route_set = set(routes)
        if "local" not in route_set:
            errors.append(f"{name}: route set must include the VPC-local route")
        if exposure == "public" and "internet-gateway" not in route_set:
            errors.append(f"{name}: public subnet is missing its Internet Gateway route")
        if exposure == "private" and "internet-gateway" in route_set:
            errors.append(f"{name}: private subnet must not route directly to the Internet Gateway")
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
