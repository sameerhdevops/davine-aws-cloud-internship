# Week 10 — Governance, security, and cost review

## Evidence status

**Verified complete as retained activity evidence.** A five-page activity report, a four-page audit report, and historical budget, Cost Explorer, security, Trusted Advisor, and Well-Architected captures are retained privately. This status does not claim a current or fully remediated AWS account.

## Purpose and topics

The material covers Well-Architected review, IAM and security posture, Trusted Advisor, AWS Budgets, Cost Explorer, and cost-conscious remediation framing.

## Evidence

Two sanitized derivatives are published in the [central evidence gallery](../../evidence/README.md) and the [cross-cutting review](../../cross-cutting/aws-security-governance-cost/README.md):

- The IAM dashboard crop showed root MFA enabled and no active root access keys at the unknown capture time. It does not prove who configured the controls or their current state.
- The Trusted Advisor crop showed zero public EBS snapshots and zero public RDS snapshots in the displayed checks at capture time. It does not establish the absence of other findings.

The original screenshots are unchanged and remain private. Budget and Cost Explorer images were withheld because they expose account-specific financial details. The Well-Architected image records an incomplete review. The before/after remediation image includes identifiers and claims without independent verification. No public screenshot demonstrates a CloudWatch alarm or completed remediation.

## What can be stated safely

- Week 10 activity and audit submissions exist in the private source collection.
- Historical captures cover budget/cost review and security/governance consoles.
- The reports document recommendations and review themes; they do not prove those recommendations were applied or remain in effect.

## Validation boundary

The reports and screenshots record a point in time. They do not prove that every recommendation was implemented, persisted, or remains in effect. This portfolio does not claim a live hardened environment or a cost outcome.

## Security note

Original material can expose account, identity, endpoint, resource, or financial context. It is withheld from Git. The public derivatives remove identifying headers and retain only the specific observations stated above.
