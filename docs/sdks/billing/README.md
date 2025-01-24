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
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.billing.list_fee_plan_agreements(security=operations.ListFeePlanAgreementsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="4c49ae91-2b32-4a4d-91bf-f062f3c2f38d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.ListFeePlanAgreementsSecurity](../../models/operations/listfeeplanagreementssecurity.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `x_moov_version`                                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                                 | :heavy_minus_sign:                                                                                   | Specify an API version.                                                                              |
| `agreement_id`                                                                                       | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | A comma-separated list of agreement IDs to filter the results by.                                    |
| `status`                                                                                             | List[[components.FeePlanAgreementStatus](../../models/components/feeplanagreementstatus.md)]         | :heavy_minus_sign:                                                                                   | A comma-separated list of statuses to filter the results by.                                         |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[List[components.FeePlanAgreement]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_fee_plan_agreements

Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.billing.create_fee_plan_agreements(security=operations.CreateFeePlanAgreementsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="19962eb8-00cd-44e5-8a66-a1ebaf88c2fe", plan_id="b97c2d59-80c5-49ac-b1fc-40e3a81d8daf")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `security`                                                                                               | [operations.CreateFeePlanAgreementsSecurity](../../models/operations/createfeeplanagreementssecurity.md) | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `account_id`                                                                                             | *str*                                                                                                    | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `plan_id`                                                                                                | *str*                                                                                                    | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `x_moov_version`                                                                                         | [Optional[components.Versions]](../../models/components/versions.md)                                     | :heavy_minus_sign:                                                                                       | Specify an API version.                                                                                  |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[components.FeePlanAgreement](../../models/components/feeplanagreement.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.FeePlanAgreementError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_fee_plans

List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.billing.list_fee_plans(security=operations.ListFeePlansSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="ac8fa716-4b75-4902-b296-d734524ca45c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.ListFeePlansSecurity](../../models/operations/listfeeplanssecurity.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `account_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `x_moov_version`                                                                   | [Optional[components.Versions]](../../models/components/versions.md)               | :heavy_minus_sign:                                                                 | Specify an API version.                                                            |
| `plan_i_ds`                                                                        | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | A comma-separated list of plan IDs to filter the results by.                       |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[List[components.FeePlan]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing

List all partner pricing plans available for use by an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.billing.list_partner_pricing(security=operations.ListPartnerPricingSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="85f15b07-5c44-4302-ab6f-d22f8d45b7f4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `security`                                                                                     | [operations.ListPartnerPricingSecurity](../../models/operations/listpartnerpricingsecurity.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `account_id`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `x_moov_version`                                                                               | [Optional[components.Versions]](../../models/components/versions.md)                           | :heavy_minus_sign:                                                                             | Specify an API version.                                                                        |
| `plan_i_ds`                                                                                    | List[*str*]                                                                                    | :heavy_minus_sign:                                                                             | A comma-separated list of plan IDs to filter the results by.                                   |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[List[components.PartnerPricing]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing_agreements

List all partner pricing agreements associated with an account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.billing.list_partner_pricing_agreements(security=operations.ListPartnerPricingAgreementsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="9366921a-25de-4c52-8ec6-4cd4ef557223")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                         | [operations.ListPartnerPricingAgreementsSecurity](../../models/operations/listpartnerpricingagreementssecurity.md) | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `account_id`                                                                                                       | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `x_moov_version`                                                                                                   | [Optional[components.Versions]](../../models/components/versions.md)                                               | :heavy_minus_sign:                                                                                                 | Specify an API version.                                                                                            |
| `agreement_id`                                                                                                     | List[*str*]                                                                                                        | :heavy_minus_sign:                                                                                                 | A comma-separated list of agreement IDs to filter the results by.                                                  |
| `status`                                                                                                           | List[[components.FeePlanAgreementStatus](../../models/components/feeplanagreementstatus.md)]                       | :heavy_minus_sign:                                                                                                 | A comma-separated list of statuses to filter the results by.                                                       |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[List[components.PartnerPricingAgreement]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |