# CreateACHDetailsBase

If transfer involves ACH, override default card acceptance properties.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `company_entry_description`                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional override of the default NACHA company entry description for a transfer. | Gym Dues                                                                            |
| `originating_company_name`                                                          | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional override of the default NACHA company name for a transfer.              | Whole Body Fit                                                                      |