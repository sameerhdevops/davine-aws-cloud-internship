# Week 3 — VPC networking

## Objective

Reason about IPv4 address planning, subnet boundaries, route tables, Internet Gateway paths, security groups, and network ACLs.

## What I did or implemented

No Week 3 brief, report, submission, screenshot, or source configuration is retained in the repository. The available portal information marks Week 3 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is available.

The added [network plan](../../demos/week03_vpc/network-plan.json) describes a sample 10.20.0.0/16 VPC with two public and two isolated private /24 subnets across illustrative Availability Zone labels. The [validator](../../demos/week03_vpc/validate.py) checks address containment, subnet overlap, VPC-local routes, and consistency between route labels and declared exposure.

## Key concepts

The example gives public subnets a default route through an Internet Gateway and leaves private subnets with only the VPC-local route. A private workload that needs package updates or AWS APIs requires an intentionally designed egress path, such as NAT or service endpoints; a security-group egress rule does not create a route.

Security groups are stateful filters on network interfaces; network ACLs are stateless subnet-level filters. Routes determine where a packet can go, while those controls determine whether it can pass. A public route does not itself assign a public address. Real CIDR and AZ choices must account for connected networks, growth, quotas, and failure domains.

## Evidence and links

Run from the repository root:

    python demos/week03_vpc/validate.py
    python -m unittest discover -s tests -v

The validator uses the standard library and makes no AWS API calls. See the [demonstration catalog](../../demos/README.md) and [evidence gallery](../../evidence/README.md).

## Limitations

This is a reproducible demonstration, not recovered internship work or an AWS deployment. It does not model route propagation, NAT, endpoint policies, NACL behavior, DNS, or AWS service semantics. No original Week 3 configuration or assignment submission is established.

## Next improvements

An extension could model endpoint-route associations or a small NACL rule set, with explicit tests for return traffic and route reachability; neither behavior is covered by the current validator.
