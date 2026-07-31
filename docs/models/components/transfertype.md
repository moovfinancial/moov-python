# TransferType

The rail and direction used to move funds for a transfer.

## Example Usage

```python
from moovio_sdk.models.components import TransferType

value = TransferType.CARD_PAYMENT
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `CARD_PAYMENT`            | card-payment              |
| `PUSH_TO_CARD`            | push-to-card              |
| `PULL_FROM_CARD`          | pull-from-card            |
| `ACH_DEBIT`               | ach-debit                 |
| `ACH_CREDIT`              | ach-credit                |
| `ACH_DEBIT_TO_ACH_CREDIT` | ach-debit-to-ach-credit   |
| `INSTANT_BANK_CREDIT`     | instant-bank-credit       |
| `WALLET`                  | wallet                    |