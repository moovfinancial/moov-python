# GooglePay

## Overview

### Available Operations

* [link_token](#link_token) - Connect a Google Pay token to the specified account.

The `paymentMethodData` field should contain the `paymentMethodData` property from Google Pay's
[PaymentData](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) response,
passed through unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

## link_token

Connect a Google Pay token to the specified account.

The `paymentMethodData` field should contain the `paymentMethodData` property from Google Pay's
[PaymentData](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) response,
passed through unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="linkGooglePayToken" method="post" path="/accounts/{accountID}/google-pay/tokens" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.google_pay.link_token(account_id="<id>", merchant_account_id="c5f78a7e-2fb0-4e4a-bcf0-9e1f8b0e5c7a", payment_method_data={
        "type": components.Type.CARD,
        "info": {
            "card_network": components.CardNetwork.VISA,
            "card_details": "1234",
            "card_funding_source": components.CardFundingSource.DEBIT,
            "billing_address": {
                "country_code": "US",
            },
        },
        "tokenization_data": {
            "type": components.GooglePayTokenizationDataType.PAYMENT_GATEWAY,
            "token": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | ID of the Moov account representing the cardholder.                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `merchant_account_id`                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                |   The merchant accountID this token was minted for. Must match the `gatewayMerchantId`<br/>  value passed to Google Pay when constructing the PaymentDataRequest. card-gateway validates<br/>  that the decrypted `gatewayMerchantId` matches this value. | c5f78a7e-2fb0-4e4a-bcf0-9e1f8b0e5c7a                                                                                                                                                                                                              |
| `payment_method_data`                                                                                                                                                                                                                             | [components.GooglePayPaymentMethodData](../../models/components/googlepaypaymentmethoddata.md)                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                |   The `paymentMethodData` object from Google Pay's<br/>  [PaymentData](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) response.                                                                                |                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[operations.LinkGooglePayTokenResponse](../../models/operations/linkgooglepaytokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GenericError       | 400, 409                  | application/json          |
| errors.LinkGooglePayError | 422                       | application/json          |
| errors.APIError           | 4XX, 5XX                  | \*/\*                     |