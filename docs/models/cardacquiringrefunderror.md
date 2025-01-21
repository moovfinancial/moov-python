# CardAcquiringRefundError

Details of a card refund.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `refund_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Identifier for the refund.                                           |
| `created_on`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_on`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `status`                                                             | [models.RefundStatus](../models/refundstatus.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |
| `amount`                                                             | [models.Amount](../models/amount.md)                                 | :heavy_check_mark:                                                   | N/A                                                                  |
| `card_details`                                                       | [Optional[models.RefundCardDetails]](../models/refundcarddetails.md) | :heavy_minus_sign:                                                   | N/A                                                                  |