"""A teaching model for consecutive target health-check thresholds, not ALB code."""

from dataclasses import dataclass


@dataclass
class TargetHealth:
    healthy_threshold: int = 2
    unhealthy_threshold: int = 2
    state: str = "initial"
    consecutive_successes: int = 0
    consecutive_failures: int = 0

    def __post_init__(self) -> None:
        if type(self.healthy_threshold) is not int or type(self.unhealthy_threshold) is not int:
            raise TypeError("health thresholds must be integers")
        if self.healthy_threshold < 1 or self.unhealthy_threshold < 1:
            raise ValueError("health thresholds must be at least 1")
        if not isinstance(self.state, str) or self.state not in {"initial", "healthy", "unhealthy"}:
            raise ValueError("state must be initial, healthy, or unhealthy")
        counts = (self.consecutive_successes, self.consecutive_failures)
        if any(type(value) is not int for value in counts):
            raise TypeError("consecutive observation counts must be integers")
        if any(value < 0 for value in counts):
            raise ValueError("consecutive observation counts must be nonnegative integers")

    def observe(self, passed: bool) -> str:
        if type(passed) is not bool:
            raise TypeError("health observation must be a bool")
        if passed:
            self.consecutive_successes += 1
            self.consecutive_failures = 0
            if self.consecutive_successes >= self.healthy_threshold:
                self.state = "healthy"
        else:
            self.consecutive_failures += 1
            self.consecutive_successes = 0
            if self.consecutive_failures >= self.unhealthy_threshold:
                self.state = "unhealthy"
        return self.state
