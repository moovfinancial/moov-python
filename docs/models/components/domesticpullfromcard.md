# DomesticPullFromCard

Indicates if the card supports domestic pull-from-card transfer.

## Example Usage

```python
from moovio_sdk.models.components import DomesticPullFromCard

value = DomesticPullFromCard.NOT_SUPPORTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NOT_SUPPORTED` | not-supported   |
| `SUPPORTED`     | supported       |
| `UNKNOWN`       | unknown         |