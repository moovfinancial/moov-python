# CreateCaptureRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `x_idempotency_key`                                                  | *str*                                                                | :heavy_check_mark:                                                   | Prevents duplicate captures from being created.                      |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Moov account ID of the partner for the transfer.                     |
| `transfer_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Identifier for the auth-capture `card-payment` transfer.             |
| `create_capture`                                                     | [components.CreateCapture](../../models/components/createcapture.md) | :heavy_check_mark:                                                   | N/A                                                                  |