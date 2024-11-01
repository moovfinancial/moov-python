# SweepUpdated


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `sweep_id`                                     | *str*                                          | :heavy_check_mark:                             | ID of the sweep                                |                                                |
| `wallet_id`                                    | *str*                                          | :heavy_check_mark:                             | ID of the Wallet                               |                                                |
| `status`                                       | [models.SweepStatus](../models/sweepstatus.md) | :heavy_check_mark:                             | Current status of the sweep.                   | accruing                                       |
| `transfer_id`                                  | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | ID of the transfer                             |                                                |