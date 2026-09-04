# WireFailureCode

Status codes for wire failures.

## Example Usage

```python
from moovio_sdk.models.components import WireFailureCode

value = WireFailureCode.PROCESSING_ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `PROCESSING_ERROR`          | processing-error            |
| `INVALID_ACCOUNT`           | invalid-account             |
| `ACCOUNT_CLOSED`            | account-closed              |
| `ACCOUNT_BLOCKED`           | account-blocked             |
| `INVALID_FIELD`             | invalid-field               |
| `TRANSACTION_NOT_SUPPORTED` | transaction-not-supported   |
| `LIMIT_EXCEEDED`            | limit-exceeded              |
| `INVALID_AMOUNT`            | invalid-amount              |
| `OTHER`                     | other                       |