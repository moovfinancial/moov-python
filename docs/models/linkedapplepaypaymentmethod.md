# LinkedApplePayPaymentMethod


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `payment_method_id`                                                       | *str*                                                                     | :heavy_check_mark:                                                        | The new payment method's ID.                                              |
| `payment_method_type`                                                     | [models.PaymentMethodType](../models/paymentmethodtype.md)                | :heavy_check_mark:                                                        | The payment method type that represents a payment rail and directionality |
| `apple_pay`                                                               | [models.ApplePayResponse](../models/applepayresponse.md)                  | :heavy_check_mark:                                                        | Describes an Apple Pay token on a Moov account.                           |