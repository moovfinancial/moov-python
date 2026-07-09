# DepositView

## Overview

### Available Operations

* [create](#create) - Ingest a deposit account into the deposit view from a core banking source system.

The request body is a raw byte payload whose format depends on the core banking
system that produced it. Set the `X-Source-System` header to identify that system
so the payload can be parsed correctly.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

## create

Ingest a deposit account into the deposit view from a core banking source system.

The request body is a raw byte payload whose format depends on the core banking
system that produced it. Set the `X-Source-System` header to identify that system
so the payload can be parsed correctly.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDepositAccount" method="post" path="/underwriting/{accountID}/deposit-accounts" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.deposit_view.create(account_id="<id>", x_source_system=components.SourceSystem.JH_CIF2020, request_body=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `account_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `x_source_system`                                                         | [components.SourceSystem](../../models/components/sourcesystem.md)        | :heavy_check_mark:                                                        | Identifies the core banking source system that produced the request body. |
| `request_body`                                                            | *Union[bytes, IO[bytes], io.IOBase]*                                      | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[operations.CreateDepositAccountResponse](../../models/operations/createdepositaccountresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400, 409                             | application/json                     |
| errors.DepositAccountValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |