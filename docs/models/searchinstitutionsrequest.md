# SearchInstitutionsRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `rail`                                     | [models.Rail](../models/rail.md)           | :heavy_check_mark:                         | Payment rail to search on                  |                                            |
| `name`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Name of the financial institution          | Farmers                                    |
| `routing_number`                           | *Optional[str]*                            | :heavy_minus_sign:                         | Routing number for a financial institution | 044112187                                  |
| `state`                                    | *Optional[str]*                            | :heavy_minus_sign:                         | Optional parameters to filter results      | IA                                         |
| `limit`                                    | *Optional[int]*                            | :heavy_minus_sign:                         | Maximum results returned by a search       | 499                                        |