# OpenIDConnect
(*open_id_connect*)

## Overview

Details on Moov's open id connect implementation

### Available Operations

* [oidc_authentication](#oidc_authentication) - Authenticate with OIDC Provider
* [oidc_callback](#oidc_callback) - Callback from OIDC Provider

## oidc_authentication

Initiates the authentication with the Provider specified by `providerID`.
This will redirect to the provider who will authenticate the user. Once the provider has authenticated 
the user it will redirect them back to us on the `/callback` url.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.open_id_connect.oidc_authentication(provider_id="my-oidc-provider")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name of the Provider to use                                         | my-oidc-provider                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OIDCAuthenticationResponse](../../models/oidcauthenticationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## oidc_callback

This is called by the users browser once their OpenID Connect provider has authenticated the user. The 
OIDC provider will send tokens we inspect and use to obtain their information and log them into the system.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.open_id_connect.oidc_callback(provider_id="my-oidc-provider")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name of the Provider to use                                         | my-oidc-provider                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OIDCCallbackResponse](../../models/oidccallbackresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |