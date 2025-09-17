# Profile

Describes a Moov account profile. A profile will have a business, individual, or guest depending on the account's type.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `individual`                                                                           | [Optional[components.IndividualProfile]](../../models/components/individualprofile.md) | :heavy_minus_sign:                                                                     | Describes an individual.                                                               |
| `business`                                                                             | [Optional[components.BusinessProfile]](../../models/components/businessprofile.md)     | :heavy_minus_sign:                                                                     | Describes a business.                                                                  |
| `guest`                                                                                | [Optional[components.GuestProfile]](../../models/components/guestprofile.md)           | :heavy_minus_sign:                                                                     | Describes a guest account profile.                                                     |