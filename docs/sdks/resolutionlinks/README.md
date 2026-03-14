# ResolutionLinks

## Overview

### Available Operations

* [create](#create) - Create a resolution link for the specified account. Resolution links are temporary, secure links
sent to merchants to resolve account requirements such as KYC verification or document uploads.  Only one active resolution link
is allowed per connected account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write`, `/accounts/{accountID}/representatives.write` and `/accounts/{accountID}/files.write` scopes.
* [list](#list) - List resolution links for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [get](#get) - Get a resolution link by code.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [disable](#disable) - Disable a resolution link. Disabled resolution links can no longer be used by merchants.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

## create

Create a resolution link for the specified account. Resolution links are temporary, secure links
sent to merchants to resolve account requirements such as KYC verification or document uploads.  Only one active resolution link
is allowed per connected account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write`, `/accounts/{accountID}/representatives.write` and `/accounts/{accountID}/files.write` scopes.

### Example Usage

<!-- UsageSnippet language="python" operationID="createResolutionLink" method="post" path="/accounts/{accountID}/resolution-links" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.resolution_links.create(account_id="<id>", recipient={
        "phone": {
            "number": "5555555555",
            "country_code": "1",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `account_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `recipient`                                                                              | [components.ResolutionLinkRecipient](../../models/components/resolutionlinkrecipient.md) | :heavy_check_mark:                                                                       | The recipient contact information for the resolution link.                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateResolutionLinkResponse](../../models/operations/createresolutionlinkresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GenericError              | 400, 409                         | application/json                 |
| errors.CreateResolutionLinkError | 422                              | application/json                 |
| errors.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list

List resolution links for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listResolutionLinks" method="get" path="/accounts/{accountID}/resolution-links" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.resolution_links.list(account_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListResolutionLinksResponse](../../models/operations/listresolutionlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get a resolution link by code.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getResolutionLink" method="get" path="/accounts/{accountID}/resolution-links/{resolutionLinkCode}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.resolution_links.get(account_id="<id>", resolution_link_code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `resolution_link_code`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetResolutionLinkResponse](../../models/operations/getresolutionlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## disable

Disable a resolution link. Disabled resolution links can no longer be used by merchants.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="disableResolutionLink" method="delete" path="/accounts/{accountID}/resolution-links/{resolutionLinkCode}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.resolution_links.disable(account_id="<id>", resolution_link_code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `resolution_link_code`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DisableResolutionLinkResponse](../../models/operations/disableresolutionlinkresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |