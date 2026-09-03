# ACHTransactionStatus

Status of a transaction within the ACH lifecycle.

## Example Usage

```python
from moovio_sdk.models.components import ACHTransactionStatus

value = ACHTransactionStatus.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `UNKNOWN`    |              |
| `INITIATED`  | initiated    |
| `ORIGINATED` | originated   |
| `CORRECTED`  | corrected    |
| `RETURNED`   | returned     |
| `COMPLETED`  | completed    |
| `CANCELED`   | canceled     |