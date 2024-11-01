# ScheduledPaymentMethod

Defines a payment method to use for the scheduled transfer


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `payment_method_id`                                                                | *str*                                                                              | :heavy_check_mark:                                                                 | ID of the payment method to use.                                                   |
| `ach_details`                                                                      | [OptionalNullable[models.ScheduledAchDetails]](../models/scheduledachdetails.md)   | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `card_details`                                                                     | [OptionalNullable[models.ScheduledCardDetails]](../models/scheduledcarddetails.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |