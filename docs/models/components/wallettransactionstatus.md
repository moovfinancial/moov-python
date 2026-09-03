# WalletTransactionStatus

## Example Usage

```python
from moovio_sdk.models.components import WalletTransactionStatus

value = WalletTransactionStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `COMPLETED` | completed   |
| `CANCELED`  | canceled    |
| `FAILED`    | failed      |