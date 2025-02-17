# PatchProfile

Describes the fields available when patching a profile.
Each object can be patched independent of patching the other fields.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `individual`                                                                       | [Optional[components.PatchIndividual]](../../models/components/patchindividual.md) | :heavy_minus_sign:                                                                 | Describes the fields available when patching an individual.                        |
| `business`                                                                         | [Optional[components.PatchBusiness]](../../models/components/patchbusiness.md)     | :heavy_minus_sign:                                                                 | N/A                                                                                |