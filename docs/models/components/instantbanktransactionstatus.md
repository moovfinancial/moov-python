# InstantBankTransactionStatus

Status of a transaction within the instant-bank lifecycle.

## Example Usage

```python
from moovio_sdk.models.components import InstantBankTransactionStatus

value = InstantBankTransactionStatus.INITIATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `INITIATED`                | initiated                  |
| `COMPLETED`                | completed                  |
| `FAILED`                   | failed                     |
| `ACCEPTED_WITHOUT_POSTING` | accepted-without-posting   |