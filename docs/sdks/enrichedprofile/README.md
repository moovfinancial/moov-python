# EnrichedProfile
(*enriched_profile*)

## Overview

### Available Operations

* [get_enrichment_profile](#get_enrichment_profile) -   Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit. 

  To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## get_enrichment_profile

  Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit. 

  To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.enriched_profile.get_enrichment_profile(security=operations.GetEnrichmentProfileSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), email="Sheldon.Effertz@gmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.GetEnrichmentProfileSecurity](../../models/operations/getenrichmentprofilesecurity.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `email`                                                                                            | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `x_moov_version`                                                                                   | [Optional[components.Versions]](../../models/components/versions.md)                               | :heavy_minus_sign:                                                                                 | Specify an API version.                                                                            |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[components.EnrichedBusinessProfile](../../models/components/enrichedbusinessprofile.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |