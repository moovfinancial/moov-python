# GetTransferRequest


## Fields

| Field                                                                                                                                        | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer_id`                                                                                                                                | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Identifier for the transfer.                                                                                                                 |
| `account_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account. |