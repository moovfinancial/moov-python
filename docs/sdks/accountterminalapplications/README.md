# AccountTerminalApplications
(*account_terminal_applications*)

## Overview

### Available Operations

* [link](#link) - Link an account with a terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.write` scope.
* [list](#list) - Retrieve all terminal applications linked to a specific account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.
* [get](#get) - Verifies if a specific Terminal Application is linked to an Account. This endpoint acts as a validation check for the link's existence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.
* [get_configuration](#get_configuration) - Fetch the configuration for a given Terminal Application linked to a specific Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-configuration.read` scope.

## link

Link an account with a terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.write` scope.

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

    res = moov.account_terminal_applications.link(account_id="76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e", terminal_application_id="12345678-1234-1234-1234-123456789012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e                                |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the terminal application.                                     | 12345678-1234-1234-1234-123456789012                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.LinkAccountTerminalApplicationResponse](../../models/operations/linkaccountterminalapplicationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GenericError                    | 400, 409                               | application/json                       |
| errors.AccountTerminalApplicationError | 422                                    | application/json                       |
| errors.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

Retrieve all terminal applications linked to a specific account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.

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

    res = moov.account_terminal_applications.list(account_id="76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListAccountTerminalApplicationsResponse](../../models/operations/listaccountterminalapplicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Verifies if a specific Terminal Application is linked to an Account. This endpoint acts as a validation check for the link's existence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.

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

    res = moov.account_terminal_applications.get(account_id="76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e", terminal_application_id="12345678-1234-1234-1234-123456789012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e                                |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12345678-1234-1234-1234-123456789012                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetAccountTerminalApplicationResponse](../../models/operations/getaccountterminalapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_configuration

Fetch the configuration for a given Terminal Application linked to a specific Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-configuration.read` scope.

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

    res = moov.account_terminal_applications.get_configuration(account_id="76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e", terminal_application_id="12345678-1234-1234-1234-123456789012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 76d4c8a0-1f2b-4e3b-8f5c-7a9e1b2c3d4e                                |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12345678-1234-1234-1234-123456789012                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetTerminalConfigurationResponse](../../models/operations/getterminalconfigurationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |