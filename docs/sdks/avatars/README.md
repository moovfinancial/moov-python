# Avatars
(*avatars*)

## Overview

You can retrieve an account's profile image. This is especially useful if you'd like to use the profile image for a corresponding account in your own product.


### Available Operations

* [get_avatar](#get_avatar) - Get avatar

## get_avatar

Get avatar image for an account using a unique ID.
<br><br> To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.avatars.get_avatar(unique_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `unique_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Any unique ID associated with an account such as accountID, representativeID, routing number, or userID. |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[models.GetAvatarResponse](../../models/getavatarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |