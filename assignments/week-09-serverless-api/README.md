# Week 9 - Serverless API workflow

## Evidence status

**Verified complete.** Multiple activity-submission versions, a final architecture diagram, and named API/Lambda/ALB/Auto Scaling/DynamoDB captures are retained privately.

## Documented architecture

![Original Week 9 architecture diagram](../../diagrams/week-09-serverless-api.svg)

The evidence depicts an API-facing workflow involving an Application Load Balancer, Auto Scaling/EC2 tier, Step Functions, Lambda, RDS, and DynamoDB. The diagram labels the data layer as verified resources but does not assert an end-to-end application-to-database call.

## Validation evidence

- A Lambda console test result was captured.
- A browser showed a successful API response.
- Console views for an ALB, Auto Scaling group, and DynamoDB table were captured.

## Limitations

No Lambda source package, API definition, state-machine definition, database schema, or integration code is included. The available evidence supports individual workflow components and a documented architecture, not a complete reproducible application.

`AWS_Week9_Task_Submission_Clean.pdf` is retained inside a private recovery archive and was used only to reconcile evidence status; it is not published here.
