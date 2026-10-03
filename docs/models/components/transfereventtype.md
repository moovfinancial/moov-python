# TransferEventType

The event family.

## Example Usage

```python
from moovio_sdk.models.components import TransferEventType

value = TransferEventType.TRANSFER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `TRANSFER`            | transfer              |
| `AUTHORIZATION`       | authorization         |
| `CAPTURE`             | capture               |
| `REFUND`              | refund                |
| `CANCELLATION`        | cancellation          |
| `DISPUTE`             | dispute               |
| `ACH_CREDIT`          | ach-credit            |
| `ACH_DEBIT`           | ach-debit             |
| `INSTANT_BANK_CREDIT` | instant-bank-credit   |
| `WIRE_CREDIT`         | wire-credit           |
| `CARD_PAYMENT`        | card-payment          |
| `PUSH_TO_CARD`        | push-to-card          |
| `PULL_FROM_CARD`      | pull-from-card        |
| `WALLET_CREDIT`       | wallet-credit         |
| `WALLET_DEBIT`        | wallet-debit          |