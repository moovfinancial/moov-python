# MoovInternal
(*moov_internal*)

## Overview

### Available Operations

* [redeem_onboarding_invite](#redeem_onboarding_invite) - Redeem onboarding invite
* [get_network_i_ds](#get_network_i_ds) - Get network IDs of an account
* [list_fee_plans](#list_fee_plans) - List fee plans
* [create_fee_plan_agreement](#create_fee_plan_agreement) - Create fee plan agreement
* [list_fee_plan_agreements](#list_fee_plan_agreements) - List fee plan agreements
* [list_partner_pricing](#list_partner_pricing) - List partner pricing plans
* [list_partner_pricing_agreements](#list_partner_pricing_agreements) - List partner pricing agreements
* [create_checkout](#create_checkout) - Create checkout
* [list_checkouts](#list_checkouts) - List checkouts
* [get_checkout](#get_checkout) - Get checkout
* [update_checkout](#update_checkout) - Update checkout
* [disable_checkout](#disable_checkout) - Disable checkout
* [get_checkout_qr_code](#get_checkout_qr_code) - Get QR code for checkout

## redeem_onboarding_invite

Redeem an onboarding invite, connecting the recipient's account to the inviting account.
If successful, the caller will be redirected to the Moov dashboard.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.redeem_onboarding_invite(code="N1IA5eWYNh", x_account_id="3fa85f64-5717-4562-b3fc-2c963f66afa6")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The unique code that identifies the onboarding invite.              | N1IA5eWYNh                                                          |
| `x_account_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the account that's redeeming the invite.                  | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RedeemOnboardingInviteResponse](../../models/redeemonboardinginviteresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## get_network_i_ds

Retrieves network IDs for the specified Moov account.
<br><br> To use this endpoint from the browser, you'll will need to specify the `/accounts/{accountID}/profile.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.get_network_i_ds(account_id="339abc33-d99f-4819-9041-8ec9409fc3c4")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account acting as a merchant in a card transaction.  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNetworkIDsResponse](../../models/getnetworkidsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_fee_plans

List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.list_fee_plans(account_id="ac8fa716-4b75-4902-b296-d734524ca45c", plan_i_ds="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `plan_i_ds`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A comma-separated list of plan IDs to filter the results by.        | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListFeePlansResponse](../../models/listfeeplansresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_fee_plan_agreement

Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.create_fee_plan_agreement(account_id="e2d7ba05-745c-4808-82d4-6ebc7d8704ab", request_body={
    "plan_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                      | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | ID of the account.                                                                                                                |
| `request_body`                                                                                                                    | [models.CreateFeePlanAgreementCreateFeePlanAgreementRequest](../../models/createfeeplanagreementcreatefeeplanagreementrequest.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.CreateFeePlanAgreementResponse](../../models/createfeeplanagreementresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_fee_plan_agreements

List all fee plan agreements associated with an account.


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.list_fee_plan_agreements(account_id="4c49ae91-2b32-4a4d-91bf-f062f3c2f38d", agreement_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", status=moov.AgreementStatus.ACTIVE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `agreement_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A comma-separated list of agreement IDs to filter the results by.   | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `status`                                                            | [Optional[models.AgreementStatus]](../../models/agreementstatus.md) | :heavy_minus_sign:                                                  | A comma-separated list of statuses to filter the results by.        | active                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListFeePlanAgreementsResponse](../../models/listfeeplanagreementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing

List all partner pricing plans available for use by an account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.list_partner_pricing(account_id="85f15b07-5c44-4302-ab6f-d22f8d45b7f4", plan_i_ds="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `plan_i_ds`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A comma-separated list of plan IDs to filter the results by.        | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPartnerPricingResponse](../../models/listpartnerpricingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing_agreements

List all partner pricing agreements associated with an account.


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.list_partner_pricing_agreements(account_id="9366921a-25de-4c52-8ec6-4cd4ef557223", agreement_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", status=moov.AgreementStatus.ACTIVE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `agreement_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A comma-separated list of agreement IDs to filter the results by.   | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `status`                                                            | [Optional[models.AgreementStatus]](../../models/agreementstatus.md) | :heavy_minus_sign:                                                  | A comma-separated list of statuses to filter the results by.        | active                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPartnerPricingAgreementsResponse](../../models/listpartnerpricingagreementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_checkout

Create a checkout that allows an end user to make a payment on Moov's hosted checkout page.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.moov_internal.create_checkout(account_id="46c65cbe-6a25-4fde-a710-624abb99bac0", create_checkout_request={
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

res = s.moov_internal.list_checkouts(account_id="6b62cb18-17aa-48ea-be36-e3e245d35b3d")

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

res = s.moov_internal.get_checkout(account_id="ecdf464a-abde-493e-8398-3318da6bc559", checkout_code="uc7ZYKrMhi")

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

res = s.moov_internal.update_checkout(account_id="5a2c6478-c2cb-447e-8752-6c84d1002454", checkout_code="uc7ZYKrMhi", update_checkout_request={
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

res = s.moov_internal.disable_checkout(account_id="9868a400-24d2-4d92-a925-1a7d475b7b57", checkout_code="uc7ZYKrMhi")

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

res = s.moov_internal.get_checkout_qr_code(account_id="cbf5ab2f-6b53-4023-83de-b2b409367bd0", checkout_code="uc7ZYKrMhi")

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