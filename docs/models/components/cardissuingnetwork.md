# CardIssuingNetwork

The name of the network a card transaction is routed through.

## Example Usage

```python
from moovio_sdk.models.components import CardIssuingNetwork

value = CardIssuingNetwork.DISCOVER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DISCOVER` | discover   |
| `SHAZAM`   | shazam     |
| `VISA`     | visa       |