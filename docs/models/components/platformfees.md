# PlatformFees

A detailed breakdown of platform fees.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `wallet_fee`                                                         | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Fees associated with wallet services.                                |
| `merchant_pci_fee`                                                   | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Fees for PCI compliance.                                             |
| `total`                                                              | [components.AmountDecimal](../../models/components/amountdecimal.md) | :heavy_check_mark:                                                   | Total platform fees.                                                 |