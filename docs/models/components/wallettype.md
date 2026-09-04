# WalletType

Type of a wallet.
  - `default`: The system-generated wallet automatically created when an account is granted the wallet capability.
  - `general`: An additional, user-defined wallet created via API or Dashboard.
  - `card-issuing`: The system-generated wallet automatically created when an account is granted the card-issuing capability.

## Example Usage

```python
from moovio_sdk.models.components import WalletType

value = WalletType.DEFAULT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `DEFAULT`      | default        |
| `GENERAL`      | general        |
| `CARD_ISSUING` | card-issuing   |