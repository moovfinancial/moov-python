# GooglePayAssuranceDetails

3-D Secure assurance details from Google Pay.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `card_holder_authenticated`                                            | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Whether the card is verified via 3-D Secure authentication.            |
| `account_verified`                                                     | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Whether the returned payment credential can be used for a transaction. |