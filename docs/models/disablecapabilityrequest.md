# DisableCapabilityRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `account_id`                                       | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `capability_id`                                    | [models.CapabilityID](../models/capabilityid.md)   | :heavy_check_mark:                                 | Moov account capabilities.                         |
| `x_moov_version`                                   | [Optional[models.Versions]](../models/versions.md) | :heavy_minus_sign:                                 | Specify an API version.                            |