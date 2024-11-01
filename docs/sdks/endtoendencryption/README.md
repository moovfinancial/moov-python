# EndToEndEncryption
(*end_to_end_encryption*)

## Overview

Allows for the passing of secure authentication data through an unverified proxies.


### Available Operations

* [generate_end_to_end_key](#generate_end_to_end_key) - Generate public key
* [test_end_to_end_token](#test_end_to_end_token) - Test JWE

## generate_end_to_end_key

Generates a public key used to create a JWE token for passing secure authentication data through non-PCI compliant intermediaries. 
Endpoint is aggressively rate limited to anonymous requests. Contact Moov to enable usage of this feature in production.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.end_to_end_encryption.generate_end_to_end_key()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenerateEndToEndKeyResponse](../../models/generateendtoendkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## test_end_to_end_token

Allows for testing a JWE token to ensure it's acceptable by Moov. 
Requires authenticated call with `ping.read` scope.
Contact Moov to enable usage of this feature in production.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.end_to_end_encryption.test_end_to_end_token()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestEndToEndTokenResponse](../../models/testendtoendtokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |