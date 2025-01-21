# ListPartnerPricingAgreementsRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `x_moov_version`                                                           | [Optional[models.Versions]](../models/versions.md)                         | :heavy_minus_sign:                                                         | Specify an API version.                                                    |
| `agreement_id`                                                             | List[*str*]                                                                | :heavy_minus_sign:                                                         | A comma-separated list of agreement IDs to filter the results by.          |
| `status`                                                                   | List[[models.FeePlanAgreementStatus](../models/feeplanagreementstatus.md)] | :heavy_minus_sign:                                                         | A comma-separated list of statuses to filter the results by.               |