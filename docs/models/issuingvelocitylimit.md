# IssuingVelocityLimit


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `amount`                                                                                         | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | The maximum amount in cents that can be spent in a given interval.                               |
| `interval`                                                                                       | [Optional[models.IssuingIntervalLimit]](../models/issuingintervallimit.md)                       | :heavy_minus_sign:                                                                               | Specifies the time frame for the velocity limit. Currently supports only per-transaction limits. |