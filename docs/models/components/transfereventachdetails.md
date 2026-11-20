# TransferEventACHDetails


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `status`                                                                           | [components.ACHTransactionStatus](../../models/components/achtransactionstatus.md) | :heavy_check_mark:                                                                 | Status of a transaction within the ACH lifecycle.                                  |
| `return_`                                                                          | [Optional[components.ACHException]](../../models/components/achexception.md)       | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `correction`                                                                       | [Optional[components.ACHException]](../../models/components/achexception.md)       | :heavy_minus_sign:                                                                 | N/A                                                                                |