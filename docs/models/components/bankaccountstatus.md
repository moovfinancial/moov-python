# BankAccountStatus

## Example Usage

```python
from moovio_sdk.models.components import BankAccountStatus

value = BankAccountStatus.NEW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `NEW`                 | new                   |
| `VERIFIED`            | verified              |
| `VERIFICATION_FAILED` | verificationFailed    |
| `PENDING`             | pending               |
| `ERRORED`             | errored               |