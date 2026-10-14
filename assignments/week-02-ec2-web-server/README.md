# Week 2 — EC2 and host-level security

## Objective and observed workflow

The recovered exercise combined a small EC2 web host with basic Linux access and monitoring. The report and captures show an instance in `running` state, type `t3.micro`, all three instance status checks passing in one historical capture, a CPU alarm creation notification, browser-based access to a simple page, and an Elastic IP association.

![Sanitized Week 2 console crop showing an EC2 instance running as a t3.micro with three status checks passed and an alarm creation notification; account, host, and resource identifiers are redacted.](../../evidence/assets/week-02-ec2/week-02-ec2-observed-status.png)

*Original internship screenshot, published as a sanitized derivative. It records a historical instance view and an alarm-created notification; it does not establish current state, alarm evaluation, or notification delivery.*

## Recovered evidence and portal status

**Original internship artifacts:** a task brief, a dated Week 2 report, and several EC2/Linux/network/monitoring screenshots were found. The public image is a redacted crop of one original screenshot; the original remains unchanged and private. Other screenshots include an IP address, instance identifiers, and host/account context, so they are not published.

**Portal schedule:** Week 2 is marked Completed as reported by the user. No portal screenshot/export was found. The supplied portal submission history separately says “No weekly submissions yet.” The recovered report is not proof of a portal upload or acceptance.

## Security and operational decisions

The historical security-group capture shows SSH limited to one `/32`, while HTTP on port 80 is open to `0.0.0.0/0` for the web exercise. A separate launch form later displays an SSH-from-anywhere warning; it is not evidence that this rule was applied. These are contextual observations, not recommended defaults. For a real host, restrict ingress to the required source, patch the OS, use a managed access path where feasible, separate web traffic from administration, and review alarms and logs. A running instance is not the same as a healthy application.

Elastic IPs and continuously running instances can incur charges. Review address attachment and instance lifecycle, and remove lab resources through an authorized cleanup process after use.

For an interview: “I distinguish EC2 instance checks from application health. The instance can pass platform checks while the service is unavailable, so I would also verify the process, listener, security-group path, and application response.”

## Limitations and links

No user-data script, web-root content, security-group source file, or Terraform configuration was recovered. The screenshot is not a current deployment or proof that the alarm fired. See the [gallery entry](../../evidence/README.md#week-2-ec2-and-host-level-security) and [evidence manifest](../../evidence/manifest.csv).

Next: [Week 3 — VPC networking](../week-03-vpc-networking/README.md).
