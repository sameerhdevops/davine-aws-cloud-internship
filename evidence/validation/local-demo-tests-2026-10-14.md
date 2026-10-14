# Local demonstration test record

Date: 2026-10-14

Environment: Windows `windows_amd64`, Python 3.14.7

## Command

```powershell
python -m unittest discover -s tests -v
```

## Result

Exit code: `0`

```text
Ran 11 tests in 0.011s

OK
```

The tests cover the included VPC plan validator, health-threshold state machine, S3-shaped event parser, simplified alarm arithmetic, in-memory idempotency example, and narrow static policy checker. They run locally without external dependencies and call no AWS API. They validate only these small examples; they are not AWS service conformance tests or deployment evidence.

The separate `python demos/week03_vpc/validate.py` command also exited `0` and reported that the illustrative four-subnet plan is internally consistent. It called no AWS API.
