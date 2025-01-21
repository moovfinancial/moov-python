# Avatars
(*avatars*)

## Overview

### Available Operations

* [get_avatar](#get_avatar) - Get avatar image for an account using a unique ID.    

To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## get_avatar

Get avatar image for an account using a unique ID.    

To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.avatars.get_avatar(security=moov.GetAvatarSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), unique_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `security`                                                                                               | [models.GetAvatarSecurity](../../models/getavatarsecurity.md)                                            | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `unique_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Any unique ID associated with an account such as accountID, representativeID, routing number, or userID. |
| `x_moov_version`                                                                                         | [Optional[models.Versions]](../../models/versions.md)                                                    | :heavy_minus_sign:                                                                                       | Specify an API version.                                                                                  |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[models.GetAvatarResponse](../../models/getavatarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |