# PartnerAccount

The account that created the onboarding invite.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The unique identifier for the account that created the onboarding invite.<br/> | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                       |
| `account_mode`                                                             | [Optional[models.Mode]](../models/mode.md)                                 | :heavy_minus_sign:                                                         | The mode this account is allowed to be used within.                        | production                                                                 |
| `display_name`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The name of the Moov account used to create the onboarding invite.<br/>    | Bob's Widgets                                                              |