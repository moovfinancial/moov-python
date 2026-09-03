# AdjustmentFees

A detailed breakdown of adjustment (correction) fees by fee name.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `items`                                                                              | List[[components.BillingAdjustment](../../models/components/billingadjustment.md)]   | :heavy_check_mark:                                                                   | Adjustment fees grouped by fee name.                                                 |
| `total`                                                                              | [components.BillingCountAndAmount](../../models/components/billingcountandamount.md) | :heavy_check_mark:                                                                   | Total adjustment fees.                                                               |