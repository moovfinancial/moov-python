# UpdateCheckoutRequest

Request to update a checkout.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `expires_on`                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                         | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `display`                                                                                    | [Optional[models.Display]](../models/display.md)                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `customer`                                                                                   | [Optional[models.Customer]](../models/customer.md)                                           | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `payment`                                                                                    | [Optional[models.Payment]](../models/payment.md)                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `transfer`                                                                                   | [Optional[models.UpdateCheckoutRequestTransfer]](../models/updatecheckoutrequesttransfer.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |