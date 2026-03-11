# ResolutionLinkRecipient

Contact information for the recipient of a resolution link. Provide either `email` or `phone`, but not both.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `email`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The email address of the recipient.                                        | jordan.lee@classbooker.dev                                                 |
| `phone`                                                                    | [Optional[components.PhoneNumber]](../../models/components/phonenumber.md) | :heavy_minus_sign:                                                         | The phone number of the recipient.                                         |                                                                            |