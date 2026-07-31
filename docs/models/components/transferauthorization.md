# TransferAuthorization


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `authorization_id`                                                   | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `requested_amount`                                                   | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `authorized_amount`                                                  | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `captured_amount`                                                    | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `capturable_amount`                                                  | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `expires_on`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |