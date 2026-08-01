# Avatars

## Overview

### Available Operations

* [get](#get) - Get avatar image for an account using a unique ID.    

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/profile-enrichment.read` scope.
* [upload](#upload) - Upload a user avatar image for an account.

The image will be normalized to 512x512 PNG format and stored separately from
automatically discovered logos. User-uploaded avatars take precedence over enriched avatars at read time.

This endpoint only accepts accountID values for the uniqueID parameter.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts.write` scope.
* [delete](#delete) - Delete a user-uploaded avatar for an account.

After deletion, the avatar endpoint will fall back to the enriched avatar
or an account-type-aware fallback icon.

This endpoint only accepts accountID values for the uniqueID parameter.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts.write` scope.

## get

Get avatar image for an account using a unique ID.    

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/profile-enrichment.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAvatar" method="get" path="/avatars/{uniqueID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.avatars.get(unique_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `unique_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Any unique ID associated with an account such as accountID, representativeID, routing number, or userID. |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAvatarResponse](../../models/operations/getavatarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## upload

Upload a user avatar image for an account.

The image will be normalized to 512x512 PNG format and stored separately from
automatically discovered logos. User-uploaded avatars take precedence over enriched avatars at read time.

This endpoint only accepts accountID values for the uniqueID parameter.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadAvatar" method="put" path="/avatars/{uniqueID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import operations


with Moov() as moov:

    res = moov.avatars.upload(security=operations.UploadAvatarSecurity(
        username="",
    ), unique_id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.UploadAvatarSecurity](../../models/operations/uploadavatarsecurity.md)       | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `unique_id`                                                                              | *str*                                                                                    | :heavy_check_mark:                                                                       | The accountID to upload the avatar for. Only accountID values are accepted for writes.   |
| `file`                                                                                   | [components.AvatarUploadRequestFile](../../models/components/avataruploadrequestfile.md) | :heavy_check_mark:                                                                       | A JPEG, PNG, or WebP image file to upload as an avatar.                                  |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UploadAvatarResponse](../../models/operations/uploadavatarresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## delete

Delete a user-uploaded avatar for an account.

After deletion, the avatar endpoint will fall back to the enriched avatar
or an account-type-aware fallback icon.

This endpoint only accepts accountID values for the uniqueID parameter.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAvatar" method="delete" path="/avatars/{uniqueID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import operations


with Moov() as moov:

    res = moov.avatars.delete(security=operations.DeleteAvatarSecurity(
        username="",
    ), unique_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.DeleteAvatarSecurity](../../models/operations/deleteavatarsecurity.md)     | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `unique_id`                                                                            | *str*                                                                                  | :heavy_check_mark:                                                                     | The accountID to delete the avatar for. Only accountID values are accepted for writes. |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.DeleteAvatarResponse](../../models/operations/deleteavatarresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |