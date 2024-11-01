# AccessToken
(*access_token*)

## Overview

When making requests to Moov from a browser, you can use OAuth with JSON Web Tokens (JWT).

Our authentication flow follows the OAuth 2.0 standard. With this endpoint, you'll [create an access token](/api/authentication/access-tokens/) that you will pass along with API requests or when initializing Moov.js. To generate an authentication token, you’ll need to specify [scopes](https://docs.moov.io/guides/developer-tools/scopes/) that enable the token to use a specific set of API endpoints. <br><br> If a scope is required, it will be listed in the description of the endpoint.


### Available Operations

* [create_o_auth2_token](#create_o_auth2_token) - Create access token
* [revoke_o_auth2_token](#revoke_o_auth2_token) - Revoke access token

## create_o_auth2_token

Use the `client_id` and `client_secret` to generate an access token.

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov()

res = s.access_token.create_o_auth2_token(security=moov.CreateOAuth2TokenSecurity(
    username=os.getenv("MOOV_USERNAME", ""),
    password=os.getenv("MOOV_PASSWORD", ""),
), request={
    "grant_type": moov.GrantType.REFRESH_TOKEN,
    "client_id": "5clTR_MdVrrkgxw2",
    "client_secret": "dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-",
    "scope": "/accounts.write",
    "refresh_token": "i1qxz68gu50zp4i8ceyxqogmq7y0yienm52351c6...",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                       | [models.ClientCredentialsGrantToAccessTokenRequest](../../models/clientcredentialsgranttoaccesstokenrequest.md) | :heavy_check_mark:                                                                                              | The request object to use for the request.                                                                      |
| `security`                                                                                                      | [models.CreateOAuth2TokenSecurity](../../createoauth2tokensecurity.md)                                          | :heavy_check_mark:                                                                                              | The security requirements to use for the request.                                                               |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.CreateOAuth2TokenResponse](../../models/createoauth2tokenresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.AccessTokenErrorResponse | 400                             | application/json                |
| models.SDKError                 | 4XX, 5XX                        | \*/\*                           |

## revoke_o_auth2_token

Allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov()

res = s.access_token.revoke_o_auth2_token(security=moov.RevokeOAuth2TokenSecurity(
    username=os.getenv("MOOV_USERNAME", ""),
    password=os.getenv("MOOV_PASSWORD", ""),
), request={
    "token": "i1qxz68gu50zp4i8ceyxqogmq7y0yienm52351c6...",
    "client_id": "5clTR_MdVrrkgxw2",
    "client_secret": "dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [models.RevokeTokenRequest](../../models/revoketokenrequest.md)        | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `security`                                                             | [models.RevokeOAuth2TokenSecurity](../../revokeoauth2tokensecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.RevokeOAuth2TokenResponse](../../models/revokeoauth2tokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |