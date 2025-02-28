# Sweeps
(*sweeps*)

## Overview

### Available Operations

* [create_config](#create_config) - Create a sweep config for a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.
* [list_configs](#list_configs) - List sweep configs associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get_config](#get_config) - Get a sweep config associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [update_config](#update_config) - Update settings on a sweep config.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.
* [list](#list) - List sweeps associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](#get) - Get details on a specific sweep.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

## create_config

Create a sweep config for a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.

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

    res = moov.sweeps.create_config(account_id="3a373e85-2777-40fe-aacd-52d6fc641d76", wallet_id="01234567-89ab-cdef-0123-456789abcdef", status=components.SweepConfigStatus.ENABLED, push_payment_method_id="01234567-89ab-cdef-0123-456789abcdef", pull_payment_method_id="01234567-89ab-cdef-0123-456789abcdef")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                       | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `wallet_id`                                                                                                                                                     | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `status`                                                                                                                                                        | [components.SweepConfigStatus](../../models/components/sweepconfigstatus.md)                                                                                    | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `push_payment_method_id`                                                                                                                                        | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `pull_payment_method_id`                                                                                                                                        | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `statement_descriptor`                                                                                                                                          | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | The text that appears on the banking statement. The default descriptor is a 10 character ID if an override is not set in the sweep configs statementDescriptor. |
| `minimum_balance`                                                                                                                                               | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `retries`                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                | :heavy_minus_sign:                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                             |

### Response

**[operations.CreateSweepConfigResponse](../../models/operations/createsweepconfigresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GenericError           | 400, 409                      | application/json              |
| errors.CreateSweepConfigError | 422                           | application/json              |
| errors.APIError               | 4XX, 5XX                      | \*/\*                         |

## list_configs

List sweep configs associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

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

    res = moov.sweeps.list_configs(account_id="b06d7726-4020-4fef-9035-75779c0fc48c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListSweepConfigsResponse](../../models/operations/listsweepconfigsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_config

Get a sweep config associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

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

    res = moov.sweeps.get_config(account_id="1f4428ca-3d11-441b-93d5-3fada6a5db01", sweep_config_id="acef9550-4b7b-4675-807b-71755d182b2f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sweep_config_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSweepConfigResponse](../../models/operations/getsweepconfigresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_config

Update settings on a sweep config.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.

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

    res = moov.sweeps.update_config(account_id="7573cb48-6325-4d3d-841d-81108fcfe6f2", sweep_config_id="49e8f3b1-259f-458e-9367-adb3b938f8c8", status=components.Status.DISABLED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `sweep_config_id`                                                                                  | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `status`                                                                                           | [OptionalNullable[components.Status]](../../models/components/status.md)                           | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `push_payment_method_id`                                                                           | [OptionalNullable[components.PushPaymentMethodID]](../../models/components/pushpaymentmethodid.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `pull_payment_method_id`                                                                           | [OptionalNullable[components.PullPaymentMethodID]](../../models/components/pullpaymentmethodid.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `statement_descriptor`                                                                             | [OptionalNullable[components.StatementDescriptor]](../../models/components/statementdescriptor.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `minimum_balance`                                                                                  | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateSweepConfigResponse](../../models/operations/updatesweepconfigresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.PatchSweepConfigError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list

List sweeps associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

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

    res = moov.sweeps.list(account_id="0fe45272-ee0d-401f-a10e-21e396676598", wallet_id="5f738f67-1989-4589-beb1-3d2f5c53a821", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `wallet_id`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `skip`                                                                     | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | 60                                                                         |
| `count`                                                                    | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | 20                                                                         |
| `status`                                                                   | [Optional[components.SweepStatus]](../../models/components/sweepstatus.md) | :heavy_minus_sign:                                                         | Optional parameter to filter by sweep status.                              |                                                                            |
| `statement_descriptor`                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Optional string to filter by statement descriptor.                         |                                                                            |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[operations.ListSweepsResponse](../../models/operations/listsweepsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get details on a specific sweep.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

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

    res = moov.sweeps.get(account_id="adb697e6-2888-48b9-b2c5-f2c3d487add5", wallet_id="9f00e2b3-9dfb-48a3-9a25-a08e80f9cf36", sweep_id="a5324f55-fbec-4323-94e4-c512608bb175")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sweep_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSweepResponse](../../models/operations/getsweepresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |