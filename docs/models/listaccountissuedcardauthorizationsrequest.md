# ListAccountIssuedCardAuthorizationsRequest


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | ID of the account.                                                                                        |                                                                                                           |
| `issued_card_id`                                                                                          | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Optional ID of the issued card to filter results.                                                         | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                      |
| `start_date_time`                                                                                         | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Optional date-time which inclusively filters all authorizations created after this date-time.             | 2009-11-10T23:00:00Z                                                                                      |
| `end_date_time`                                                                                           | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Optional date-time which exclusively filters all authorizations created before this date-time.            | 2009-11-13T01:00:00Z                                                                                      |
| `statuses`                                                                                                | [Optional[models.IssuedCardAuthorizationStatus]](../models/issuedcardauthorizationstatus.md)              | :heavy_minus_sign:                                                                                        | Optional, comma-separated statuses of the authorization to filter results. For example `declined,expired` | declined                                                                                                  |
| `count`                                                                                                   | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Optional parameter to limit the number of results in the query.                                           | 10                                                                                                        |
| `skip`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | The number of items to offset before starting to collect the result set.                                  | 10                                                                                                        |