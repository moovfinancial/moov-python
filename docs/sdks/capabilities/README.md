# Capabilities
(*capabilities*)

## Overview

### Available Operations

* [list](#list) - Retrieve all the capabilities an account has requested.

Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.
* [request](#request) - Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.
* [get](#get) - Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.
* [disable](#disable) - Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

  To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.

## list

Retrieve all the capabilities an account has requested.

Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.

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

    res = moov.capabilities.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListCapabilitiesResponse](../../models/operations/listcapabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## request

Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.

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

    res = moov.capabilities.request(account_id="32613610-de25-446e-8662-ec2709ffea9d", capabilities=[
        components.CapabilityID.COLLECT_FUNDS,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `account_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `capabilities`                                                           | List[[components.CapabilityID](../../models/components/capabilityid.md)] | :heavy_check_mark:                                                       | N/A                                                                      |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.RequestCapabilitiesResponse](../../models/operations/requestcapabilitiesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GenericError         | 400, 409                    | application/json            |
| errors.AddCapabilitiesError | 422                         | application/json            |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.

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

    res = moov.capabilities.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", capability_id=components.CapabilityID.PRODUCTION_APP)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                     |
| `capability_id`                                                                                                                                                                                                                                                         | [components.CapabilityID](../../models/components/capabilityid.md)                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                      | Moov account capabilities.<br/><br/>The `production-app` capability might appear in your list. This is a read-only capability that Moov requests and uses for account verification purposes. The capability remains active with your account and requires no additional action. |
| `retries`                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                     |

### Response

**[operations.GetCapabilityResponse](../../models/operations/getcapabilityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## disable

Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

  To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.

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

    res = moov.capabilities.disable(account_id="cd7cd1ce-90cc-444b-ac3e-badb79be277f", capability_id=components.CapabilityID.TRANSFERS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                     |
| `capability_id`                                                                                                                                                                                                                                                         | [components.CapabilityID](../../models/components/capabilityid.md)                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                      | Moov account capabilities.<br/><br/>The `production-app` capability might appear in your list. This is a read-only capability that Moov requests and uses for account verification purposes. The capability remains active with your account and requires no additional action. |
| `retries`                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                     |

### Response

**[operations.DisableCapabilityResponse](../../models/operations/disablecapabilityresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |