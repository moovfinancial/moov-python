# Underwriting

Describes underwriting values (in USD) used for card payment acceptance.


## Fields

| Field                                                                                                                                                                                      | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `average_transaction_size`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        | 10000                                                                                                                                                                                      |
| `max_transaction_size`                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        | 50000                                                                                                                                                                                      |
| `average_monthly_transaction_volume`                                                                                                                                                       | *Optional[int]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        | 250000                                                                                                                                                                                     |
| ~~`status`~~                                                                                                                                                                               | [Optional[models.UnderwritingStatus]](../models/underwritingstatus.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated and will be removed in a future release. |                                                                                                                                                                                            |
| `volume_by_customer_type`                                                                                                                                                                  | [Optional[models.VolumeByCustomerType]](../models/volumebycustomertype.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `card_volume_distribution`                                                                                                                                                                 | [Optional[models.CardVolumeDistribution]](../models/cardvolumedistribution.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `fulfillment`                                                                                                                                                                              | [Optional[models.Fulfillment]](../models/fulfillment.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |