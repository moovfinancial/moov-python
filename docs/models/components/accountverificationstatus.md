# ~~AccountVerificationStatus~~

Possible states an account verification can be in.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

## Example Usage

```python
from moovio_sdk.models.components import AccountVerificationStatus

value = AccountVerificationStatus.UNVERIFIED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `UNVERIFIED` | unverified   |
| `PENDING`    | pending      |
| `RESUBMIT`   | resubmit     |
| `REVIEW`     | review       |
| `VERIFIED`   | verified     |
| `FAILED`     | failed       |