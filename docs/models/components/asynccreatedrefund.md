# AsyncCreatedRefund

Asynchronous refund response


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `refund_id`                                                                                | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `created_on`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                       | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `amount`                                                                                   | [components.Amount](../../models/components/amount.md)                                     | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `amount_details`                                                                           | [Optional[components.RefundAmountDetails]](../../models/components/refundamountdetails.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |