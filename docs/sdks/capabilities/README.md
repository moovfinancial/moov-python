# Capabilities
(*capabilities*)

## Overview

### Available Operations

* [list_capabilities](#list_capabilities) - Retrieve all the capabilities an account has requested.

Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.
* [add_capabilities](#add_capabilities) - Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_capability](#get_capability) - Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [disable_capability](#disable_capability) - Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## list_capabilities

Retrieve all the capabilities an account has requested.

Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.capabilities.list_capabilities(security=moov.ListCapabilitiesSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="c236a258-0a99-455d-9fbb-2312bc028cd2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.ListCapabilitiesSecurity](../../models/listcapabilitiessecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `account_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `x_moov_version`                                                            | [Optional[models.Versions]](../../models/versions.md)                       | :heavy_minus_sign:                                                          | Specify an API version.                                                     |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.Capability]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## add_capabilities

Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.capabilities.add_capabilities(security=moov.AddCapabilitiesSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="1f48b82c-3158-4fa6-a507-0bd22afd441e", capabilities=[
        moov.CapabilityID.COLLECT_FUNDS,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.AddCapabilitiesSecurity](../../models/addcapabilitiessecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `account_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `capabilities`                                                            | List[[models.CapabilityID](../../models/capabilityid.md)]                 | :heavy_check_mark:                                                        | N/A                                                                       |
| `x_moov_version`                                                          | [Optional[models.Versions]](../../models/versions.md)                     | :heavy_minus_sign:                                                        | Specify an API version.                                                   |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[List[models.Capability]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.GenericError         | 400, 409                    | application/json            |
| models.AddCapabilitiesError | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_capability

Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.capabilities.get_capability(security=moov.GetCapabilitySecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="15fbc94d-721f-44a3-b5fb-77f58657305f", capability_id=moov.CapabilityID.TRANSFERS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetCapabilitySecurity](../../models/getcapabilitysecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `account_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `capability_id`                                                       | [models.CapabilityID](../../models/capabilityid.md)                   | :heavy_check_mark:                                                    | Moov account capabilities.                                            |
| `x_moov_version`                                                      | [Optional[models.Versions]](../../models/versions.md)                 | :heavy_minus_sign:                                                    | Specify an API version.                                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Capability](../../models/capability.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## disable_capability

Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    moov.capabilities.disable_capability(security=moov.DisableCapabilitySecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="c57b48d7-4182-4632-a345-eeed5a742b0d", capability_id=moov.CapabilityID.CARD_ISSUING)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.DisableCapabilitySecurity](../../models/disablecapabilitysecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `account_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `capability_id`                                                               | [models.CapabilityID](../../models/capabilityid.md)                           | :heavy_check_mark:                                                            | Moov account capabilities.                                                    |
| `x_moov_version`                                                              | [Optional[models.Versions]](../../models/versions.md)                         | :heavy_minus_sign:                                                            | Specify an API version.                                                       |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |