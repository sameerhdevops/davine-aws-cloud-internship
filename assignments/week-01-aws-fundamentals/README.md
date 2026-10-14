# Week 1 — AWS cloud fundamentals

## Objective and concepts

The retained Week 1 material surveys core AWS service boundaries: IAM for identity and authorization; EC2 for virtual machines; S3 for object storage; VPC for network isolation; RDS and DynamoDB for relational and key-value/document data; Lambda for event-driven compute; CloudWatch for operational telemetry; and Route 53 and CloudFront for DNS and content delivery.

The useful foundation is to start with the requirement and the responsibility boundary. A service name in a report is not itself evidence that a resource was configured. A console screenshot is a historical observation, not a current account audit.

## Recovered internship work and evidence

**Original internship artifacts:** a named Week 1 report, a task brief, and console captures associated with core AWS services were found. The report supports that these services were explored and summarized. The retained set does not provide a reproducible deployment or a cleanly attributable, public-safe Week 1 screenshot.

**Portal schedule:** Week 1 is marked Completed in the portal state reported by the user. No saved portal screenshot or export was found; the portal state is therefore reported, not independently screenshot-verified. The supplied portal history says “No weekly submissions yet,” which is separate from schedule status.

## Security, operations, and cost reasoning

- IAM identity policies and resource policies answer different authorization questions; grant the smallest action/resource set needed and verify both sides of cross-service access.
- S3 public access, encryption, lifecycle retention, and object-level access are separate controls. “Encrypted” does not mean “private.”
- Network reachability depends on routes, security groups, network ACLs, DNS, and service endpoints—not only on whether a subnet is called public or private.
- Managed services reduce some host work but introduce service-specific availability, limits, observability, and billing dimensions.

Start with the requirement and the service boundary, then verify the relevant permission, route, or metric instead of inferring runtime state from a diagram.

## Validation and limits

There is no Week 1 code in this repository to execute. Earlier portfolio records describe a report and captures, but the private originals were not reopened for this final review. No completion certificate, portal upload, reviewer approval, or current AWS state is established here. See the [evidence policy](../../docs/EVIDENCE.md) and [gallery](../../evidence/README.md) for the publication boundary.

Next: [Week 2 — EC2 and host-level security](../week-02-ec2-web-server/README.md).
