# PushDeliverySpeed

Delivery speed options for push-to-card payouts.

## Example Usage

```python
from moovio_sdk.models.components import PushDeliverySpeed

value = PushDeliverySpeed.INSTANT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `INSTANT`  | instant    |
| `DEFERRED` | deferred   |