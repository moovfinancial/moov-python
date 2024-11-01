# Institutions
(*institutions*)

## Overview

Lookup ACH and wire participating financial institutions. We recommend using this endpoint when an end-user enters a routing number to confirm their bank or credit union.


### Available Operations

* [search_institutions](#search_institutions) - Search institutions

## search_institutions

Search for institutions by their routing number or name. <br><br> To use this endpoint from the browser, you'll need to specify the `/fed.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.institutions.search_institutions(request={
    "rail": moov.Rail.WIRE,
    "name": "Farmers",
    "routing_number": "044112187",
    "state": "IA",
    "limit": 499,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.SearchInstitutionsRequest](../../models/searchinstitutionsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.SearchInstitutionsResponse](../../models/searchinstitutionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |