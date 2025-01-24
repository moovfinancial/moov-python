# OnboardingPartnerAccount

The account that created the onboarding invite.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `account_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | The account ID of the partner that created the invite.             |                                                                    |
| `account_mode`                                                     | [components.Mode](../../models/components/mode.md)                 | :heavy_check_mark:                                                 | The operating mode for an account.                                 | production                                                         |
| `display_name`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The name of the Moov account used to create the onboarding invite. | Bob's Widgets                                                      |