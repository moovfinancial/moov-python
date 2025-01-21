# ListFeePlansRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `account_id`                                                 | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `x_moov_version`                                             | [Optional[models.Versions]](../models/versions.md)           | :heavy_minus_sign:                                           | Specify an API version.                                      |
| `plan_i_ds`                                                  | List[*str*]                                                  | :heavy_minus_sign:                                           | A comma-separated list of plan IDs to filter the results by. |