# WebhookDataSweepUpdated


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `account_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | The accountID associated with the wallet being swept.            |
| `wallet_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `sweep_id`                                                       | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `transfer_id`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `status`                                                         | [components.SweepStatus](../../models/components/sweepstatus.md) | :heavy_check_mark:                                               | N/A                                                              |