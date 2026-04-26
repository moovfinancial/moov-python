# LinkedGooglePayPaymentMethod


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `payment_method_id`                                                          | *str*                                                                        | :heavy_check_mark:                                                           | The new payment method's ID.                                                 |
| `payment_method_type`                                                        | [components.PaymentMethodType](../../models/components/paymentmethodtype.md) | :heavy_check_mark:                                                           | The payment method type that represents a payment rail and directionality    |
| `google_pay`                                                                 | [components.GooglePayResponse](../../models/components/googlepayresponse.md) | :heavy_check_mark:                                                           | Describes a Google Pay token on a Moov account.                              |