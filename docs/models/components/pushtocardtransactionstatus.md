# PushToCardTransactionStatus

Status of a push-to-card transaction.

## Example Usage

```python
from moovio_sdk.models.components import PushToCardTransactionStatus

value = PushToCardTransactionStatus.INITIATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INITIATED` | initiated   |
| `DEFERRED`  | deferred    |
| `CANCELED`  | canceled    |
| `FAILED`    | failed      |
| `COMPLETED` | completed   |