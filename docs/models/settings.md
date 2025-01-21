# Settings

User provided settings to manage an account.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `card_payment`                                                                                   | [Optional[models.CardPaymentSettings]](../models/cardpaymentsettings.md)                         | :heavy_minus_sign:                                                                               | User provided settings to manage card payments. This data is only allowed on a business account. |
| `ach_payment`                                                                                    | [Optional[models.ACHPaymentSettings]](../models/achpaymentsettings.md)                           | :heavy_minus_sign:                                                                               | N/A                                                                                              |