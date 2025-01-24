# Ping
(*ping*)

## Overview

### Available Operations

* [ping](#ping) - A simple endpoint to check auth.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/ping.read` scope.

## ping

A simple endpoint to check auth.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/ping.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    moov.ping.ping(security=operations.PingSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Use the SDK ...

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `security`                                                           | [operations.PingSecurity](../../models/operations/pingsecurity.md)   | :heavy_check_mark:                                                   | N/A                                                                  |
| `x_moov_version`                                                     | [Optional[components.Versions]](../../models/components/versions.md) | :heavy_minus_sign:                                                   | Specify an API version.                                              |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |