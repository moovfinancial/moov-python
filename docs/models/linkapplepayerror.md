# LinkApplePayError


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `error`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Describes an error that wasn't attributable to a single request field.     |
| `payment_data`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Describes an error within the `token.paymentData` request field.           |
| `payment_method`                                                           | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Describes an error within the `token.paymentMethod` request field.         |
| `transaction_identifier`                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Describes an error within the `token.transactionIdentifier` request field. |