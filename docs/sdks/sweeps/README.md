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

    res = moov.sweeps.create_config(account_id="2c0dfb65-d7ef-4c8e-8c74-e6c7773550bc", wallet_id="01234567-89ab-cdef-0123-456789abcdef", status=components.SweepConfigStatus.ENABLED, push_payment_method_id="01234567-89ab-cdef-0123-456789abcdef", pull_payment_method_id="01234567-89ab-cdef-0123-456789abcdef")

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

    res = moov.sweeps.list_configs(account_id="5d9d568d-fb5d-478b-a301-d495422f1c35")

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

    res = moov.sweeps.get_config(account_id="12f68c4e-1e8d-483b-9f62-b5d6458d538c", sweep_config_id="ce92235d-dd84-4e14-9895-3b98a0003522")

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

    res = moov.sweeps.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6", wallet_id="21e27667-18d6-4d46-812e-0aee1b9ddf12", skip=60, count=20)

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

    res = moov.sweeps.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", wallet_id="e50f7622-81da-484b-9c66-1c8a99c6b71b", sweep_id="ecd62b8f-7112-4aaf-90ab-4e43b4cca371")

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