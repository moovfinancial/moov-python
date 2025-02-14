# Avatars
(*avatars*)

## Overview

### Available Operations

* [get](#get) - Get avatar image for an account using a unique ID.    

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/profile-enrichment.read` scope.

## get

Get avatar image for an account using a unique ID.    

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/profile-enrichment.read` scope.

### Example Usage

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