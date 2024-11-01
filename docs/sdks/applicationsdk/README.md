# ApplicationSDK
(*application*)

## Overview

An application allows an account to connect to other accounts and gain access to their information and move money on their behalf.


### Available Operations

* [enable_application](#enable_application) - Enable this account as a application provider
* [list_applications](#list_applications) - List applications
* [update_application](#update_application) - Update an application
* [disable_application](#disable_application) - Disables an application
* [list_application_keys](#list_application_keys) - List keys for an application
* [create_application_keys](#create_application_keys) - Create a new application key
* [disable_application_key](#disable_application_key) - Disables an application key
* [update_application_key](#update_application_key) - Updates an application key

## enable_application

Enable this account as a application provider

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.enable_application(request={
    "name": "Amanda Yang",
    "description": "Here lies a description of the item",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateApplication](../../models/createapplication.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnableApplicationResponse](../../models/enableapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_applications

List applications for an account

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.list_applications()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListApplicationsResponse](../../models/listapplicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_application

Updates an application

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.update_application(application_id="6a1f242b-0c98-47a4-b66d-45ec984edc18", update_application={
    "name": "Amanda Yang",
    "description": "Here lies a description of the item",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `update_application`                                                | [models.UpdateApplication](../../models/updateapplication.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateApplicationResponse](../../models/updateapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disable_application

Disables an application

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.disable_application(application_id="70d1abf8-7802-4507-8bfa-6eec8a778964")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DisableApplicationResponse](../../models/disableapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_application_keys

Lists keys for an application

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.list_application_keys(application_id="c0bb3a97-221c-4208-95ce-96dbba575bb7")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListApplicationKeysResponse](../../models/listapplicationkeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_application_keys

Create a new application key that can be used for OAuth 2.0 authentication

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.create_application_keys(application_id="6f6615db-e341-4a11-886c-7842218cdd62", create_application_key={
    "name": "Amanda Yang",
    "description": "Here lies a description of the item",
    "origins": [
        "https://placekitten.com/408/287",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `create_application_key`                                            | [models.CreateApplicationKey](../../models/createapplicationkey.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateApplicationKeysResponse](../../models/createapplicationkeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disable_application_key

Disables an application key

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.disable_application_key(application_id="4f0724bf-9c38-43c8-a0b8-97ae1f58e9c3", application_key_id="b956f31d-0358-43d4-9ab9-f64bd5c55863")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `application_key_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the application key                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DisableApplicationKeyResponse](../../models/disableapplicationkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_application_key

Updates an application key

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.application.update_application_key(application_id="b3ca54db-1ac4-4c00-8dd6-02f07e89bcf8", application_key_id="3eac5e2f-4ff4-4a4f-b903-61dfacf43701", update_application_key={
    "name": "Amanda Yang",
    "description": "Here lies a description of the item",
    "origins": [
        "https://placekitten.com/408/287",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the application                                               |
| `application_key_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the application key                                           |
| `update_application_key`                                            | [models.UpdateApplicationKey](../../models/updateapplicationkey.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateApplicationKeyResponse](../../models/updateapplicationkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |