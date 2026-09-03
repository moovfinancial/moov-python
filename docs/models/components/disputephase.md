# DisputePhase

The phase of a dispute within the dispute lifecycle.

## Example Usage

```python
from moovio_sdk.models.components import DisputePhase

value = DisputePhase.PRE_DISPUTE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `PRE_DISPUTE` | pre-dispute   |
| `INQUIRY`     | inquiry       |
| `CHARGEBACK`  | chargeback    |
| `UNKNOWN`     | unknown       |