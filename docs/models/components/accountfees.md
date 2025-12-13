# AccountFees

A detailed breakdown of account fees.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `wallet_fee`                                                                   | [components.AmountDecimal](../../models/components/amountdecimal.md)           | :heavy_check_mark:                                                             | Fees associated with wallet services.                                          |
| `merchant_pci_fee`                                                             | [components.AmountDecimal](../../models/components/amountdecimal.md)           | :heavy_check_mark:                                                             | Fees for PCI compliance.                                                       |
| `kyb_fee`                                                                      | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | Fees for business verification.                                                |
| `kyc_fee`                                                                      | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | Fees for customer verification.                                                |
| `transaction_monitoring_fee`                                                   | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | Fees for transaction risk monitoring.                                          |
| `total`                                                                        | [components.AmountDecimal](../../models/components/amountdecimal.md)           | :heavy_check_mark:                                                             | Total platform fees.                                                           |