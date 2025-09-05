# PayoutRecipient

Specify the intended recipient of the payout.
Either `email` or `phone` must be specified, but not both.

This information will be used to authenticate the end user when they follow the payment link.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `email`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | jordan.lee@classbooker.dev                                                 |
| `phone`                                                                    | [Optional[components.PhoneNumber]](../../models/components/phonenumber.md) | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |