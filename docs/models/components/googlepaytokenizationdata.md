# GooglePayTokenizationData

  Contains the encrypted payment token from Google Pay.

  The `token` field is a JSON-encoded string containing the ECv2 encrypted payment token.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `type`                                                                                               | [components.GooglePayTokenizationDataType](../../models/components/googlepaytokenizationdatatype.md) | :heavy_check_mark:                                                                                   | The tokenization type. Always `PAYMENT_GATEWAY`.                                                     | PAYMENT_GATEWAY                                                                                      |
| `token`                                                                                              | *str*                                                                                                | :heavy_check_mark:                                                                                   | The ECv2 encrypted payment token, as a JSON-encoded string.                                          |                                                                                                      |