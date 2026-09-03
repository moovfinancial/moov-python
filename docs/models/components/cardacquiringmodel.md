# CardAcquiringModel

Specifies the card processing pricing model

## Example Usage

```python
from moovio_sdk.models.components import CardAcquiringModel

value = CardAcquiringModel.COST_PLUS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `COST_PLUS` | cost-plus   |
| `FLAT_RATE` | flat-rate   |