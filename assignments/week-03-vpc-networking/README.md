# Week 3 — VPC networking

## Objective and evidence boundary

The supplied 12-week framework associates this week with IPv4 CIDR planning, public/private subnet boundaries, route tables, Internet Gateway paths, security groups, and network ACLs. **No Week 3 brief, report, submission, screenshot, or source configuration was recovered.** The portal marks Week 3 Completed as reported by the user, but that schedule state does not establish a retained assignment submission. No saved portal screenshot/export is available.

## Independent reconstruction: route and CIDR plan

[`network-plan.json`](../../demos/week03_vpc/network-plan.json) defines a sample `10.20.0.0/16` VPC with two public and two isolated private `/24` subnets across two illustrative AZ labels. [`validate.py`](../../demos/week03_vpc/validate.py) checks CIDR containment, subnet overlap, presence of VPC-local routes, and whether direct Internet Gateway routes match the declared exposure. This is a **reproducible demonstration**, not recovered internship work or an AWS deployment.

```powershell
python demos/week03_vpc/validate.py
python -m unittest discover -s tests -v
```

The example gives public subnets a default route through an Internet Gateway and leaves private subnets with only the VPC-local route. A workload that needs package updates or AWS APIs would need a deliberate egress path, such as a reviewed NAT or service endpoint design; a security-group egress permission alone does not create a route.

## Security and operations

Security groups are stateful filters attached to network interfaces; network ACLs are stateless subnet-level filters. Routes determine where a packet can go, while those controls determine whether it can pass. A public route does not itself assign a public address. Production CIDR and AZ choices must account for existing networks, growth, service quotas, and failover needs.

“I would verify address containment and overlap first, trace the route table associated with the subnet, then check both security-group directions and stateless NACL return traffic. I would not label a subnet public solely from its name.”

## Validation and limitations

The standard-library validator and tests run locally and call no AWS API. They do not model route propagation, NAT, endpoint policies, NACL behavior, DNS, or AWS service semantics. No original Week 3 configuration or completion claim is made. See [independent demos](../../demos/README.md) and the [evidence gallery](../../evidence/README.md).

Next: [Week 4 — Application Load Balancing](../week-04-application-load-balancing/README.md).
