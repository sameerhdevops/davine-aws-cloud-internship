"""A simple numeric M-of-N alarm example; not an Amazon CloudWatch emulator."""

from __future__ import annotations

from collections.abc import Sequence as RuntimeSequence
from math import isfinite
from typing import Sequence


def evaluate(
    datapoints: Sequence[float | None],
    *,
    threshold: float,
    evaluation_periods: int,
    datapoints_to_alarm: int,
) -> str:
    if type(evaluation_periods) is not int or type(datapoints_to_alarm) is not int:
        raise TypeError("evaluation_periods and datapoints_to_alarm must be integers")
    if evaluation_periods < 1 or not 1 <= datapoints_to_alarm <= evaluation_periods:
        raise ValueError("require 1 <= datapoints_to_alarm <= evaluation_periods")
    if type(threshold) not in {int, float}:
        raise TypeError("threshold must be an int or float")
    try:
        threshold_is_finite = isfinite(threshold)
    except OverflowError:
        threshold_is_finite = False
    if not threshold_is_finite:
        raise ValueError("threshold must be finite")
    if not isinstance(datapoints, RuntimeSequence) or isinstance(
        datapoints, (str, bytes, bytearray)
    ):
        raise TypeError("datapoints must be a sequence of numbers or None")
    window = list(datapoints[-evaluation_periods:])
    numeric: list[int | float] = []
    missing = False
    for value in window:
        if value is None:
            missing = True
            continue
        if type(value) not in {int, float}:
            raise TypeError("datapoints must contain only finite numbers or None")
        try:
            value_is_finite = isfinite(value)
        except OverflowError:
            value_is_finite = False
        if not value_is_finite:
            raise ValueError("datapoints must contain only finite numbers or None")
        numeric.append(value)
    if len(window) < evaluation_periods or missing:
        return "INSUFFICIENT_DATA"
    breaches = sum(value > threshold for value in numeric)
    return "ALARM" if breaches >= datapoints_to_alarm else "OK"
