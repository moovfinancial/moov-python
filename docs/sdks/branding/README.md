# Branding
(*branding*)

## Overview

### Available Operations

* [post_brand](#post_brand) - Creates the brand properties for the specified account.
* [get_brand](#get_brand) - Gets the brand properties for the specified account.
* [update_brand](#update_brand) - Updates the brand properties for the specified account.

## post_brand

Creates the brand properties for the specified account.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.branding.post_brand(security=moov.PostBrandSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="e0ae5cc2-d23b-44c7-b778-06f786dadb4b", colors=moov.Colors(
        dark={
            "accent": "#111111",
        },
        light={
            "accent": "#111111",
        },
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.PostBrandSecurity](../../models/postbrandsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `colors`                                                            | [models.Colors](../../models/colors.md)                             | :heavy_check_mark:                                                  | Set brand accent colors for light and dark modes.                   |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Brand](../../models/brand.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.GenericError         | 400, 409                    | application/json            |
| models.BrandValidationError | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_brand

Gets the brand properties for the specified account.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.branding.get_brand(security=moov.GetBrandSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="07eb5173-1869-4649-9aa6-f399787a2751")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetBrandSecurity](../../models/getbrandsecurity.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Brand](../../models/brand.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_brand

Updates the brand properties for the specified account.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.branding.update_brand(security=moov.UpdateBrandSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="6c1f5632-7f37-4b3d-861e-10e31b8853de")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.UpdateBrandSecurity](../../models/updatebrandsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `colors`                                                            | [Optional[models.UpdateColors]](../../models/updatecolors.md)       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Brand](../../models/brand.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.GenericError         | 400, 409                    | application/json            |
| models.BrandValidationError | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |