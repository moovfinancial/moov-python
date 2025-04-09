# MoovFee

Moov fee charged to an account involved in a transfer.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `account_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | ID of the account that fees were charged to.                                          |
| `transfer_party`                                                                      | [components.TransferParty](../../models/components/transferparty.md)                  | :heavy_check_mark:                                                                    | Indicates whether the account charged is the source, destination, or partner account. |
| `total_amount`                                                                        | [components.AmountDecimal](../../models/components/amountdecimal.md)                  | :heavy_check_mark:                                                                    | The total amount of fees charged to the account.                                      |
| `fee_i_ds`                                                                            | List[*str*]                                                                           | :heavy_check_mark:                                                                    | List of fee IDs that sum to the totalAmount.                                          |