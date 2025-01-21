# Profile

Describes a Moov account profile. A profile will have a business or an individual, depending on the account's type.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `individual`                                                         | [Optional[models.IndividualProfile]](../models/individualprofile.md) | :heavy_minus_sign:                                                   | Describes an individual.                                             |
| `business`                                                           | [Optional[models.BusinessProfile]](../models/businessprofile.md)     | :heavy_minus_sign:                                                   | Describes a business.                                                |