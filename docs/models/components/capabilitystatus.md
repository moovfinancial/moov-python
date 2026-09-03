# CapabilityStatus

The status of the capability requested for an account.

## Example Usage

```python
from moovio_sdk.models.components import CapabilityStatus

value = CapabilityStatus.ENABLED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `ENABLED`   | enabled     |
| `DISABLED`  | disabled    |
| `PENDING`   | pending     |
| `IN_REVIEW` | in-review   |