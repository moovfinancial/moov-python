# BrandingSDK
(*branding*)

## Overview

### Available Operations

* [get_branding](#get_branding) - Get account branding
* [create_branding](#create_branding) - Create a brand
* [update_branding](#update_branding) - Update branding

## get_branding

Gets the brand properties for the specified account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.branding.get_branding(account_id="4de607f4-575e-4ce3-9d41-d6af8398a770")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBrandingResponse](../../models/getbrandingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_branding

Creates the brand properties for the specified account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.branding.create_branding(account_id="3226d1b6-78c9-4a27-88d7-faf928bc4492", request_body={
    "colors": {
        "light": {
            "accent": "#111111",
        },
        "dark": {
            "accent": "#ffffff",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | ID of the account.                                                                                |
| `request_body`                                                                                    | [models.CreateBrandingCreateBrandingRequest](../../models/createbrandingcreatebrandingrequest.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.CreateBrandingResponse](../../models/createbrandingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_branding

Updates the brand properties for the specified account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.branding.update_branding(account_id="3c399c04-daff-4fba-90b7-bc0d2d264610", request_body={
    "colors": {
        "light": {
            "accent": "#111111",
        },
        "dark": {
            "accent": "#ffffff",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `account_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | ID of the account.                                                                              |
| `request_body`                                                                                  | [models.UpdateBrandingPatchBrandingRequest](../../models/updatebrandingpatchbrandingrequest.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.UpdateBrandingResponse](../../models/updatebrandingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |