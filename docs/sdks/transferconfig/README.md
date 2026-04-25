# TransferConfig

## Overview

### Available Operations

* [create](#create) - Create a transfer config for an account.
* [get](#get) - Get the transfer config for an account.
* [update](#update) - Update the transfer config for an account.

## create

Create a transfer config for an account.

### Example Usage: Fixed amount tip config created

<!-- UsageSnippet language="python" operationID="createTransferConfig" method="post" path="/accounts/{accountID}/transfer-config" example="Fixed amount tip config created" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.create(account_id="<id>", tip_presets={
        "fixed_amount_options": [
            {
                "currency": "USD",
                "value_decimal": "12.987654321",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: Percentage tip config created

<!-- UsageSnippet language="python" operationID="createTransferConfig" method="post" path="/accounts/{accountID}/transfer-config" example="Percentage tip config created" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.create(account_id="<id>", tip_presets={
        "fixed_amount_options": [
            {
                "currency": "USD",
                "value_decimal": "12.987654321",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `account_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | Your Moov account ID.                                                                |
| `tip_presets`                                                                        | [Optional[components.CreateTipPresets]](../../models/components/createtippresets.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateTransferConfigResponse](../../models/operations/createtransferconfigresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400                                  | application/json                     |
| errors.TransferConfigValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## get

Get the transfer config for an account.

### Example Usage: Fixed amount tip config

<!-- UsageSnippet language="python" operationID="getTransferConfig" method="get" path="/accounts/{accountID}/transfer-config" example="Fixed amount tip config" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.get(account_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: Percentage tip config

<!-- UsageSnippet language="python" operationID="getTransferConfig" method="get" path="/accounts/{accountID}/transfer-config" example="Percentage tip config" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.get(account_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTransferConfigResponse](../../models/operations/gettransferconfigresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update the transfer config for an account.

### Example Usage: Updated fixed amount tip config

<!-- UsageSnippet language="python" operationID="updateTransferConfig" method="put" path="/accounts/{accountID}/transfer-config" example="Updated fixed amount tip config" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.update(account_id="<id>", tip_presets={
        "fixed_amount_options": [
            {
                "currency": "USD",
                "value_decimal": "12.987654321",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: Updated percentage tip config

<!-- UsageSnippet language="python" operationID="updateTransferConfig" method="put" path="/accounts/{accountID}/transfer-config" example="Updated percentage tip config" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.transfer_config.update(account_id="<id>", tip_presets={
        "fixed_amount_options": [
            {
                "currency": "USD",
                "value_decimal": "12.987654321",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `tip_presets`                                                        | [components.PutTipPresets](../../models/components/puttippresets.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.UpdateTransferConfigResponse](../../models/operations/updatetransferconfigresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400                                  | application/json                     |
| errors.TransferConfigValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |