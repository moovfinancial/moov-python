# PaymentMethods
(*payment_methods*)

## Overview

[Payment methods](https://docs.moov.io/guides/money-movement/payment-methods/) represent all of the ways an account can move funds to another Moov account. Payment methods are generated programmatically when a card or bank account is added or the status is updated e.g., `ach-debit-fund` will be added as a payment method once the bank account is verified.

<em>RTP® and Push to Card are not yet generally available on Moov. Contact us for more information.</em>


### Available Operations

* [get_payment_methods](#get_payment_methods) - List payment methods
* [get_payment_method](#get_payment_method) - Get payment method

## get_payment_methods

Retrieve a list of payment methods associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.payment_methods.get_payment_methods(account_id="3e369c12-7be2-4ee2-8563-824667af5939", source_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", payment_method_type=moov.PaymentMethodType.CARD_PAYMENT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                          | ID of the account.                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                             |
| `source_id`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Optional parameter to filter the account's payment methods by source ID. A source ID can be a [walletID](https://docs.moov.io/api/sources/wallets/list/), [cardID](https://docs.moov.io/api/sources/cards/list/), or [bankAccountID](https://docs.moov.io/api/sources/bank-accounts/list/). | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                                                                        |
| `payment_method_type`                                                                                                                                                                                                                                                                       | [Optional[models.PaymentMethodType]](../../models/paymentmethodtype.md)                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Optional parameter to filter the account's payment methods by payment method type.                                                                                                                                                                                                          | card-payment                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                             |

### Response

**[models.GetPaymentMethodsResponse](../../models/getpaymentmethodsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_method

Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.payment_methods.get_payment_method(account_id="dec1e9d0-b795-4449-824a-127444ae0d75", payment_method_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `account_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | ID of the account.                                                                |                                                                                   |
| `payment_method_id`                                                               | *str*                                                                             | :heavy_check_mark:                                                                | ID of the payment method. Can be one of `walletID`, `cardID`, or `bankAccountID`. | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                              |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |

### Response

**[models.GetPaymentMethodResponse](../../models/getpaymentmethodresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |