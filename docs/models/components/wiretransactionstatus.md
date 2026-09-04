# WireTransactionStatus

Status of a transaction within the wire lifecycle.

## Example Usage

```python
from moovio_sdk.models.components import WireTransactionStatus

value = WireTransactionStatus.INITIATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INITIATED` | initiated   |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |
| `RETURNED`  | returned    |