# Institutions
(*institutions*)

## Overview

### Available Operations

* [list_institutions](#list_institutions) -   Search for institutions by either their name or routing number.
  
  To use this endpoint from the browser, you'll need to specify the `/fed.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## list_institutions

  Search for institutions by either their name or routing number.
  
  To use this endpoint from the browser, you'll need to specify the `/fed.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.institutions.list_institutions(security=moov.ListInstitutionsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.ListInstitutionsSecurity](../../models/listinstitutionssecurity.md)               | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `x_moov_version`                                                                          | [Optional[models.Versions]](../../models/versions.md)                                     | :heavy_minus_sign:                                                                        | Specify an API version.                                                                   |
| `name`                                                                                    | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Name of the financial institution. Either `name` or `routingNumber` is required.          |
| `routing_number`                                                                          | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Routing number for a financial institution. Either `routingNumber` or `name` is required. |
| `state`                                                                                   | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The state where a financial institution is based.                                         |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | Maximum results returned by a search.                                                     |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[List[models.FinancialInstitutions]](../../models/.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |