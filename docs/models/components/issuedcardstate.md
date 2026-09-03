# IssuedCardState

The `state` represents the operational status of an issued card. A card can only approve incoming authorizations if it is in an active state.

- `active`: The card is operational and can approve authorizations.
- `frozen`: The card is temporarily suspended and cannot approve authorizations. A frozen card can be reactivated by setting its state back to `active`.
- `closed`: The card is permanently deactivated and cannot approve authorizations. A card can be closed by request or when it expires.

## Example Usage

```python
from moovio_sdk.models.components import IssuedCardState

value = IssuedCardState.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `ACTIVE` | active   |
| `FROZEN` | frozen   |
| `CLOSED` | closed   |