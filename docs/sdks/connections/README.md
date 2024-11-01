# Connections
(*connections*)

## Overview

A connection forms a relationship between two accounts, allowing them to transact with each other. When you create an account for someone else, your account automatically has a connection with the account you've just created.

### Available Operations

* [list_connections](#list_connections) - List connections

## list_connections

Lists all the accounts that a specific account is connected to.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.connections.list_connections()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListConnectionsResponse](../../models/listconnectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |