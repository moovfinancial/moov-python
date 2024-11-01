# CreateProfile

Describes the fields available when creating a profile.
If `accountType` is set to `individual`, the `individual` object should be completed. All others should populate `business`.



## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `individual`                                                                             | [OptionalNullable[models.CreateProfileIndividual]](../models/createprofileindividual.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `business`                                                                               | [OptionalNullable[models.CreateProfileBusiness]](../models/createprofilebusiness.md)     | :heavy_minus_sign:                                                                       | N/A                                                                                      |