# GetRefundRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `transfer_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Identifier for the transfer.                                         |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `refund_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Identifier for the refund.                                           |
| `x_moov_version`                                                     | [Optional[components.Versions]](../../models/components/versions.md) | :heavy_minus_sign:                                                   | Specify an API version.                                              |