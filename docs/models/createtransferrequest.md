# CreateTransferRequest


## Fields

| Field                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_idempotency_key`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | Prevents duplicate transfers from being created. Note that we only accept UUID v4.                                                                                                                                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                                   |
| `create_transfer`                                                                                                                                                                                                                                      | [models.CreateTransfer](../models/createtransfer.md)                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |
| `x_wait_for`                                                                                                                                                                                                                                           | [Optional[models.WaitFor]](../models/waitfor.md)                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                        |