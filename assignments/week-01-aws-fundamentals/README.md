# Week 1 — AWS cloud fundamentals

## Objective

Introduce the main AWS service boundaries and the habit of connecting a requirement to the service, permission, network path, and operational signal that supports it.

## What I did or implemented

Retained Week 1 material surveys IAM, EC2, S3, VPC, RDS, DynamoDB, Lambda, CloudWatch, Route 53, and CloudFront. The available portal information marks Week 1 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained here.

## Key concepts

- IAM identity and resource policies answer different authorization questions. Grant only the required actions on the required resources, then verify both sides of cross-service access.
- S3 public-access controls, encryption, lifecycle retention, and object permissions are distinct. Encryption alone does not make a bucket private.
- Network reachability depends on routes, security groups, network ACLs, DNS, and service endpoints; a subnet label is not enough to establish connectivity.
- Managed services reduce some host-management work while introducing service-specific limits, availability behavior, observability, and billing dimensions.

Start with the requirement and responsibility boundary. A service name in a report does not establish that a resource was configured, and a historical console image does not establish current account state.

## Evidence and links

The existing portfolio record describes a Week 1 report, task brief, and service-console captures. The report supports documented exploration; its source files have not been independently inspected. See the [evidence policy](../../docs/EVIDENCE.md) and [gallery](../../evidence/README.md).

## Limitations

No Week 1 code is available to run, and no focused public screenshot is included. The retained descriptions do not establish a reproducible deployment, portal upload, acceptance, reviewer approval, completion certificate, or current AWS state.

## Next improvements

Build a small local request-flow map that follows one example workload through identity, network, storage, and monitoring boundaries, then record which claims are design assumptions and which can be checked locally.
