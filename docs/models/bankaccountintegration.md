# BankAccountIntegration

Describes the account to link to the Moov account.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `holder_name`                                          | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    | Jules Jackson                                          |
| `holder_type`                                          | [models.HolderType](../models/holdertype.md)           | :heavy_check_mark:                                     | The type of holder on a funding source.                |                                                        |
| `account_number`                                       | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    | 0004321567000                                          |
| `bank_account_type`                                    | [models.BankAccountType](../models/bankaccounttype.md) | :heavy_check_mark:                                     | The bank account type.                                 |                                                        |
| `routing_number`                                       | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    | 123456789                                              |