# PartnerRiskOutcomesResponse

The risk rules that contributed to a transfer's risk decision.

This information has limited availability and must be enabled for your account by Moov.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `transfer_id`                                                                              | *str*                                                                                      | :heavy_check_mark:                                                                         | Identifier of the transfer these outcomes belong to.                                       |
| `contributing_rules`                                                                       | List[[components.ContributingRule](../../models/components/contributingrule.md)]           | :heavy_check_mark:                                                                         | The risk rules that contributed to the decision. May be empty when no rules are disclosed. |