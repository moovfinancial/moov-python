# MerchantRestrictions

Restricts card usage to specific merchants, independent of merchant category.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `mode`                                                                                                 | [components.IssuingControlsRestrictionMode](../../models/components/issuingcontrolsrestrictionmode.md) | :heavy_check_mark:                                                                                     | Whether the listed items should be allowed (`allow`) or blocked (`block`).                             |
| `merchants`                                                                                            | List[[components.MerchantEntry](../../models/components/merchantentry.md)]                             | :heavy_check_mark:                                                                                     | The merchants to allow or block.                                                                       |