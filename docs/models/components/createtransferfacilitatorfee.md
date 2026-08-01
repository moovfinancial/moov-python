# CreateTransferFacilitatorFee

Total or markup fee to apply when creating a transfer.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `total`                                                                        | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | Total facilitator fee. Only either `total` or `markup` can be set.             |
| `markup`                                                                       | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | Markup facilitator fee. Only either `total` or `markup` can be set.            |