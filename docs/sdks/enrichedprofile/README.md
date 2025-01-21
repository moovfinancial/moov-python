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
import moov
from moov import Moov

with Moov() as moov:

    res = moov.enriched_profile.get_enrichment_profile(security=moov.GetEnrichmentProfileSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), email="Sheldon.Effertz@gmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetEnrichmentProfileSecurity](../../models/getenrichmentprofilesecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `email`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `x_moov_version`                                                                    | [Optional[models.Versions]](../../models/versions.md)                               | :heavy_minus_sign:                                                                  | Specify an API version.                                                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EnrichedBusinessProfile](../../models/enrichedbusinessprofile.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |