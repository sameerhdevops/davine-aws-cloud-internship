# Week 3 — VPC networking

## Objective

I wanted to reason about IPv4 address planning, subnet boundaries, route tables, Internet Gateway paths, and traffic filters.

## What I did or implemented

No week-specific source file or screenshot is published for Week 3. The local [network plan](../../demos/week03_vpc/network-plan.json) describes a sample `10.20.0.0/16` VPC with two public and two isolated private `/24` subnets across illustrative Availability Zone labels. The [validator](../../demos/week03_vpc/validate.py) checks address containment, overlap, VPC-local routes, and whether route labels match the declared exposure.

## Key concepts

- **Routes and exposure:** A public subnet’s default route points to an Internet Gateway, but a route alone does not assign a public address.
- **Private egress:** A private workload needing package updates or AWS APIs requires a deliberate path, such as NAT or a service endpoint; a security-group egress rule does not create that route.
- **Traffic controls:** Security groups are stateful and attached to network interfaces; network ACLs are stateless subnet controls. Routes and filters solve different parts of reachability.

## Evidence and links

Run `python demos/week03_vpc/validate.py` and `python -m unittest discover -s tests -v` from the repository root. The [demonstration catalog](../../demos/README.md) describes the sample.

## Limitations

This is a reproducible demonstration, not recovered internship work or an AWS deployment. It does not model route propagation, NAT, endpoint policies, NACL behavior, DNS, or AWS service semantics. No original Week 3 configuration or submission is established by repository files.

## Next improvements

An extension could model endpoint-route associations or a small NACL rule set, with tests for return traffic and route reachability.
