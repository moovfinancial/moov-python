# ReverseTransferRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `transfer_id`                                                  | *str*                                                          | :heavy_check_mark:                                             | Identifier for the transfer.                                   |                                                                |
| `x_idempotency_key`                                            | *str*                                                          | :heavy_check_mark:                                             | Prevents duplicate reversals from being created.               | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                           |
| `create_reversal`                                              | [Optional[models.CreateReversal]](../models/createreversal.md) | :heavy_minus_sign:                                             | N/A                                                            |                                                                |