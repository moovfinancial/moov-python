# BillingSummaryInterchange

A summary of interchange fees by card brand.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `visa`                                                               | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Total interchange fees for Visa.                                     |
| `mastercard`                                                         | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Total interchange fees for Mastercard.                               |
| `discover`                                                           | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Total interchange fees for Discover.                                 |
| `american_express`                                                   | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Total interchange fees for American Express.                         |