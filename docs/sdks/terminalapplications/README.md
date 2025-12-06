# TerminalApplications

## Overview

### Available Operations

* [create](#create) - Create a new terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.
* [list](#list) - List all the terminal applications for a Moov Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.
* [get](#get) - Fetch a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.
* [delete](#delete) - Delete a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.
* [create_version](#create_version) - Register a new version of a terminal application. For Android applications, this is used to register a new version code of the application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.

## create

Create a new terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTerminalApplication" method="post" path="/terminal-applications" -->
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

    res = moov.terminal_applications.create(platform=components.TerminalApplicationPlatform.ANDROID, package_name="com.example.app", sha256_digest="AA:BB:CC:DD:EE:FF:AA:BB:CC:DD:EE:FF:AA:BB:CC:DD:AA:BB:CC:DD:EE:FF:AA:BB:CC:DD:EE:FF:AA:BB:CC:DD", version_code="20332277")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `platform`                                                                                       | [components.TerminalApplicationPlatform](../../models/components/terminalapplicationplatform.md) | :heavy_check_mark:                                                                               | Platform of the terminal application.                                                            | ios                                                                                              |
| `app_bundle_id`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app bundle identifier of the terminal application. Required if platform is `ios`.            |                                                                                                  |
| `package_name`                                                                                   | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app package name of the terminal application. Required if platform is `android`.             |                                                                                                  |
| `sha256_digest`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The SHA-256 digest of the signing key for the application. Required if platform is `android`.    |                                                                                                  |
| `version_code`                                                                                   | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The version code of the Android application. Required if platform is `android`.                  |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.CreateTerminalApplicationResponse](../../models/operations/createterminalapplicationresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GenericError             | 400, 409                        | application/json                |
| errors.TerminalApplicationError | 422                             | application/json                |
| errors.APIError                 | 4XX, 5XX                        | \*/\*                           |

## list

List all the terminal applications for a Moov Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTerminalApplications" method="get" path="/terminal-applications" -->
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

    res = moov.terminal_applications.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListTerminalApplicationsRequest](../../models/operations/listterminalapplicationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListTerminalApplicationsResponse](../../models/operations/listterminalapplicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Fetch a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTerminalApplication" method="get" path="/terminal-applications/{terminalApplicationID}" -->
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

    res = moov.terminal_applications.get(terminal_application_id="12345678-1234-1234-1234-123456789012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12345678-1234-1234-1234-123456789012                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetTerminalApplicationResponse](../../models/operations/getterminalapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTerminalApplication" method="delete" path="/terminal-applications/{terminalApplicationID}" -->
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

    res = moov.terminal_applications.delete(terminal_application_id="12345678-1234-1234-1234-123456789012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 12345678-1234-1234-1234-123456789012                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.DeleteTerminalApplicationResponse](../../models/operations/deleteterminalapplicationresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## create_version

Register a new version of a terminal application. For Android applications, this is used to register a new version code of the application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTerminalApplicationVersion" method="post" path="/terminal-applications/{terminalApplicationID}/versions" -->
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

    res = moov.terminal_applications.create_version(terminal_application_id="12345678-1234-1234-1234-123456789012", version="20440059")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `terminal_application_id`                                                                    | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          | 12345678-1234-1234-1234-123456789012                                                         |
| `version`                                                                                    | *str*                                                                                        | :heavy_check_mark:                                                                           | The app version of the terminal application (version code for Android terminal application). |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[operations.CreateTerminalApplicationVersionResponse](../../models/operations/createterminalapplicationversionresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GenericError             | 400, 409                        | application/json                |
| errors.TerminalApplicationError | 422                             | application/json                |
| errors.APIError                 | 4XX, 5XX                        | \*/\*                           |