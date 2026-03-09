# DomesticPushToCard

Indicates which level of domestic push-to-card transfer is supported by the card, if any.

## Example Usage

```python
from moovio_sdk.models.components import DomesticPushToCard

value = DomesticPushToCard.NOT_SUPPORTED
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NOT_SUPPORTED` | not-supported   |
| `STANDARD`      | standard        |
| `FAST_FUNDS`    | fast-funds      |
| `UNKNOWN`       | unknown         |