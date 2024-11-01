# Capabilities
(*capabilities*)

## Overview

Capabilities determine what a Moov account can do. Each capability has specific [requirements](https://docs.moov.io/guides/accounts/capabilities/requirements/), depending on risk and compliance standards associated with different account activities. For example, there are more information requirements for a business that wants to charge other accounts than for an individual who simply wants to receive funds.

When you request a capability, we list the information requirements for that capability. Once you submit the required information, we need to verify the data. Because of this, a requested capability may not immediately become active. Note, if an account requests and is approved for `send-funds` or `collect-funds`, the `wallet` capability is automatically enabled as well. For more detailed information on capabilities and capability IDs, read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/).


### Available Operations

* [get_capability](#get_capability) - Get capability for account
* [disable_capability](#disable_capability) - Disable a capability for an account.
* [list_capabilities](#list_capabilities) - List capabilities for account
* [add_capabilities](#add_capabilities) - Request capabilities

## get_capability

Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.capabilities.get_capability(account_id="15fbc94d-721f-44a3-b5fb-77f58657305f", capability_id=moov.CapabilityID.TRANSFERS)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `capability_id`                                                     | [models.CapabilityID](../../models/capabilityid.md)                 | :heavy_check_mark:                                                  | The requested capability identifier.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCapabilityResponse](../../models/getcapabilityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disable_capability

Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.capabilities.disable_capability(account_id="c57b48d7-4182-4632-a345-eeed5a742b0d", capability_id=moov.CapabilityID.CARD_ISSUING)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `capability_id`                                                     | [models.CapabilityID](../../models/capabilityid.md)                 | :heavy_check_mark:                                                  | The requested capability identifier.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DisableCapabilityResponse](../../models/disablecapabilityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_capabilities

Retrieve all the capabilities an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.capabilities.list_capabilities(account_id="c236a258-0a99-455d-9fbb-2312bc028cd2")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListCapabilitiesResponse](../../models/listcapabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## add_capabilities

Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/capabilities.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.capabilities.add_capabilities(account_id="f48b82c3-158f-4a65-9070-bd22afd441ea", add_capability_request={
    "capabilities": [
        moov.CapabilityID.TRANSFERS,
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `add_capability_request`                                            | [models.AddCapabilityRequest](../../models/addcapabilityrequest.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddCapabilitiesResponse](../../models/addcapabilitiesresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.CapabilityRequestError | 409                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |