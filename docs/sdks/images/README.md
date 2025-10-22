# Images
(*images*)

## Overview

### Available Operations

* [list](#list) - List metadata for all images in the specified account.
* [upload](#upload) -   Upload a new PNG, JPEG, or WebP image with optional metadata. 
  Duplicate images, and requests larger than 16MB will be rejected.
* [get_metadata](#get_metadata) - Retrieve metadata for a specific image by its ID.
* [update](#update) - Update an existing image and/or its metadata.

Duplicate images, and requests larger than 16MB will be rejected. Omit any
form parts you do not wish to update. Existing metadata can be cleared by
sending `null` for the `metadata` form part.
* [delete](#delete) - Permanently delete an image by its ID.
* [get_public](#get_public) - Get an image by its public ID.

## list

List metadata for all images in the specified account.

### Example Usage

<!-- UsageSnippet language="python" operationID="listImageMetadata" method="get" path="/accounts/{accountID}/images" -->
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

    res = moov.images.list(account_id="3a4ed2d9-03e1-4b0e-b45f-2a9ca72f8adb", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `skip`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 60                                                                  |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListImageMetadataResponse](../../models/operations/listimagemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## upload

  Upload a new PNG, JPEG, or WebP image with optional metadata. 
  Duplicate images, and requests larger than 16MB will be rejected.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadImage" method="post" path="/accounts/{accountID}/images" -->
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

    res = moov.images.upload(account_id="c0971a52-1f1c-4511-876a-f45c4cfd6154", image={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `image`                                                                                      | [components.Image](../../models/components/image.md)                                         | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `metadata`                                                                                   | [Optional[components.ImageMetadataRequest]](../../models/components/imagemetadatarequest.md) | :heavy_minus_sign:                                                                           | Optional, json-encoded metadata to associate with the uploaded image.                        |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UploadImageResponse](../../models/operations/uploadimageresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GenericError                | 400, 409                           | application/json                   |
| errors.ImageRequestValidationError | 422                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_metadata

Retrieve metadata for a specific image by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getImageMetadata" method="get" path="/accounts/{accountID}/images/{imageID}" -->
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

    res = moov.images.get_metadata(account_id="6cf66a43-31ce-4d27-8dd4-130fa57f0a6f", image_id="7cec5bd3-6340-4de4-a923-bf6ec0f7e921")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `image_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetImageMetadataResponse](../../models/operations/getimagemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update an existing image and/or its metadata.

Duplicate images, and requests larger than 16MB will be rejected. Omit any
form parts you do not wish to update. Existing metadata can be cleared by
sending `null` for the `metadata` form part.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateImage" method="patch" path="/accounts/{accountID}/images/{imageID}" -->
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

    res = moov.images.update(account_id="310f4f19-45cf-4429-9aae-8e93827ecb0d", image_id="8ef109f8-5a61-4355-b2e4-b8ac2f6f6f47")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                         | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `image_id`                                                                                                                           | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `image`                                                                                                                              | [Optional[components.ImageUpdateRequestMultiPartImage]](../../models/components/imageupdaterequestmultipartimage.md)                 | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |
| `metadata`                                                                                                                           | [OptionalNullable[components.Metadata]](../../models/components/metadata.md)                                                         | :heavy_minus_sign:                                                                                                                   | JSON-encoded metadata to update for the image.<br/><br/>Omit this field if not updating metadata, or send `null` to clear existing metadata. |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.UpdateImageResponse](../../models/operations/updateimageresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GenericError                | 400, 409                           | application/json                   |
| errors.ImageRequestValidationError | 422                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## delete

Permanently delete an image by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteImage" method="delete" path="/accounts/{accountID}/images/{imageID}" -->
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

    res = moov.images.delete(account_id="866c32ce-2536-4b21-8e12-f8c474fb2a9b", image_id="ca048253-31d2-4bfb-9077-1f07a2a09f26")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `image_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteImageResponse](../../models/operations/deleteimageresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_public

Get an image by its public ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublicImage" method="get" path="/images/{publicID}" -->
```python
from moovio_sdk import Moov


with Moov() as moov:

    res = moov.images.get_public(public_id="<id>", size="400x400")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `public_id`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                |
| `if_none_match`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                |
| `size`                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Optional parameter to request a resized version of the image (WxH).<br/><br/>If either dimension is 0, the image will be scaled proportionally based on<br/>the non-zero dimension. Dimensions are capped at 2048 pixels. A default size<br/>of 400x400 will be used if this parameter is omitted. |
| `retries`                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                |

### Response

**[operations.GetPublicImageResponse](../../models/operations/getpublicimageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |