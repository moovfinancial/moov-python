# SweepConfigPaymentMethod

The payment method used to push or pull funds to a bank account.
The push payment method can only be ach-credit-standard or ach-credit-same-day. The pull payment method can only be ach-debit-fund.



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `payment_method_id`                                                  | *str*                                                                | :heavy_check_mark:                                                   | UUID v4                                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                 |
| `disabled_on`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |