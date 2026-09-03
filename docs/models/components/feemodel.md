# FeeModel

Specifies the pricing model used for the calculation of the final fee.

## Example Usage

```python
from moovio_sdk.models.components import FeeModel

value = FeeModel.FIXED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `FIXED`    | fixed      |
| `BLENDED`  | blended    |
| `VARIABLE` | variable   |