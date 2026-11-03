# CreateCardPaymentOptionsCaptureMethod

How funds are captured. `automatic` (default) authorizes and captures the full amount right away.
`manual` authorizes only; capture later with the capture endpoint.

## Example Usage

```python
from moovio_sdk.models.components import CreateCardPaymentOptionsCaptureMethod

value = CreateCardPaymentOptionsCaptureMethod.AUTOMATIC
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `AUTOMATIC` | automatic   |
| `MANUAL`    | manual      |