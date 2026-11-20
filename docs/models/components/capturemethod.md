# CaptureMethod

When funds for a `card-payment` transfer are captured.

## Example Usage

```python
from moovio_sdk.models.components import CaptureMethod

value = CaptureMethod.AUTOMATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `AUTOMATIC` | automatic   |
| `MANUAL`    | manual      |