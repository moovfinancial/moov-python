# PaymentMethods
(*payment_methods*)

## Overview

### Available Operations

* [list](#list) - Retrieve a list of payment methods associated with a Moov account. Read our [payment methods 
guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.
* [get](#get) - Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

## list

Retrieve a list of payment methods associated with a Moov account. Read our [payment methods 
guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components

with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.payment_methods.list(account_id="062d9768-0375-4e19-a48f-00ae75251086")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |
| `source_id`                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional parameter to filter the account's payment methods by source ID. <br/><br/>A source ID can be a [walletID](https://docs.moov.io/api/sources/wallets/list/), [cardID](https://docs.moov.io/api/sources/cards/list/), <br/>or [bankAccountID](https://docs.moov.io/api/sources/bank-accounts/list/). |
| `payment_method_type`                                                                                                                                                                                                                                                                          | [Optional[components.PaymentMethodType]](../../models/components/paymentmethodtype.md)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional parameter to filter the account's payment methods by payment method type.                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |

### Response

**[operations.ListPaymentMethodsResponse](../../models/operations/listpaymentmethodsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components

with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.payment_methods.get(account_id="dec1e9d0-b795-4449-824a-127444ae0d75", payment_method_id="e4f6d969-b108-405e-b95a-d71e917fb15e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `payment_method_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetPaymentMethodResponse](../../models/operations/getpaymentmethodresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |