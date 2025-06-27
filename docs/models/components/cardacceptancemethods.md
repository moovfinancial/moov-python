# CardAcceptanceMethods

Describes the distribution of card transactions by payment method.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `in_person_percentage`                                                                               | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | Percentage of card transactions that are in-person payments. Minimum value is 0, maximum is 100.     |
| `mail_or_phone_percentage`                                                                           | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | Percentage of card transactions that are mail or phone payments. Minimum value is 0, maximum is 100. |
| `online_percentage`                                                                                  | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | Percentage of card transactions that are online payments. Minimum value is 0, maximum is 100.        |