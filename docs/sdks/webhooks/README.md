# Webhooks

## Overview

### Available Operations

* [list_event_types](#list_event_types) - List all available event types that can be subscribed to.
* [list](#list) - List all webhooks configured for the account.
* [create](#create) - Create a new webhook for the account.
* [get](#get) - Get details of a specific webhook.
* [update](#update) - Update an existing webhook.
* [disable](#disable) - Disable a webhook. Disabled webhooks will no longer receive events.
* [ping](#ping) - Send a test ping to a webhook to verify it is configured correctly.
* [get_secret](#get_secret) - Get the secret key for verifying webhook payloads.

## list_event_types

List all available event types that can be subscribed to.

### Example Usage

<!-- UsageSnippet language="python" operationID="listEventTypes" method="get" path="/event-types" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.list_event_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListEventTypesRequest](../../models/operations/listeventtypesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListEventTypesResponse](../../models/operations/listeventtypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list

List all webhooks configured for the account.

### Example Usage

<!-- UsageSnippet language="python" operationID="listWebhooks" method="get" path="/webhooks" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListWebhooksRequest](../../models/operations/listwebhooksrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListWebhooksResponse](../../models/operations/listwebhooksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new webhook for the account.

### Example Usage

<!-- UsageSnippet language="python" operationID="createWebhook" method="post" path="/webhooks" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.create(url="https://experienced-sailor.biz/", status=components.WebhookStatus.DISABLED, event_types=[], description="overdue bonnet failing")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `url`                                                                            | *str*                                                                            | :heavy_check_mark:                                                               | The URL where webhook events will be sent.                                       |
| `status`                                                                         | [components.WebhookStatus](../../models/components/webhookstatus.md)             | :heavy_check_mark:                                                               | The status of the webhook.                                                       |
| `event_types`                                                                    | List[[components.WebhookEventType](../../models/components/webhookeventtype.md)] | :heavy_check_mark:                                                               | The list of event types this webhook should subscribe to.                        |
| `description`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | A description of the webhook for reference. Can be an empty string.              |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GenericError                 | 400, 409                            | application/json                    |
| errors.CreateWebhookValidationError | 422                                 | application/json                    |
| errors.APIError                     | 4XX, 5XX                            | \*/\*                               |

## get

Get details of a specific webhook.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWebhook" method="get" path="/webhooks/{webhookID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.get(webhook_id="deeb5a05-74d4-40ad-b4be-a9265fd49428")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update an existing webhook.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWebhook" method="put" path="/webhooks/{webhookID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.update(webhook_id="954b566e-0c37-481b-bf92-6cdbd0e47dc0", url="https://nimble-affect.name", status=components.WebhookStatus.ENABLED, event_types=[], description="hmph eyeglasses pink stylish blah")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `webhook_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `url`                                                                            | *str*                                                                            | :heavy_check_mark:                                                               | The URL where webhook events will be sent.                                       |
| `status`                                                                         | [components.WebhookStatus](../../models/components/webhookstatus.md)             | :heavy_check_mark:                                                               | The status of the webhook.                                                       |
| `event_types`                                                                    | List[[components.WebhookEventType](../../models/components/webhookeventtype.md)] | :heavy_check_mark:                                                               | The list of event types this webhook should subscribe to.                        |
| `description`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | A description of the webhook for reference. Can be an empty string.              |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GenericError                 | 400, 409                            | application/json                    |
| errors.UpdateWebhookValidationError | 422                                 | application/json                    |
| errors.APIError                     | 4XX, 5XX                            | \*/\*                               |

## disable

Disable a webhook. Disabled webhooks will no longer receive events.

### Example Usage

<!-- UsageSnippet language="python" operationID="disableWebhook" method="delete" path="/webhooks/{webhookID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.disable(webhook_id="c88929b3-cbb6-4144-923f-e9a5ba645708")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DisableWebhookResponse](../../models/operations/disablewebhookresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## ping

Send a test ping to a webhook to verify it is configured correctly.

### Example Usage

<!-- UsageSnippet language="python" operationID="pingWebhook" method="post" path="/webhooks/{webhookID}/ping" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.ping(webhook_id="87e0ecc6-d6c3-4eeb-99e8-6dbe9212a6a2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.PingWebhookResponse](../../models/operations/pingwebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_secret

Get the secret key for verifying webhook payloads.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWebhookSecret" method="get" path="/webhooks/{webhookID}/secret" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.webhooks.get_secret(webhook_id="1fac81d6-2d5b-4180-8765-81282a450eda")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhookSecretResponse](../../models/operations/getwebhooksecretresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |