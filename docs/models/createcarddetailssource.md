# CreateCardDetailsSource

If transfer involves card acceptance, override default card acceptance properties.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dynamic_descriptor`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                         | An optional override of the default card statement descriptor for a transfer. Accounts must be enabled by Moov to set this field.<br/>                                                                                                                                                                                                                                                                                                                                     | WhlBdy *Yoga 11-12                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `transaction_source`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [OptionalNullable[models.TransactionSource]](../models/transactionsource.md)                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Specifies the nature and initiator of a transaction. Crucial for recurring and merchant-initiated transactions as per card scheme rules. Omit for customer-initiated e-commerce transactions.<br/><br/>- `first-recurring`: Initial transaction in a recurring series or saving a card for future merchant-initiated charges<br/>- `recurring`: Regular, merchant-initiated scheduled transactions<br/>- `unscheduled`: Non-regular, merchant-initiated transactions like account top-ups<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |