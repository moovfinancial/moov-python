# Devices
(*devices*)

## Overview

### Available Operations

* [refresh_session](#refresh_session) - Refresh Cookie
* [list_devices_for_user](#list_devices_for_user) - Devices for a user
* [get_device_for_user](#get_device_for_user) - Specific device
* [disable_device_for_user](#disable_device_for_user) - Disable device

## refresh_session

Refresh the cookie to keep a user logged in

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.devices.refresh_session(request={
    "fingerprint": "fBkwz3q43jlTHB8wFtiDgxT0WMpjUmDvMsTbQbz1",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeviceInfo](../../models/deviceinfo.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_devices_for_user

Returns the list of devices that are currently remembered

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.devices.list_devices_for_user(user_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Which userID to list the devices of                                 | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListDevicesForUserResponse](../../models/listdevicesforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_device_for_user

Get Information on a specific device

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.devices.get_device_for_user(user_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", device_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Which userID to list the devices of                                 | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `device_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Which device that belongs to the user to get                        | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDeviceForUserResponse](../../models/getdeviceforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disable_device_for_user

Disable a specific device

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.devices.disable_device_for_user(user_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", device_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Which userID to list the devices of                                 | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `device_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Which device that belongs to the user to get                        | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DisableDeviceForUserResponse](../../models/disabledeviceforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |