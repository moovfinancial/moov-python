# RunTransfer

Defines the attributes of a transfer.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `amount`                                                           | [models.Amount](../models/amount.md)                               | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `destination`                                                      | [models.SchedulePaymentMethod](../models/schedulepaymentmethod.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `partner_account_id`                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | c520f1b9-0ba7-42f5-b977-248cdbe41c69                               |
| `source`                                                           | [models.SchedulePaymentMethod](../models/schedulepaymentmethod.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `description`                                                      | *str*                                                              | :heavy_check_mark:                                                 | Simple description to place on the transfer.                       |                                                                    |