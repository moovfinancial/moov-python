# UpdateCardRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `account_id`                                       | *str*                                              | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `card_id`                                          | *str*                                              | :heavy_check_mark:                                 | N/A                                                | 01234567-89ab-cdef-0123-456789abcdef               |
| `update_card`                                      | [models.UpdateCard](../models/updatecard.md)       | :heavy_check_mark:                                 | N/A                                                | {<br/>"cardCvv": "456"<br/>}                       |
| `x_moov_version`                                   | [Optional[models.Versions]](../models/versions.md) | :heavy_minus_sign:                                 | Specify an API version.                            |                                                    |