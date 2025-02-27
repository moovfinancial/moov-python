# Institutions
(*institutions*)

## Overview

### Available Operations

* [search](#search) - Search for institutions by either their name or routing number.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/fed.read` scope.

## search

Search for institutions by either their name or routing number.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/fed.read` scope.

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

    res = moov.institutions.search()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `name`                                                                                    | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Name of the financial institution. Either `name` or `routingNumber` is required.          |
| `routing_number`                                                                          | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Routing number for a financial institution. Either `routingNumber` or `name` is required. |
| `state`                                                                                   | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The state where a financial institution is based.                                         |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | Maximum results returned by a search.                                                     |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[operations.ListInstitutionsResponse](../../models/operations/listinstitutionsresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |