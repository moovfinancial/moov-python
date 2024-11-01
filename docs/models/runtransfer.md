# RunTransfer

Defines the attributes of a transfer


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `amount`                                                             | [models.Amount](../models/amount.md)                                 | :heavy_check_mark:                                                   | An integer value representing money in a specific currency.          |
| `partner_account_id`                                                 | *str*                                                                | :heavy_check_mark:                                                   | AccountID of the Moov partner in the transfer.                       |
| `source`                                                             | [models.ScheduledPaymentMethod](../models/scheduledpaymentmethod.md) | :heavy_check_mark:                                                   | Defines a payment method to use for the scheduled transfer           |
| `destination`                                                        | [models.ScheduledPaymentMethod](../models/scheduledpaymentmethod.md) | :heavy_check_mark:                                                   | Defines a payment method to use for the scheduled transfer           |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Simple description to place on the transfer                          |