# GooglePay

## Overview

### Available Operations

* [link_token](#link_token) - Connect a Google Pay token to the specified account.

The `token` data is defined by Google Pay and should be passed through from Google Pay's response unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

## link_token

Connect a Google Pay token to the specified account.

The `token` data is defined by Google Pay and should be passed through from Google Pay's response unmodified.

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

    res = moov.google_pay.link_token(account_id="<id>", token={
        "protocol_version": "ECv2",
        "signature": "<value>",
        "intermediate_signing_key": {
            "signed_key": "<value>",
            "signatures": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "signed_message": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                    | ID of the Moov account representing the cardholder.                                                                                                                                                                                                   |
| `token`                                                                                                                                                                                                                                               | [components.GooglePayToken](../../models/components/googlepaytoken.md)                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                    |   Contains the encrypted payment token as returned from Google Pay.<br/><br/>  Refer to [Google's documentation](https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography#payment-method-token-structure)<br/>  for more information. |
| `retries`                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                   |

### Response

**[operations.LinkGooglePayTokenResponse](../../models/operations/linkgooglepaytokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GenericError       | 400, 409                  | application/json          |
| errors.LinkGooglePayError | 422                       | application/json          |
| errors.APIError           | 4XX, 5XX                  | \*/\*                     |