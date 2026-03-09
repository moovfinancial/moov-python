# WalletStatus

Status of a wallet.
  - `active`: The wallet is available for use and has an enabled payment method.
  - `closed`: The wallet is no longer active and the corresponding payment method has been disabled.

## Example Usage

```python
from moovio_sdk.models.components import WalletStatus

value = WalletStatus.ACTIVE
```


## Values

| Name     | Value    |
| -------- | -------- |
| `ACTIVE` | active   |
| `CLOSED` | closed   |