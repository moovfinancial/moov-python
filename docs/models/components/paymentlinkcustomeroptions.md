# PaymentLinkCustomerOptions


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `require_address`                                                                   | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | If true, a billing address is required when completing the payment form.            |
| `require_phone`                                                                     | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | If true, a phone number is required when completing the payment form.               |
| `metadata`                                                                          | Dict[str, *str*]                                                                    | :heavy_minus_sign:                                                                  | Optional free-form metadata for the Moov account that will represent this customer. |