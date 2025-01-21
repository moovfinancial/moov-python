# Billing
(*billing*)

## Overview

### Available Operations

* [list_fee_plan_agreements](#list_fee_plan_agreements) - List all fee plan agreements associated with an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [create_fee_plan_agreements](#create_fee_plan_agreements) - Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.
* [list_fee_plans](#list_fee_plans) - List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [list_partner_pricing](#list_partner_pricing) - List all partner pricing plans available for use by an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [list_partner_pricing_agreements](#list_partner_pricing_agreements) - List all partner pricing agreements associated with an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

## list_fee_plan_agreements

List all fee plan agreements associated with an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.billing.list_fee_plan_agreements(security=moov.ListFeePlanAgreementsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="4c49ae91-2b32-4a4d-91bf-f062f3c2f38d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.ListFeePlanAgreementsSecurity](../../models/listfeeplanagreementssecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `account_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `x_moov_version`                                                                      | [Optional[models.Versions]](../../models/versions.md)                                 | :heavy_minus_sign:                                                                    | Specify an API version.                                                               |
| `agreement_id`                                                                        | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | A comma-separated list of agreement IDs to filter the results by.                     |
| `status`                                                                              | List[[models.FeePlanAgreementStatus](../../models/feeplanagreementstatus.md)]         | :heavy_minus_sign:                                                                    | A comma-separated list of statuses to filter the results by.                          |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[List[models.FeePlanAgreement]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_fee_plan_agreements

Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.billing.create_fee_plan_agreements(security=moov.CreateFeePlanAgreementsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="19962eb8-00cd-44e5-8a66-a1ebaf88c2fe", plan_id="b97c2d59-80c5-49ac-b1fc-40e3a81d8daf")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.CreateFeePlanAgreementsSecurity](../../models/createfeeplanagreementssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `account_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `plan_id`                                                                                 | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `x_moov_version`                                                                          | [Optional[models.Versions]](../../models/versions.md)                                     | :heavy_minus_sign:                                                                        | Specify an API version.                                                                   |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.FeePlanAgreement](../../models/feeplanagreement.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.GenericError          | 400, 409                     | application/json             |
| models.FeePlanAgreementError | 422                          | application/json             |
| models.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_fee_plans

List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.billing.list_fee_plans(security=moov.ListFeePlansSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="ac8fa716-4b75-4902-b296-d734524ca45c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ListFeePlansSecurity](../../models/listfeeplanssecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `plan_i_ds`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | A comma-separated list of plan IDs to filter the results by.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.FeePlan]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing

List all partner pricing plans available for use by an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.billing.list_partner_pricing(security=moov.ListPartnerPricingSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="85f15b07-5c44-4302-ab6f-d22f8d45b7f4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.ListPartnerPricingSecurity](../../models/listpartnerpricingsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `account_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `x_moov_version`                                                                | [Optional[models.Versions]](../../models/versions.md)                           | :heavy_minus_sign:                                                              | Specify an API version.                                                         |
| `plan_i_ds`                                                                     | List[*str*]                                                                     | :heavy_minus_sign:                                                              | A comma-separated list of plan IDs to filter the results by.                    |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.PartnerPricing]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing_agreements

List all partner pricing agreements associated with an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.billing.list_partner_pricing_agreements(security=moov.ListPartnerPricingAgreementsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="9366921a-25de-4c52-8ec6-4cd4ef557223")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ListPartnerPricingAgreementsSecurity](../../models/listpartnerpricingagreementssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `account_id`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `x_moov_version`                                                                                    | [Optional[models.Versions]](../../models/versions.md)                                               | :heavy_minus_sign:                                                                                  | Specify an API version.                                                                             |
| `agreement_id`                                                                                      | List[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | A comma-separated list of agreement IDs to filter the results by.                                   |
| `status`                                                                                            | List[[models.FeePlanAgreementStatus](../../models/feeplanagreementstatus.md)]                       | :heavy_minus_sign:                                                                                  | A comma-separated list of statuses to filter the results by.                                        |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[List[models.PartnerPricingAgreement]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |