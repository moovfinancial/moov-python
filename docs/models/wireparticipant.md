# WireParticipant

Financial institution information regarding a wire participant


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `routing_number`                                           | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | 123456789                                                  |
| `telegraphic_name`                                         | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | MN STR BNK                                                 |
| `customer_name`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | Main Street Bank                                           |
| `location`                                                 | [Optional[models.WireLocation]](../models/wirelocation.md) | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `funds_transfer_status`                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | Y                                                          |
| `funds_settlement_only_status`                             | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `book_entry_securities_transfer_status`                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | Y                                                          |
| `date_`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | 20000222                                                   |