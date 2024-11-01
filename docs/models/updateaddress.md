# UpdateAddress

Provide address fields as necessary to patch the currently saved address. 
Omit any fields that should not be changed.



## Fields

| Field                   | Type                    | Required                | Description             | Example                 |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `address_line1`         | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | 123 Main Street         |
| `address_line2`         | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | Apt 302                 |
| `city`                  | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | Boulder                 |
| `state_or_province`     | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | CO                      |
| `postal_code`           | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | 80301                   |
| `country`               | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     | US                      |