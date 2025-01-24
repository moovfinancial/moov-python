# IssuingControls


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `single_use`                                                                                 | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Indicates if the card is single-use. If true, the card closes after the first authorization. |
| `velocity_limits`                                                                            | List[[components.IssuingVelocityLimit](../../models/components/issuingvelocitylimit.md)]     | :heavy_minus_sign:                                                                           | Sets the spending limit per time interval. Only one limit per interval is supported.         |