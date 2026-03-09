# CardTransactionStatus

Status of a transaction within the card payment lifecycle.

## Example Usage

```python
from moovio_sdk.models.components import CardTransactionStatus

value = CardTransactionStatus.INITIATED
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