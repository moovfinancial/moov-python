# PatchSweepConfigRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `sweep_config_id`                                                          | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `patch_sweep_config`                                                       | [components.PatchSweepConfig](../../models/components/patchsweepconfig.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `x_moov_version`                                                           | [Optional[components.Versions]](../../models/components/versions.md)       | :heavy_minus_sign:                                                         | Specify an API version.                                                    |