# Fulfillment


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `has_physical_goods`                                       | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        | true                                                       |
| `is_shipping_product`                                      | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        | true                                                       |
| `shipment_duration_days`                                   | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        | 7                                                          |
| `return_policy`                                            | [Optional[models.ReturnPolicy]](../models/returnpolicy.md) | :heavy_minus_sign:                                         | Describes the return policy.                               |                                                            |