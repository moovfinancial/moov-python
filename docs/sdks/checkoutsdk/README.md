# CheckoutSDK
(*checkout*)

## Overview

<b>Coming soon -</b> Hosted checkout.


### Available Operations

* [create_checkout](#create_checkout) - Create checkout
* [list_checkouts](#list_checkouts) - List checkouts
* [get_checkout](#get_checkout) - Get checkout
* [update_checkout](#update_checkout) - Update checkout
* [disable_checkout](#disable_checkout) - Disable checkout
* [get_checkout_qr_code](#get_checkout_qr_code) - Get QR code for checkout

## create_checkout

Create a checkout that allows an end user to make a payment on Moov's hosted checkout page.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.create_checkout(account_id="46c65cbe-6a25-4fde-a710-624abb99bac0", create_checkout_request={
    "partner_account_id": "e76d386c-3709-47a7-83af-51912a3d5acc",
    "display": {
        "title": "<value>",
        "description": "nerve represent although joyously executor shell",
        "call_to_action": "<value>",
    },
    "transfer": {
        "destination": {
            "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
            "card_details": {
                "dynamic_descriptor": "WhlBdy *Yoga 11-12",
            },
            "ach_details": {
                "company_entry_description": "Gym Dues",
                "originating_company_name": "Whole Body Fit",
            },
        },
        "amount": {
            "currency": "USD",
            "value": 1204,
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `account_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | ID of the account.                                                    |
| `create_checkout_request`                                             | [models.CreateCheckoutRequest](../../models/createcheckoutrequest.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateCheckoutResponse](../../models/createcheckoutresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## list_checkouts

List all the checkouts created under a Moov account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.list_checkouts(account_id="6b62cb18-17aa-48ea-be36-e3e245d35b3d")

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

**[models.ListCheckoutsResponse](../../models/listcheckoutsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_checkout

Retrieve a checkout by code.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.get_checkout(account_id="ecdf464a-abde-493e-8398-3318da6bc559", checkout_code="uc7ZYKrMhi")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `checkout_code`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Unique code of the checkout.                                        | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCheckoutResponse](../../models/getcheckoutresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_checkout

Update a checkout by code.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.update_checkout(account_id="5a2c6478-c2cb-447e-8752-6c84d1002454", checkout_code="uc7ZYKrMhi", update_checkout_request={
    "transfer": {
        "destination": {
            "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
            "card_details": {
                "dynamic_descriptor": "WhlBdy *Yoga 11-12",
            },
            "ach_details": {
                "company_entry_description": "Gym Dues",
                "originating_company_name": "Whole Body Fit",
            },
        },
        "amount": {
            "currency": "USD",
            "value": 1204,
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `account_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | ID of the account.                                                    |                                                                       |
| `checkout_code`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | Unique code of the checkout.                                          | uc7ZYKrMhi                                                            |
| `update_checkout_request`                                             | [models.UpdateCheckoutRequest](../../models/updatecheckoutrequest.md) | :heavy_check_mark:                                                    | N/A                                                                   |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.UpdateCheckoutResponse](../../models/updatecheckoutresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## disable_checkout

Disable a checkout by code rendering it unusable.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.disable_checkout(account_id="9868a400-24d2-4d92-a925-1a7d475b7b57", checkout_code="uc7ZYKrMhi")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `checkout_code`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Unique code of the checkout.                                        | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DisableCheckoutResponse](../../models/disablecheckoutresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_checkout_qr_code

Retrieve the checkout link encoded in a QR code. Use the `Accept` header to specify
the format of the response. Supported formats are `application/json` and `image/png`.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.checkout.get_checkout_qr_code(account_id="cbf5ab2f-6b53-4023-83de-b2b409367bd0", checkout_code="uc7ZYKrMhi")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `checkout_code`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Unique code of the checkout.                                        | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCheckoutQRCodeResponse](../../models/getcheckoutqrcoderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400, 409         | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |