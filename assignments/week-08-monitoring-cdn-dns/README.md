# Week 8 — Observability, DNS, and CDN

## Objective and recovered evidence

The recovered brief and September report cover CloudWatch metrics/alarms, CloudTrail, Route 53, and CloudFront. A console alarm capture shows a CPU condition above 70 for one datapoint, actions enabled, and state `Insufficient data` at the displayed update time. The redacted public derivative preserves that operationally important state.

![Sanitized CloudWatch alarms row showing a CPUUtilization threshold above 70 for one datapoint, actions enabled, and Insufficient data; the account and alarm name are redacted.](../../evidence/assets/week-08-cloudwatch/week-08-cpu-alarm-insufficient-data.png)

*Original internship screenshot, sanitized for publication. Capture date is 2026-09-09. It demonstrates the configured threshold and state shown at capture time; it does not show a breaching alarm, delivered notification, or current monitoring state.*

**Portal schedule:** Week 8 is marked Completed as reported by the user. No portal screenshot/export was found; the supplied submission history says “No weekly submissions yet.” The report itself notes that CloudTrail, Route 53, and CloudFront captures were missing; this portfolio does not imply those console screenshots were recovered.

## Local alarm-arithmetic demonstration

[`alarm_math.py`](../../demos/week08_observability/alarm_math.py) calculates a simple numeric M-of-N threshold decision for a short list of datapoints. Run `python -m unittest discover -s tests -v` from the repository root. This **reproducible demonstration** does not emulate CloudWatch aggregation, alarm timing, missing-data settings, metric delivery, or actions.

Operationally, choose a metric that represents user impact, set a threshold from baseline and SLO context, and test missing-data and action behavior. CloudWatch charges can arise from alarms, custom metrics, dashboards, logs, and data ingestion. Route 53 and CloudFront introduce DNS, caching, invalidation, certificate, and data-transfer considerations.

“An `Insufficient data` alarm is not proof that a threshold was crossed. I would check metric publication, dimensions, period/evaluation settings, and alarm history before claiming the alert worked.”

## Limits and links

The two original alarm screenshots are not current-state evidence; only the selected crop is public. Report-described DNS/CDN topics are not screenshot-verified here. See the [gallery](../../evidence/README.md#week-8-observability-dns-and-cdn) and [demo catalog](../../demos/README.md).

Next: [Week 9 — serverless integration and scaling](../week-09-serverless-api/README.md).
