# ListIssuedCardAuthorizationEventsRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `account_id`                                                | *str*                                                       | :heavy_check_mark:                                          | The Moov business account for which cards have been issued. |                                                             |
| `authorization_id`                                          | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |                                                             |
| `skip`                                                      | *Optional[int]*                                             | :heavy_minus_sign:                                          | N/A                                                         | 60                                                          |
| `count`                                                     | *Optional[int]*                                             | :heavy_minus_sign:                                          | N/A                                                         | 20                                                          |