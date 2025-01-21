# PaymentLinkPaymentDetailsUpdate

Options for payment links used to collect payment.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `allowed_methods`                                                                    | List[[models.CollectionPaymentMethodType](../models/collectionpaymentmethodtype.md)] | :heavy_minus_sign:                                                                   | A list of payment methods that should be supported for this payment link.            |
| `card_details`                                                                       | [Optional[models.CardPaymentDetails]](../models/cardpaymentdetails.md)               | :heavy_minus_sign:                                                                   | Options for payment links used to collect a card payment.                            |
| `ach_details`                                                                        | [Optional[models.ACHPaymentDetails]](../models/achpaymentdetails.md)                 | :heavy_minus_sign:                                                                   | Options for payment links used to collect an ACH payment.                            |