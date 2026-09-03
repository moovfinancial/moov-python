# TransferStatus

Status of a transfer.

## Example Usage

```python
from moovio_sdk.models.components import TransferStatus

value = TransferStatus.CREATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `CREATED`   | created     |
| `PENDING`   | pending     |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |
| `REVERSED`  | reversed    |
| `QUEUED`    | queued      |
| `CANCELED`  | canceled    |