"""A simple numeric M-of-N alarm example; not an Amazon CloudWatch emulator."""

from __future__ import annotations

from math import isfinite
from typing import Sequence


def evaluate(
    datapoints: Sequence[float | None],
    *,
    threshold: float,
    evaluation_periods: int,
    datapoints_to_alarm: int,
) -> str:
    if evaluation_periods < 1 or not 1 <= datapoints_to_alarm <= evaluation_periods:
        raise ValueError("require 1 <= datapoints_to_alarm <= evaluation_periods")
    if not isfinite(threshold):
        raise ValueError("threshold must be finite")
    window = list(datapoints[-evaluation_periods:])
    if len(window) < evaluation_periods or any(value is None for value in window):
        return "INSUFFICIENT_DATA"
    numeric = [float(value) for value in window if value is not None]
    if any(not isfinite(value) for value in numeric):
        raise ValueError("datapoints must be finite numbers or None")
    breaches = sum(value > threshold for value in numeric)
    return "ALARM" if breaches >= datapoints_to_alarm else "OK"
