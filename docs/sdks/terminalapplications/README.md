# TerminalApplications
(*terminal_applications*)

## Overview

### Available Operations

* [create](#create) - Create a new terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminalApplications.write` scope.
* [list](#list) - List all the terminal applications for a Moov Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminalApplications.read` scope.
* [get](#get) - Fetch a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminalApplications.read` scope.
* [delete](#delete) - Delete a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminalApplications.write` scope.

## create

Create a new terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminalApplications.write` scope.

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

    res = moov.terminal_applications.create(platform=components.TerminalApplicationPlatform.IOS, app_bundle_id="com.example.app", package_name="com.example.app", sha256_digest="1234567890", version_code="1.0.0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `platform`                                                                                       | [components.TerminalApplicationPlatform](../../models/components/terminalapplicationplatform.md) | :heavy_check_mark:                                                                               | Platform of the terminal application.                                                            | ios                                                                                              |
| `app_bundle_id`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app bundle identifier of the terminal application. Required if platform is ios.              |                                                                                                  |
| `package_name`                                                                                   | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app package name of the terminal application. Required if platform is android.               |                                                                                                  |
| `sha256_digest`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app version of the terminal application. Required if paltform is android.                    |                                                                                                  |
| `version_code`                                                                                   | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | The app version of the terminal application. Required if platform is android.                    |                                                                                                  |
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
you'll need to specify the `/terminalApplications.read` scope.

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
you'll need to specify the `/terminalApplications.read` scope.

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

    res = moov.terminal_applications.get(terminal_application_id="01234567-89ab-cdef-0123-456789abcdef")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 01234567-89ab-cdef-0123-456789abcdef                                |
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
you'll need to specify the `/terminalApplications.write` scope.

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

    res = moov.terminal_applications.delete(terminal_application_id="01234567-89ab-cdef-0123-456789abcdef")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `terminal_application_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 01234567-89ab-cdef-0123-456789abcdef                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.DeleteTerminalApplicationResponse](../../models/operations/deleteterminalapplicationresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |