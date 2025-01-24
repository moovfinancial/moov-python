# UpdateIssuedCardRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | The Moov business account for which the card was issued.                   |
| `issued_card_id`                                                           | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `update_issued_card`                                                       | [components.UpdateIssuedCard](../../models/components/updateissuedcard.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `x_moov_version`                                                           | [Optional[components.Versions]](../../models/components/versions.md)       | :heavy_minus_sign:                                                         | Specify an API version.                                                    |