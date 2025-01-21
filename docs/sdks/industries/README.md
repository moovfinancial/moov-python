# Industries
(*industries*)

## Overview

### Available Operations

* [list_industries](#list_industries) -   Returns a list of all industry titles and their corresponding MCC/SIC/NAICS codes. Results are ordered by title.    
  
  To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## list_industries

  Returns a list of all industry titles and their corresponding MCC/SIC/NAICS codes. Results are ordered by title.    
  
  To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.industries.list_industries(security=moov.ListIndustriesSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ListIndustriesSecurity](../../models/listindustriessecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `x_moov_version`                                                        | [Optional[models.Versions]](../../models/versions.md)                   | :heavy_minus_sign:                                                      | Specify an API version.                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.EnrichedIndustry]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |