# Public evidence gallery

This page displays nine screenshot derivatives described by the existing portfolio record as internship evidence. The captions state the visible historical observation and its limits. Historical captures do not establish current AWS state.

The captions and provenance descriptions follow existing portfolio records; private originals were not inspected. Source-to-derivative matches, dates, redactions, and source descriptions have not been independently checked against those private files. The manifest records this limitation. The gallery describes only what is visible in each published derivative.

The [CSV manifest](manifest.csv) records artifact type, provenance, evidence category, public path, date confidence, supported claim, limitations, and redaction or withholding reason. Paths are repository-relative; private source-machine paths are not included.

## Week 2 — EC2 and host-level security

![Screenshot derivative showing a t3.micro row marked running with three status checks passing and an alarm-created notification; identifying details are redacted.](assets/week-02-ec2/week-02-ec2-observed-status.png)

**What it shows:** one historical console view displayed `running`, `t3.micro`, and `3/3 checks passed`, alongside an alarm creation notification. **It does not show:** current instance state, alarm evaluation, or notification delivery. The account/host/resource identity and network addresses are not visible.

[Week 2 technical explanation](../assignments/week-02-ec2-web-server/README.md).

## Week 5 — high availability and Auto Scaling

![Screenshot derivative showing a successful launch activity associated with an unhealthy instance; the instance identifier is redacted.](assets/week-05-high-availability/week-05-asg-replacement-event.png)

**What it shows:** a dated activity event reports a successful EC2 launch in response to an unhealthy instance needing replacement. **It does not show:** the replacement target becoming healthy, sustained availability, or current state. The separate target-group capture had one healthy and one unhealthy target; the ALB detail capture was still provisioning.

[Week 5 technical explanation](../assignments/week-05-high-availability/README.md).

## Week 7 — Infrastructure as Code

![Screenshot derivative showing CloudShell output that reports one Terraform resource added and a subsequent query returning a running t3.micro; identifiers and query details are redacted.](assets/week-07-terraform/week-07-terraform-apply-observed.png)

**What it shows:** one original Week 7 screenshot displayed an apply completion summary and a subsequent EC2 query result for a running `t3.micro`. **It does not show:** the original IaC source, the entire apply scope, state safety, the Week 12 reconstruction, or current AWS state. A separate launch-form screenshot showing SSH open to `0.0.0.0/0` is withheld and discussed in the [Week 7 review](../assignments/week-07-infrastructure-as-code/README.md).

## Week 8 — observability, DNS, and CDN

![Screenshot derivative showing a CloudWatch alarm configured for CPUUtilization above 70 for one datapoint, actions enabled, and state Insufficient data; account and alarm identity are redacted.](assets/week-08-cloudwatch/week-08-cpu-alarm-insufficient-data.png)

**What it shows:** on the displayed 2026-09-09 capture, the selected alarm condition was `CPUUtilization > 70 for 1 datapoint`, actions were enabled, and its state was `Insufficient data`. **It does not show:** a threshold breach, notification delivery, or current state. The report notes that CloudTrail, Route 53, and CloudFront screenshots were missing.

[Week 8 technical explanation](../assignments/week-08-monitoring-cdn-dns/README.md).

## Week 9 — serverless integration and scaling

![Screenshot derivative showing a Lambda console test result with Status: Succeeded for a saved test event; function and account context are outside the crop.](assets/week-09-integration/week-09-lambda-test-result.png)

**What it shows:** the Lambda console test result displayed `Status: Succeeded`. **It does not show:** API Gateway integration, production data, durable storage, or an end-to-end workflow. The capture date is unknown.

![Auto Scaling group row with group and launch-template names redacted; the row displays one instance at desired capacity and 1/1 healthy.](assets/week-09-integration/week-09-asg-capacity-health.png)

**What it shows:** a historical Auto Scaling summary row displayed `At desired capacity`, `1/1 Healthy`, desired/minimum capacity 1, maximum 2, and three Availability Zones. Group and launch-template names were redacted in the public derivative. **It does not show:** health over time or that the Week 5 environment was the same group. Capture date is unknown.

[Week 9 technical explanation](../assignments/week-09-serverless-api/README.md).

## Week 10 — governance, security, and cost

### Root-account control summary

![Sanitized IAM dashboard crop reporting root MFA enabled and no active root access keys at capture time.](assets/cross-cutting/aws-security-governance-cost/iam-dashboard-root-controls.png)

This original screenshot derivative shows what the IAM dashboard reported at an unknown capture time. It does not identify who configured the controls, prove present state, or establish least privilege for all identities.

### Trusted Advisor public snapshot checks

![Sanitized Trusted Advisor crop reporting zero public EBS and RDS snapshots in the displayed checks.](assets/cross-cutting/aws-security-governance-cost/trusted-advisor-public-snapshots.png)

This original screenshot derivative shows zero public EBS and RDS snapshots in the displayed checks at an unknown capture time. It does not establish a clean account-wide review; the adjacent S3 check is not expanded.

The Well-Architected capture is withheld because it shows 0 of 57 questions answered and 0 issues, not a completed review. Cost Explorer and budget captures are withheld because they expose account-specific financial data and show different date/filter contexts. The [Week 10 page](../assignments/week-10-governance-audit/README.md) and [cross-cutting review](../cross-cutting/aws-security-governance-cost/README.md) preserve the interpretation without publishing billing details.

## Week 12 — TalentFlow AI capstone

![Screenshot derivative described as a VPC resource map embedded in the final report, showing a named VPC, four-subnet and route-table layout, and Internet Gateway connection; route-table identifier is redacted.](assets/week-12-talentflow-ai/week-12-vpc-resource-map.png)

This derivative shows a historical VPC console map from a page in the retained capstone report. It does not show that the repository’s Terraform created these resources, that the application ran in the VPC, or that all routes and controls were validated. Account and route-table identifiers were redacted; names needed to understand the map remain.

The remaining report pages and captures are withheld because they expose account/resource IDs, endpoints, bucket details, or unverified implementation claims. Their important limits are recorded in the [Week 12 technical page](../assignments/week-12-talentflow-ai/README.md): the report shows a Terraform **plan**, an alarm in `Insufficient data`, and an SNS subscription pending confirmation—not a proven deployment or delivered alert.

## Validation records

- [Validation index](validation/README.md): dated local and hosted records, with their commands, environments, commit scope, and limitations.

These records do not establish an AWS plan or deployment. The workflow has read-only repository permissions and no AWS credentials or deployment steps.

## Publication choices and labels

**Published:** nine selected screenshot derivatives from Weeks 2, 5, 7, 8, 9, 10, and 12. The public files were visually inspected and contain no embedded image metadata. Private originals were not inspected, so source correspondence and claims that originals were left unchanged have not been independently checked. The Week 9 Auto Scaling derivative also masks its group and launch-template names.

**Withheld:** original reports and ZIP archives; account/billing and raw network/security-group screens; a launch form displaying SSH from `0.0.0.0/0`; a DynamoDB example row containing person-like sample data; endpoint/DNS/ARN/resource IDs; the incomplete Well-Architected review capture; and the full capstone/briefing PDFs. These add privacy, ownership, attribution, or interpretation risk beyond the narrow claims already supported by safe crops and written context. The public manifest records major withheld groups.

## Classification key

- **Original internship artifact:** a source report, screenshot, or record described in existing portfolio records; source details have not been independently checked against private originals.
- **Sanitized evidence derivative:** a publication copy with visible redaction/cropping; the underlying historical claim is unchanged.
- **Independent reconstruction:** a later, reasoned diagram or infrastructure subset; the label does not establish personal authorship.
- **Reproducible demonstration:** added local code or tests that demonstrate one bounded behavior; the label does not establish personal authorship.
- **Independently validated:** a specific check actually run, with command, result, environment, and scope recorded.
- **Not established by retained evidence:** a claim for which the available artifacts or checks are insufficient.

The SVG diagrams’ XML, text labels, and internal links were checked against their documentation. No local SVG renderer was available, so their layout has not been visually reviewed.
