# Authentication
(*authentication*)

## Overview

### Available Operations

* [revoke_access_token](#revoke_access_token) - Revoke an auth token.

Allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed.
* [create_access_token](#create_access_token) - Create or refresh an access token.

## revoke_access_token

Revoke an auth token.

Allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed.

### Example Usage

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

    res = moov.authentication.revoke_access_token(token="<value>", client_id="5clTR_MdVrrkgxw2", client_secret="dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `token`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | The access or refresh token to revoke.                                                 |                                                                                        |
| `token_type_hint`                                                                      | [Optional[components.TokenTypeHint]](../../models/components/tokentypehint.md)         | :heavy_minus_sign:                                                                     | The type of token being revoked.                                                       |                                                                                        |
| `client_id`                                                                            | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Client ID can be provided here in the body, or as the Username in HTTP Basic Auth.     | 5clTR_MdVrrkgxw2                                                                       |
| `client_secret`                                                                        | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Client secret can be provided here in the body, or as the Password in HTTP Basic Auth. | dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-                                                       |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.RevokeAccessTokenResponse](../../models/operations/revokeaccesstokenresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400                            | application/json               |
| errors.RevokeTokenRequestError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## create_access_token

Create or refresh an access token.

### Example Usage

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

    res = moov.authentication.create_access_token(grant_type=components.GrantType.CLIENT_CREDENTIALS, client_id="5clTR_MdVrrkgxw2", client_secret="dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-", scope="/accounts.read /accounts.write", refresh_token="eyJhbGc0eSI6TQSIsImN0kpXVCIsImtp6IkpXVsImtpZC0a...")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                  | Description                                                                                                                                                                                                               | Example                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `grant_type`                                                                                                                                                                                                              | [components.GrantType](../../models/components/granttype.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                        | The type of grant being requested.<br/><br/>  - `client_credentials`: A grant type used by clients to obtain an access token<br/>  - `refresh_token`: A grant type used by clients to obtain a new access token using a refresh token |                                                                                                                                                                                                                           |
| `client_id`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | Client ID can be provided here in the body, or as the Username in HTTP Basic Auth.                                                                                                                                        | 5clTR_MdVrrkgxw2                                                                                                                                                                                                          |
| `client_secret`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | Client secret can be provided here in the body, or as the Password in HTTP Basic Auth.                                                                                                                                    | dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-                                                                                                                                                                                          |
| `scope`                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | A space delimited list of scopes. Required when `grant_type` is `client_credentials`.                                                                                                                                     | /accounts.read /accounts.write                                                                                                                                                                                            |
| `refresh_token`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | The refresh_token returned alongside the access token being refreshed. Required when `grant_type` is `refresh_token`.                                                                                                     | eyJhbGc0eSI6TQSIsImN0kpXVCIsImtp6IkpXVsImtpZC0a...                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                       |                                                                                                                                                                                                                           |

### Response

**[operations.CreateAccessTokenResponse](../../models/operations/createaccesstokenresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400                          | application/json             |
| errors.AuthTokenRequestError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |