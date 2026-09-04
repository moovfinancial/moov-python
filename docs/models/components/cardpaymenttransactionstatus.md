# CardPaymentTransactionStatus

Status of a card payment transaction.

## Example Usage

```python
from moovio_sdk.models.components import CardPaymentTransactionStatus

value = CardPaymentTransactionStatus.INITIATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INITIATED` | initiated   |
| `CONFIRMED` | confirmed   |
| `CANCELED`  | canceled    |
| `SETTLED`   | settled     |
| `FAILED`    | failed      |
| `COMPLETED` | completed   |