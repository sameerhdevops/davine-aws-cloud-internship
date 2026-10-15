# Week 1 — AWS cloud fundamentals

## Objective

I wanted to understand how common AWS services divide responsibility across identity, compute, storage, networking, data, and operations.

## What I did or implemented

The portfolio’s Week 1 notes describe a report and task brief covering IAM, EC2, S3, VPC, RDS, DynamoDB, Lambda, CloudWatch, Route 53, and CloudFront. No Week 1 code or focused screenshot is published, so this page summarizes topics recorded for the week rather than a reproducible deployment.

## Key concepts

- **Service boundaries:** Choose a service by its role in the workload, then identify which responsibilities remain with the operator.
- **Identity and access:** IAM identity policies and resource policies answer different authorization questions; both sides matter when services interact.
- **Operational context:** Network paths, monitoring, availability behavior, and billing affect whether a design works beyond the service diagram.

## Evidence and links

See the shared [evidence guide](../../docs/evidence-and-validation.md) and [evidence gallery](../../evidence/README.md) for how to read portfolio notes and public images.

## Limitations

The repository contains no Week 1 code or focused image; descriptions of the report and task brief have not been checked against the private source files. These notes do not establish a reproducible deployment or an accepted assignment.

## Next improvements

A small local request-flow map could follow one example workload through identity, network, storage, and monitoring boundaries.
