# RequestCardRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The Moov business account for which the card is to be issued.        |
| `request_card`                                                       | [components.RequestCard](../../models/components/requestcard.md)     | :heavy_check_mark:                                                   | N/A                                                                  |
| `x_moov_version`                                                     | [Optional[components.Versions]](../../models/components/versions.md) | :heavy_minus_sign:                                                   | Specify an API version.                                              |