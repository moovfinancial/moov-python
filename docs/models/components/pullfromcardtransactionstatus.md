# PullFromCardTransactionStatus

Status of a pull-from-card transaction.

## Example Usage

```python
from moovio_sdk.models.components import PullFromCardTransactionStatus

value = PullFromCardTransactionStatus.INITIATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INITIATED` | initiated   |
| `FAILED`    | failed      |
| `COMPLETED` | completed   |