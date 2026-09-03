# BankAccountVerificationStatus

## Example Usage

```python
from moovio_sdk.models.components import BankAccountVerificationStatus

value = BankAccountVerificationStatus.NEW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `NEW`                   | new                     |
| `SENT_CREDIT`           | sent-credit             |
| `MAX_ATTEMPTS_EXCEEDED` | max-attempts-exceeded   |
| `FAILED`                | failed                  |
| `EXPIRED`               | expired                 |
| `SUCCESSFUL`            | successful              |