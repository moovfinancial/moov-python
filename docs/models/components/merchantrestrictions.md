# MerchantRestrictions

Restricts card usage to specific merchants, independent of merchant category.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `mode`                                                                                                 | [components.IssuingControlsRestrictionMode](../../models/components/issuingcontrolsrestrictionmode.md) | :heavy_check_mark:                                                                                     | Whether the listed merchants are the only ones allowed, or the ones to block.                          |
| `merchants`                                                                                            | List[[components.MerchantEntry](../../models/components/merchantentry.md)]                             | :heavy_check_mark:                                                                                     | The merchants to allow or block.                                                                       |