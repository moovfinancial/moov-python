# EnrichedProfile
(*enriched_profile*)

## Overview

By supplying an email address, you can retrieve a profile with enriched data fields. This service is offered in collaboration with Clearbit.


### Available Operations

* [get_enrichment_profile](#get_enrichment_profile) - Get enriched profile

## get_enrichment_profile

Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit.
<br><br> To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.enriched_profile.get_enrichment_profile(email="employee@business.com")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Valid email address belonging to the profile of interest<br/>       | employee@business.com                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetEnrichmentProfileResponse](../../models/getenrichmentprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |