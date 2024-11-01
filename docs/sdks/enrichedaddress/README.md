# EnrichedAddress
(*enriched_address*)

## Overview

Search for valid addresses using a partial or full address.


### Available Operations

* [get_enrichment_address](#get_enrichment_address) - Get address suggestions

## get_enrichment_address

Fetch enriched address suggestions. Requires a partial address. 
<br><br> To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.enriched_address.get_enrichment_address(request={
    "search": "123 Main Street",
    "max_results": 10,
    "include_cities": "chicago;honolulu;portland",
    "include_states": "illinois;hawaii;oregon",
    "include_zipcodes": "60412;96818;97209",
    "exclude_states": "AZ;WA;SC",
    "prefer_cities": "denver;aurora;omaha",
    "prefer_states": "CO;MN;WI",
    "prefer_zipcodes": "60412;96818;97209",
    "prefer_ratio": 45,
    "prefer_geolocation": "none",
    "selected": "Apt",
    "source": "all",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.GetEnrichmentAddressRequest](../../models/getenrichmentaddressrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetEnrichmentAddressResponse](../../models/getenrichmentaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |