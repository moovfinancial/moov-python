# ReverseTransferRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `x_idempotency_key`                                            | *str*                                                          | :heavy_check_mark:                                             | Prevents duplicate reversals from being created.               |
| `account_id`                                                   | *str*                                                          | :heavy_check_mark:                                             | The Moov account ID.                                           |
| `transfer_id`                                                  | *str*                                                          | :heavy_check_mark:                                             | The transfer ID to reverse.                                    |
| `x_moov_version`                                               | [Optional[models.Versions]](../models/versions.md)             | :heavy_minus_sign:                                             | Specify an API version.                                        |
| `create_reversal`                                              | [Optional[models.CreateReversal]](../models/createreversal.md) | :heavy_minus_sign:                                             | N/A                                                            |