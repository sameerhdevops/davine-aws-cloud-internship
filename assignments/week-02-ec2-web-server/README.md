# Week 2 - EC2 web server

## Evidence status

**Strongly supported probable assignment.** A browser capture explicitly labels a basic AWS web server as a Week 2 task. Related screens show an EC2 instance, browser-based Linux access, an Elastic IP, security-group rules, and a CloudWatch alarm.

## Objective

Document a basic web-hosting workflow using an EC2 instance and verify that a simple page was reachable.

## Observed workflow

1. An EC2 instance was shown running.
2. Browser-based Linux access was shown.
3. A public address was associated and a basic page was rendered.
4. A CPU-related CloudWatch alarm was shown as created.

## Security considerations

Historical screenshots show SSH/network exposure details. They are not published because addresses and resource identifiers are visible, and they should not be read as a recommended public-access pattern. Production access should use least privilege, restricted ingress, current patching, and managed access paths where appropriate.

## Limitations

No server configuration, user-data script, web-page source, or infrastructure definition is available. The exercise demonstrates capture-time evidence, not an active deployment.
