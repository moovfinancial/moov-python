# SweepSubtotal


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [components.WalletTransactionType](../../models/components/wallettransactiontype.md) | :heavy_check_mark:                                                                   | The type of wallet transaction the subtotal is for.                                  |
| `count`                                                                              | *int*                                                                                | :heavy_check_mark:                                                                   | The number of transactions of this type accrued in the sweep.                        |
| `amount`                                                                             | [components.AmountDecimal](../../models/components/amountdecimal.md)                 | :heavy_check_mark:                                                                   | The value of transactions of this type accrued in the sweep.                         |