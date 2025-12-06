# Sweeps

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

<!-- UsageSnippet language="python" operationID="createSweepConfig" method="post" path="/accounts/{accountID}/sweep-configs" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.create_config(account_id="cd0ec32e-bd84-418c-90d3-fffbc5465f8b", wallet_id="01234567-89ab-cdef-0123-456789abcdef", status=components.SweepConfigStatus.ENABLED, push_payment_method_id="01234567-89ab-cdef-0123-456789abcdef", pull_payment_method_id="01234567-89ab-cdef-0123-456789abcdef")

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

<!-- UsageSnippet language="python" operationID="listSweepConfigs" method="get" path="/accounts/{accountID}/sweep-configs" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.list_configs(account_id="ed67e4c8-03d3-4d88-ba38-fcd87de45a92")

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

<!-- UsageSnippet language="python" operationID="getSweepConfig" method="get" path="/accounts/{accountID}/sweep-configs/{sweepConfigID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.get_config(account_id="ae1c2e76-3195-4fc8-b922-b7af6dcf1aad", sweep_config_id="bfddff28-5291-4d9b-a0f8-22a0895e8486")

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

<!-- UsageSnippet language="python" operationID="updateSweepConfig" method="patch" path="/accounts/{accountID}/sweep-configs/{sweepConfigID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.update_config(account_id="c16d0264-3e93-4d13-b8d8-6e8e98122631", sweep_config_id="f7943244-882b-4a3a-837a-a58418358399", status=components.Status.DISABLED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `account_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `sweep_config_id`                                                        | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `status`                                                                 | [OptionalNullable[components.Status]](../../models/components/status.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `push_payment_method_id`                                                 | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | N/A                                                                      |
| `pull_payment_method_id`                                                 | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | N/A                                                                      |
| `statement_descriptor`                                                   | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | N/A                                                                      |
| `minimum_balance`                                                        | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | N/A                                                                      |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

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

<!-- UsageSnippet language="python" operationID="listSweeps" method="get" path="/accounts/{accountID}/wallets/{walletID}/sweeps" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.list(account_id="a227b50c-035d-4b7f-932c-a4b7e02aaf5c", wallet_id="d01e5b34-b207-4a5c-b249-6e049be6a841", skip=60, count=20)

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

<!-- UsageSnippet language="python" operationID="getSweep" method="get" path="/accounts/{accountID}/wallets/{walletID}/sweeps/{sweepID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.sweeps.get(account_id="481bc941-34a2-4c2a-a4f8-feaa9a25d630", wallet_id="e63a4638-ad67-44fb-9b59-ed7311023602", sweep_id="c88c9731-06c2-4b4a-a7d2-34c8b936d9ae")

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