# UpdateIssuedCardState

Updates the state of a Moov issued card.
- `closed`: The card is permanently deactivated and cannot approve authorizations. A card can be closed by request or when it expires.

## Example Usage

```python
from moovio_sdk.models.components import UpdateIssuedCardState

value = UpdateIssuedCardState.CLOSED
```


## Values

| Name     | Value    |
| -------- | -------- |
| `CLOSED` | closed   |