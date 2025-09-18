# BillingSummaryDetails

Details of volume and fees for a specific payment method.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `volume_amount`                                                                | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | The total transaction volume amount.                                           |
| `volume_count`                                                                 | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | The total number of transactions.                                              |
| `fee_amount`                                                                   | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | The total fee amount.                                                          |