"""Show retry behavior with a process-local cache; not durable distributed idempotency."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    request_id: str
    status: str


class InMemoryIdempotency:
    def __init__(self) -> None:
        self._results: dict[str, Result] = {}

    def handle(self, idempotency_key: str) -> Result:
        if not isinstance(idempotency_key, str):
            raise TypeError("idempotency key must be a string")
        if not idempotency_key.strip():
            raise ValueError("idempotency key cannot be empty")
        cached = self._results.get(idempotency_key)
        if cached is not None:
            return cached
        result = Result(request_id=f"req-{len(self._results) + 1}", status="accepted")
        self._results[idempotency_key] = result
        return result
