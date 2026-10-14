# Week 2 — EC2 and host-level security

## Objective

Explore a small EC2 web host, basic Linux access, instance-health signals, and the difference between platform status and application health.

## What I did or implemented

The retained report and console captures describe an instance in **running** state as **t3.micro**, three instance status checks passing in one capture, an alarm-creation notification, browser access to a simple page, and an Elastic IP association. The available portal information marks Week 2 Completed and separately reports “No weekly submissions yet”; no portal screenshot or export is retained.

## Key concepts

The historical security-group capture shows SSH limited to one **/32** and HTTP on port 80 open to **0.0.0.0/0** for the web exercise. A separate launch form displays a warning about SSH from anywhere, but does not establish that the rule was applied. These are observations, not recommended defaults. For a real host, restrict ingress, patch the OS, prefer a managed access path where practical, separate web and administration traffic, and review alarms and logs.

Instance status checks are not application checks. A host can pass platform checks while its process, listener, or application response is failing. Elastic IPs and continuously running instances can also incur charges; review address attachment and the lab cleanup plan.

## Evidence and links

![Historical EC2 console crop showing a running t3.micro, three status checks passed, and an alarm-created notification; account, host, and resource identifiers are redacted.](../../evidence/assets/week-02-ec2/week-02-ec2-observed-status.png)

*Sanitized derivative described in the existing portfolio record as an internship screenshot. It records a historical instance view and an alarm-created notification; it does not show alarm evaluation or notification delivery.* See the [gallery entry](../../evidence/README.md#week-2-ec2-and-host-level-security) and [evidence manifest](../../evidence/manifest.csv).

## Limitations

No user-data script, web-root content, security-group source, or Terraform configuration is available in the repository. Other described screenshots contain identifiers and are not published. The report and image do not establish present AWS state, a functioning alarm, or portal upload or acceptance.

## Next improvements

A follow-up local lab could define a minimal host and security-group configuration, restrict SSH to a supplied test CIDR, and check host and application health separately. Any future AWS exercise would require an authorized budget and cleanup plan.
