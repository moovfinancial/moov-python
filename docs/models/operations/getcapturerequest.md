# GetCaptureRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `account_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | Moov account ID of an authorized partner or the transfer's source or destination. |
| `transfer_id`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | Identifier for the auth-capture `card-payment` transfer.                          |
| `capture_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | Identifier for the capture.                                                       |