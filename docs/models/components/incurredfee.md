# IncurredFee

A fee incurred by a user.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `fee_id`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `account_id`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `wallet_id`                                                                    | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `created_on`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `fee_name`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |
| `amount`                                                                       | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `generated_by`                                                                 | [Optional[components.GeneratedBy]](../../models/components/generatedby.md)     | :heavy_minus_sign:                                                             | The entity that generated the fee.                                             |