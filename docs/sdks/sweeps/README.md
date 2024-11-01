# Sweeps
(*sweeps*)

## Overview

### Available Operations

* [create_sweep_config](#create_sweep_config) - Create a sweep config
* [list_sweep_configs](#list_sweep_configs) - List sweep configs
* [patch_sweep_config](#patch_sweep_config) - Patch a sweep config
* [get_sweep_config](#get_sweep_config) - Get a sweep config
* [list_sweeps](#list_sweeps) - List sweeps
* [get_sweep](#get_sweep) - Get a sweep

## create_sweep_config

Create a sweep config for a wallet.

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.create_sweep_config(account_id="a373e852-7770-4fea-9cd5-2d6fc641d76a", create_sweep_config={
    "wallet_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "status": moov.SweepConfigStatus.ENABLED,
    "push_payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "pull_payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "minimum_balance": "12.34",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `create_sweep_config`                                               | [models.CreateSweepConfig](../../models/createsweepconfig.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateSweepConfigResponse](../../models/createsweepconfigresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.Error1           | 400                     | application/json        |
| models.SweepConfigError | 409                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_sweep_configs

List sweep configs associated with an account.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.list_sweep_configs(account_id="b06d7726-4020-4fef-9035-75779c0fc48c")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSweepConfigsResponse](../../models/listsweepconfigsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## patch_sweep_config

Update settings on a sweep config.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.patch_sweep_config(account_id="c0ee091a-5b72-49c9-9c8b-7cb99d7f9309", sweep_config_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", patch_sweep_config={
    "minimum_balance": "12.34",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `sweep_config_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the sweep config                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `patch_sweep_config`                                                | [models.PatchSweepConfig](../../models/patchsweepconfig.md)         | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PatchSweepConfigResponse](../../models/patchsweepconfigresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## get_sweep_config

Get a sweep config associated with a wallet.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.get_sweep_config(account_id="1f4428ca-3d11-441b-93d5-3fada6a5db01", sweep_config_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `sweep_config_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the sweep config                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSweepConfigResponse](../../models/getsweepconfigresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_sweeps

List sweeps associated with a wallet.

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.list_sweeps(request={
    "account_id": "0fe45272-ee0d-401f-a10e-21e396676598",
    "wallet_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "status": moov.SweepStatus.PAID,
    "statement_descriptor": "swp_f6g955",
    "count": 10,
    "skip": 10,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListSweepsRequest](../../models/listsweepsrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSweepsResponse](../../models/listsweepsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_sweep

Get details on a specific sweep.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.sweeps.get_sweep(account_id="adb697e6-2888-48b9-b2c5-f2c3d487add5", wallet_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", sweep_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of the wallet                                                    | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `sweep_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the sweep                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSweepResponse](../../models/getsweepresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |