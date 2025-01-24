# PaymentMethods
(*payment_methods*)

## Overview

### Available Operations

* [list_payment_methods](#list_payment_methods) - Retrieve a list of payment methods associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_payment_method](#get_payment_method) - Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## list_payment_methods

Retrieve a list of payment methods associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.payment_methods.list_payment_methods(security=operations.ListPaymentMethodsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="062d9768-0375-4e19-a48f-00ae75251086")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                                  | [operations.ListPaymentMethodsSecurity](../../models/operations/listpaymentmethodssecurity.md)                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                         |
| `x_moov_version`                                                                                                                                                                                                                                                                            | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Specify an API version.                                                                                                                                                                                                                                                                     |
| `source_id`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Optional parameter to filter the account's payment methods by source ID. A source ID can be a [walletID](https://docs.moov.io/api/sources/wallets/list/), [cardID](https://docs.moov.io/api/sources/cards/list/), or [bankAccountID](https://docs.moov.io/api/sources/bank-accounts/list/). |
| `payment_method_type`                                                                                                                                                                                                                                                                       | [Optional[components.PaymentMethodType]](../../models/components/paymentmethodtype.md)                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Optional parameter to filter the account's payment methods by payment method type.                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                         |

### Response

**[List[components.PaymentMethod]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_payment_method

Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.payment_methods.get_payment_method(security=operations.GetPaymentMethodSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="dec1e9d0-b795-4449-824a-127444ae0d75", payment_method_id="e4f6d969-b108-405e-b95a-d71e917fb15e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [operations.GetPaymentMethodSecurity](../../models/operations/getpaymentmethodsecurity.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `account_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `payment_method_id`                                                                        | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `x_moov_version`                                                                           | [Optional[components.Versions]](../../models/components/versions.md)                       | :heavy_minus_sign:                                                                         | Specify an API version.                                                                    |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[components.PaymentMethod](../../models/components/paymentmethod.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |