# DisputeCreated


## Fields

| Field                                                                                                                                                                                                 | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           | Example                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | ID of the merchant's Account associated with the disputed transaction.                                                                                                                                |                                                                                                                                                                                                       |
| `transfer_id`                                                                                                                                                                                         | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | ID of the disputed transfer.                                                                                                                                                                          |                                                                                                                                                                                                       |
| `transaction_id`                                                                                                                                                                                      | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | ID of the disputed transaction.                                                                                                                                                                       |                                                                                                                                                                                                       |
| `dispute_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | ID of the dispute.                                                                                                                                                                                    |                                                                                                                                                                                                       |
| `status`                                                                                                                                                                                              | [models.DisputeStatus](../models/disputestatus.md)                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                    | The status of a particular dispute. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/#dispute-statuses) to learn what each status means. | response-needed                                                                                                                                                                                       |
| `phase`                                                                                                                                                                                               | [models.DisputePhase](../models/disputephase.md)                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                    | The phase of a particular dispute.                                                                                                                                                                    | pre-dispute                                                                                                                                                                                           |