# Analytics
(*analytics*)

## Overview

You can retrieve helpful at-a-glance information about your account by getting metrics on categories such as new accounts, transfer counts, and transfer volume over different time periods.


### Available Operations

* [analytics_transfer_sum](#analytics_transfer_sum) - Sum all transfers across intervals
* [analytics_transfer_largest](#analytics_transfer_largest) - Return the largest number of transfers
* [analytics_transfer_smallest](#analytics_transfer_smallest) - Return the smallest number of transfers
* [analytics_transfer_statuses](#analytics_transfer_statuses) - Count the transfer statuses
* [analytics_accounts_created](#analytics_accounts_created) - Count the number of profiles created by an individual or business

## analytics_transfer_sum

To use this endpoint from the browser, you'll need to specify the `/analytics.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.analytics.analytics_transfer_sum(request={
    "from_": dateutil.parser.isoparse("2024-10-23T21:56:53.874Z"),
    "to": dateutil.parser.isoparse("2024-03-22T07:24:09.774Z"),
    "every": dateutil.parser.isoparse("2022-08-02T13:45:43.177Z"),
    "tz": dateutil.parser.isoparse("2024-11-24T16:07:13.546Z"),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TimeRange](../../models/timerange.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsTransferSumResponse](../../models/analyticstransfersumresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## analytics_transfer_largest

To use this endpoint from the browser, you'll need to specify the `/analytics.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.analytics.analytics_transfer_largest(request={
    "from_": dateutil.parser.isoparse("2022-05-13T01:24:39.253Z"),
    "to": dateutil.parser.isoparse("2023-12-08T18:52:33.102Z"),
    "every": "America/Paramaribo",
    "tz": "America/Dawson",
    "count": 19225,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LimitedTimeRange](../../models/limitedtimerange.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsTransferLargestResponse](../../models/analyticstransferlargestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## analytics_transfer_smallest

To use this endpoint from the browser, you'll need to specify the `/analytics.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.analytics.analytics_transfer_smallest(request={
    "from_": dateutil.parser.isoparse("2022-03-29T21:05:25.175Z"),
    "to": dateutil.parser.isoparse("2022-12-25T22:08:39.409Z"),
    "every": "Atlantic/Faroe",
    "tz": "Antarctica/Casey",
    "count": 618955,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LimitedTimeRange](../../models/limitedtimerange.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsTransferSmallestResponse](../../models/analyticstransfersmallestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## analytics_transfer_statuses

To use this endpoint from the browser, you'll need to specify the `/analytics.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.analytics.analytics_transfer_statuses(request={
    "from_": dateutil.parser.isoparse("2022-06-20T17:04:22.352Z"),
    "to": dateutil.parser.isoparse("2024-03-10T09:19:16.352Z"),
    "every": dateutil.parser.isoparse("2023-07-14T18:48:11.590Z"),
    "tz": dateutil.parser.isoparse("2023-12-28T17:55:34.062Z"),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TimeRange](../../models/timerange.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsTransferStatusesResponse](../../models/analyticstransferstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## analytics_accounts_created

To use this endpoint from the browser, you'll need to specify the `/analytics.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.analytics.analytics_accounts_created(request={
    "from_": dateutil.parser.isoparse("2023-02-24T12:48:15.823Z"),
    "to": dateutil.parser.isoparse("2022-07-16T14:05:26.635Z"),
    "every": dateutil.parser.isoparse("2024-04-18T02:30:09.015Z"),
    "tz": dateutil.parser.isoparse("2023-03-22T16:41:07.299Z"),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TimeRange](../../models/timerange.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsAccountsCreatedResponse](../../models/analyticsaccountscreatedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |