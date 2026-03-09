# CardUpdateReason

The results of the card update request.

## Example Usage

```python
from moovio_sdk.models.components import CardUpdateReason

value = CardUpdateReason.UNSPECIFIED
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `UNSPECIFIED`        | unspecified          |
| `ACCOUNT_CLOSED`     | account-closed       |
| `CONTACT_CARDHOLDER` | contact-cardholder   |
| `EXPIRATION_UPDATE`  | expiration-update    |
| `NO_CHANGE`          | no-change            |
| `NO_MATCH`           | no-match             |
| `NUMBER_UPDATE`      | number-update        |