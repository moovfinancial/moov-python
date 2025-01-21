# CreateTransferDestination

The final stage of a transfer and the ultimate recipient of the funds.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `payment_method_id`                                                                          | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `card_details`                                                                               | [Optional[models.CreateTransferDestinationCard]](../models/createtransferdestinationcard.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `ach_details`                                                                                | [Optional[models.CreateTransferDestinationACH]](../models/createtransferdestinationach.md)   | :heavy_minus_sign:                                                                           | N/A                                                                                          |