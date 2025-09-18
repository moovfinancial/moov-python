# BillingInterchangeProgramFee

Details of a specific interchange program fee.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `program_name`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The name of the interchange program.                                 |
| `count`                                                              | *int*                                                                | :heavy_check_mark:                                                   | The number of transactions for this program.                         |
| `percentage_rate`                                                    | *Decimal*                                                            | :heavy_check_mark:                                                   | The percentage rate for this program.                                |
| `per_item_rate`                                                      | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | The per-item rate for this program.                                  |
| `total`                                                              | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | The total fee amount for this program.                               |
| `transfer_volume`                                                    | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | The total transfer volume for this program.                          |