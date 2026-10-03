# RiskVerificationOutcome

The outcome of a bank account risk-verification attempt.

## Example Usage

```python
from moovio_sdk.models.components import RiskVerificationOutcome

value = RiskVerificationOutcome.NOT_ATTEMPTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NOT_ATTEMPTED` | notAttempted    |
| `SUCCESS`       | success         |
| `INCONCLUSIVE`  | inconclusive    |
| `DECLINE`       | decline         |