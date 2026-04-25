# GooglePayBillingAddress

  Billing address as returned by Google Pay.

  Refer to [Google's documentation](https://developers.google.com/pay/api/web/reference/response-objects#Address)
  for more information.


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `address1`                             | *Optional[str]*                        | :heavy_minus_sign:                     | First line of the street address.      |                                        |
| `address2`                             | *Optional[str]*                        | :heavy_minus_sign:                     | Second line of the street address.     |                                        |
| `address3`                             | *Optional[str]*                        | :heavy_minus_sign:                     | Third line of the street address.      |                                        |
| `locality`                             | *Optional[str]*                        | :heavy_minus_sign:                     | City, town, neighborhood, or suburb.   |                                        |
| `administrative_area`                  | *Optional[str]*                        | :heavy_minus_sign:                     | State, province, or region.            |                                        |
| `postal_code`                          | *Optional[str]*                        | :heavy_minus_sign:                     | Postal or ZIP code.                    |                                        |
| `country_code`                         | *Optional[str]*                        | :heavy_minus_sign:                     | ISO 3166-1 alpha-2 country code.       | US                                     |
| `name`                                 | *Optional[str]*                        | :heavy_minus_sign:                     | Name of the cardholder.                |                                        |
| `phone_number`                         | *Optional[str]*                        | :heavy_minus_sign:                     | Phone number.                          |                                        |
| `sorting_code`                         | *Optional[str]*                        | :heavy_minus_sign:                     | Sorting code (used in some countries). |                                        |