# TransferDestination


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `payment_method_id`                                                                                    | *str*                                                                                                  | :heavy_check_mark:                                                                                     | UUID v4                                                                                                | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                   |
| `payment_method_type`                                                                                  | [models.PaymentMethodType](../models/paymentmethodtype.md)                                             | :heavy_check_mark:                                                                                     | The payment method type that represents a payment rail and directionality                              | card-payment                                                                                           |
| `account`                                                                                              | [models.GetTransferPartialAccount](../models/gettransferpartialaccount.md)                             | :heavy_check_mark:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `bank_account`                                                                                         | [OptionalNullable[models.TransferDestinationBankAccount]](../models/transferdestinationbankaccount.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `wallet`                                                                                               | [OptionalNullable[models.TransferDestinationWallet]](../models/transferdestinationwallet.md)           | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `card`                                                                                                 | [OptionalNullable[models.TransferDestinationCard]](../models/transferdestinationcard.md)               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `ach_details`                                                                                          | [OptionalNullable[models.ACHDetailsBase]](../models/achdetailsbase.md)                                 | :heavy_minus_sign:                                                                                     | ACH specific details about the transaction.                                                            |                                                                                                        |
| `apple_pay`                                                                                            | [OptionalNullable[models.TransferDestinationApplePay]](../models/transferdestinationapplepay.md)       | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `card_details`                                                                                         | [OptionalNullable[models.CardDetails]](../models/carddetails.md)                                       | :heavy_minus_sign:                                                                                     | Card-specific details about the transaction.                                                           |                                                                                                        |
| `rtp_details`                                                                                          | [OptionalNullable[models.RTPDetails]](../models/rtpdetails.md)                                         | :heavy_minus_sign:                                                                                     | RTP specific details about the transaction.                                                            |                                                                                                        |
| `__pydantic_extra__`                                                                                   | Dict[str, *Any*]                                                                                       | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |