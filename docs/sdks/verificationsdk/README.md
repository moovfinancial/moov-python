# VerificationSDK
(*verification*)

## Overview

### Available Operations

* [is_device_verified](#is_device_verified) - Device verification
* [check_verification_code_from_email](#check_verification_code_from_email) - Device verification
* [send_verification_code_via_email](#send_verification_code_via_email) - Send code via email

## is_device_verified

Checks to ensure a device is verified and if not how to go about getting it verified

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.verification.is_device_verified(request={
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

**[models.IsDeviceVerifiedResponse](../../models/isdeviceverifiedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## check_verification_code_from_email

Checks to ensure a device is verified and if not how to go about getting it verified

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.verification.check_verification_code_from_email(request={
    "fingerprint": "fBkwz3q43jlTHB8wFtiDgxT0WMpjUmDvMsTbQbz1",
    "code": "123456",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.VerifyViaEmail](../../models/verifyviaemail.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckVerificationCodeFromEmailResponse](../../models/checkverificationcodefromemailresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## send_verification_code_via_email

Send device verification code via email to the email address of the user

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.verification.send_verification_code_via_email()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SendViaEmail](../../models/sendviaemail.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SendVerificationCodeViaEmailResponse](../../models/sendverificationcodeviaemailresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |