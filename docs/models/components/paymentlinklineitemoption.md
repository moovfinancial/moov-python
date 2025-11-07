# PaymentLinkLineItemOption

Represents a modifier or option applied to a line item.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | The name of the option or modifier.                                                     |
| `quantity`                                                                              | *int*                                                                                   | :heavy_check_mark:                                                                      | The quantity of this option.                                                            |
| `price_modifier`                                                                        | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md)          | :heavy_minus_sign:                                                                      | Optional price modification applied by this option. Can be positive, negative, or zero. |
| `group`                                                                                 | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional group identifier to categorize related options (e.g., 'toppings').             |