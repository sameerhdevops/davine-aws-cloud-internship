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
        if self.healthy_threshold < 1 or self.unhealthy_threshold < 1:
            raise ValueError("health thresholds must be at least 1")

    def observe(self, passed: bool) -> str:
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
