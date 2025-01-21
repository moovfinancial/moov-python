# Sweeps
(*sweeps*)

## Overview

### Available Operations

* [create_sweep_config](#create_sweep_config) - Create a sweep config for a wallet.
* [list_sweep_configs](#list_sweep_configs) - List sweep configs associated with an account.
* [get_sweep_config](#get_sweep_config) - Get a sweep config associated with a wallet.
* [patch_sweep_config](#patch_sweep_config) - Update settings on a sweep config.
* [list_sweeps](#list_sweeps) - List sweeps associated with a wallet.
* [get_sweep](#get_sweep) - Get details on a specific sweep.

## create_sweep_config

Create a sweep config for a wallet.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.create_sweep_config(security=moov.CreateSweepConfigSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="3a373e85-2777-40fe-aacd-52d6fc641d76", wallet_id="01234567-89ab-cdef-0123-456789abcdef", status=moov.SweepConfigStatus.ENABLED, push_payment_method_id="01234567-89ab-cdef-0123-456789abcdef", pull_payment_method_id="01234567-89ab-cdef-0123-456789abcdef")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                       | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                      | [models.CreateSweepConfigSecurity](../../models/createsweepconfigsecurity.md)                                                                                   | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `account_id`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `wallet_id`                                                                                                                                                     | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `status`                                                                                                                                                        | [models.SweepConfigStatus](../../models/sweepconfigstatus.md)                                                                                                   | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `push_payment_method_id`                                                                                                                                        | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `pull_payment_method_id`                                                                                                                                        | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `x_moov_version`                                                                                                                                                | [Optional[models.Versions]](../../models/versions.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                              | Specify an API version.                                                                                                                                         |
| `statement_descriptor`                                                                                                                                          | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | The text that appears on the banking statement. The default descriptor is a 10 character ID if an override is not set in the sweep configs statementDescriptor. |
| `minimum_balance`                                                                                                                                               | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `retries`                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                | :heavy_minus_sign:                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                             |

### Response

**[models.SweepConfig](../../models/sweepconfig.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.GenericError           | 400, 409                      | application/json              |
| models.CreateSweepConfigError | 422                           | application/json              |
| models.APIError               | 4XX, 5XX                      | \*/\*                         |

## list_sweep_configs

List sweep configs associated with an account.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.list_sweep_configs(security=moov.ListSweepConfigsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="b06d7726-4020-4fef-9035-75779c0fc48c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.ListSweepConfigsSecurity](../../models/listsweepconfigssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `account_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `x_moov_version`                                                            | [Optional[models.Versions]](../../models/versions.md)                       | :heavy_minus_sign:                                                          | Specify an API version.                                                     |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.SweepConfig]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_sweep_config

Get a sweep config associated with a wallet.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.get_sweep_config(security=moov.GetSweepConfigSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="1f4428ca-3d11-441b-93d5-3fada6a5db01", sweep_config_id="acef9550-4b7b-4675-807b-71755d182b2f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetSweepConfigSecurity](../../models/getsweepconfigsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `account_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `sweep_config_id`                                                       | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `x_moov_version`                                                        | [Optional[models.Versions]](../../models/versions.md)                   | :heavy_minus_sign:                                                      | Specify an API version.                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SweepConfig](../../models/sweepconfig.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_sweep_config

Update settings on a sweep config.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.patch_sweep_config(security=moov.PatchSweepConfigSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="c0ee091a-5b72-49c9-9c8b-7cb99d7f9309", sweep_config_id="c1f1c60c-cb13-4bc6-891c-f34d96682f06", status=moov.SweepConfigStatus.DISABLED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                       | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                      | [models.PatchSweepConfigSecurity](../../models/patchsweepconfigsecurity.md)                                                                                     | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `account_id`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `sweep_config_id`                                                                                                                                               | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `x_moov_version`                                                                                                                                                | [Optional[models.Versions]](../../models/versions.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                              | Specify an API version.                                                                                                                                         |
| `status`                                                                                                                                                        | [Optional[models.SweepConfigStatus]](../../models/sweepconfigstatus.md)                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `push_payment_method_id`                                                                                                                                        | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `pull_payment_method_id`                                                                                                                                        | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | ID of the payment method.                                                                                                                                       |
| `statement_descriptor`                                                                                                                                          | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | The text that appears on the banking statement. The default descriptor is a 10 character ID if an override is not set in the sweep configs statementDescriptor. |
| `minimum_balance`                                                                                                                                               | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `retries`                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                | :heavy_minus_sign:                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                             |

### Response

**[models.SweepConfig](../../models/sweepconfig.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.GenericError          | 400, 409                     | application/json             |
| models.PatchSweepConfigError | 422                          | application/json             |
| models.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_sweeps

List sweeps associated with a wallet.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.list_sweeps(security=moov.ListSweepsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="0fe45272-ee0d-401f-a10e-21e396676598", wallet_id="5f738f67-1989-4589-beb1-3d2f5c53a821", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ListSweepsSecurity](../../models/listsweepssecurity.md)     | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |                                                                     |
| `skip`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 60                                                                  |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `status`                                                            | [Optional[models.SweepStatus]](../../models/sweepstatus.md)         | :heavy_minus_sign:                                                  | Optional parameter to filter by sweep status.                       |                                                                     |
| `statement_descriptor`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional string to filter by statement descriptor.                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.Sweep]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_sweep

Get details on a specific sweep.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.sweeps.get_sweep(security=moov.GetSweepSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="adb697e6-2888-48b9-b2c5-f2c3d487add5", wallet_id="9f00e2b3-9dfb-48a3-9a25-a08e80f9cf36", sweep_id="a5324f55-fbec-4323-94e4-c512608bb175")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetSweepSecurity](../../models/getsweepsecurity.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sweep_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Sweep](../../models/sweep.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |