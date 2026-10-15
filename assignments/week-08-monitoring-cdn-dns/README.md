# Week 8 — Observability, DNS, and CDN

## Objective

I wanted to review CloudWatch metrics and alarms alongside CloudTrail, Route 53, and CloudFront, with attention to what an alarm state tells an operator.

## What I did or implemented

The portfolio’s brief and September report notes cover those services and say that CloudTrail, Route 53, and CloudFront captures were missing. The local [alarm_math.py](../../demos/week08_observability/alarm_math.py) demonstrates an M-of-N calculation over datapoints. A published CloudWatch crop shows a CPU threshold above 70 for one datapoint, actions enabled, and an `Insufficient data` state.

## Key concepts

- **Alarm state:** Metric publication, dimensions, period, evaluation windows, threshold, and missing-data treatment all affect an alarm; `Insufficient data` is not a threshold breach.
- **Operational response:** Check metric delivery, alarm configuration, and history before changing a threshold or concluding that an alert worked.
- **Signal and cost:** Choose measures tied to service impact, and account for alarms, custom metrics, logs, DNS queries, CDN requests, and data transfer.

## Evidence and links

![CloudWatch alarm crop showing a CPUUtilization threshold above 70 for one datapoint, actions enabled, and Insufficient data; account and alarm identifiers are redacted.](../../evidence/assets/week-08-cloudwatch/week-08-cpu-alarm-insufficient-data.png)

*The crop records a selected threshold and state at capture time, not a breach, delivered notification, or current monitoring state.* See the [gallery entry](../../evidence/README.md#week-8-observability-dns-and-cdn) and [demo catalog](../../demos/README.md).

## Limitations

The local example is not CloudWatch emulation; it does not model aggregation, alarm timing, missing-data configuration, metric delivery, or actions. The report-described DNS/CDN topics do not have corresponding screenshots in the repository.

## Next improvements

A small test matrix could cover missing and incomplete datapoints and document how to verify metric dimensions and alarm history.
