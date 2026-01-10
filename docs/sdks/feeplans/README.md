# FeePlans

## Overview

### Available Operations

* [list_fee_plan_agreements](#list_fee_plan_agreements) - List all fee plan agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [create_fee_plan_agreements](#create_fee_plan_agreements) - Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [list_fee_plans](#list_fee_plans) - List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [list_fee_revenue](#list_fee_revenue) - Used by a partner. Retrieve revenue generated from merchant fees.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [retrieve_fees](#retrieve_fees) - Retrieve fees assessed to an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_fees_fetch](#list_fees_fetch) - List fees associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_partner_pricing](#list_partner_pricing) - List all partner pricing plans available for use by an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [list_partner_pricing_agreements](#list_partner_pricing_agreements) - List all partner pricing agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [list_residuals](#list_residuals) - List all residuals associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [get_residual](#get_residual) - Get a residual associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [list_residual_fees](#list_residual_fees) - List all fees associated with a residual.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

## list_fee_plan_agreements

List all fee plan agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFeePlanAgreements" method="get" path="/accounts/{accountID}/fee-plan-agreements" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_fee_plan_agreements(account_id="93c43634-5477-42a7-972d-01fa76a09e17", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |
| `skip`                                                                                       | *Optional[int]*                                                                              | :heavy_minus_sign:                                                                           | N/A                                                                                          | 60                                                                                           |
| `count`                                                                                      | *Optional[int]*                                                                              | :heavy_minus_sign:                                                                           | N/A                                                                                          | 20                                                                                           |
| `agreement_id`                                                                               | List[*str*]                                                                                  | :heavy_minus_sign:                                                                           | A comma-separated list of agreement IDs to filter the results by.                            |                                                                                              |
| `status`                                                                                     | List[[components.FeePlanAgreementStatus](../../models/components/feeplanagreementstatus.md)] | :heavy_minus_sign:                                                                           | A comma-separated list of statuses to filter the results by.                                 |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[operations.ListFeePlanAgreementsResponse](../../models/operations/listfeeplanagreementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_fee_plan_agreements

Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createFeePlanAgreements" method="post" path="/accounts/{accountID}/fee-plan-agreements" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.create_fee_plan_agreements(account_id="409c6b4b-e622-40c2-9dc4-fb494e555723", plan_id="19801f96-ea27-4610-b4d1-8c6b46f37928")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `plan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateFeePlanAgreementsResponse](../../models/operations/createfeeplanagreementsresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.FeePlanAgreementError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_fee_plans

List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFeePlans" method="get" path="/accounts/{accountID}/fee-plans" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_fee_plans(account_id="b3d59179-f74e-4ee8-b123-33220b3c7d4b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `plan_i_ds`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | A comma-separated list of plan IDs to filter the results by.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListFeePlansResponse](../../models/operations/listfeeplansresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_fee_revenue

Used by a partner. Retrieve revenue generated from merchant fees.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFeeRevenue" method="get" path="/accounts/{accountID}/fee-revenue" -->
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

    res = moov.fee_plans.list_fee_revenue(account_id="795465fb-f955-40e7-9d48-4a6d6fbdbdf2", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The Partner's AccountID.                                                         |                                                                                  |
| `skip`                                                                           | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 60                                                                               |
| `count`                                                                          | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 20                                                                               |
| `transfer_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional transfer ID to filter the results by.                                   |                                                                                  |
| `dispute_id`                                                                     | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional dispute ID to filter the results by.                                    |                                                                                  |
| `residual_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional residual ID to filter the results by.                                   |                                                                                  |
| `start_date_time`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to inclusively filter all fees created after this date-time.  |                                                                                  |
| `end_date_time`                                                                  | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to exclusively filter all fees created before this date-time. |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.ListFeeRevenueResponse](../../models/operations/listfeerevenueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_fees

Retrieve fees assessed to an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="retrieveFees" method="get" path="/accounts/{accountID}/fees" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.retrieve_fees(account_id="89daf02d-b6b3-4fbf-b20d-5bf967324682", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `transfer_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional transfer ID to filter the results by.                                   |                                                                                  |
| `dispute_id`                                                                     | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional dispute ID to filter the results by.                                    |                                                                                  |
| `residual_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional residual ID to filter the results by.                                   |                                                                                  |
| `start_date_time`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to inclusively filter all fees created after this date-time.  |                                                                                  |
| `end_date_time`                                                                  | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to exclusively filter all fees created before this date-time. |                                                                                  |
| `skip`                                                                           | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 60                                                                               |
| `count`                                                                          | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 20                                                                               |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.RetrieveFeesResponse](../../models/operations/retrievefeesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_fees_fetch

List fees associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFeesFetch" method="post" path="/accounts/{accountID}/fees/.fetch" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_fees_fetch(account_id="55c34e26-269d-4872-8e42-0fa83e3f4b10")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `fee_i_ds`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListFeesFetchResponse](../../models/operations/listfeesfetchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing

List all partner pricing plans available for use by an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPartnerPricing" method="get" path="/accounts/{accountID}/partner-pricing" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_partner_pricing(account_id="600637f9-c38a-473f-b909-0d5ac537b8a5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `plan_i_ds`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | A comma-separated list of plan IDs to filter the results by.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListPartnerPricingResponse](../../models/operations/listpartnerpricingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_partner_pricing_agreements

List all partner pricing agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPartnerPricingAgreements" method="get" path="/accounts/{accountID}/partner-pricing-agreements" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_partner_pricing_agreements(account_id="123bfe5e-2288-4146-9d8a-4c07264c3758", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |
| `skip`                                                                                       | *Optional[int]*                                                                              | :heavy_minus_sign:                                                                           | N/A                                                                                          | 60                                                                                           |
| `count`                                                                                      | *Optional[int]*                                                                              | :heavy_minus_sign:                                                                           | N/A                                                                                          | 20                                                                                           |
| `agreement_id`                                                                               | List[*str*]                                                                                  | :heavy_minus_sign:                                                                           | A comma-separated list of agreement IDs to filter the results by.                            |                                                                                              |
| `status`                                                                                     | List[[components.FeePlanAgreementStatus](../../models/components/feeplanagreementstatus.md)] | :heavy_minus_sign:                                                                           | A comma-separated list of statuses to filter the results by.                                 |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[operations.ListPartnerPricingAgreementsResponse](../../models/operations/listpartnerpricingagreementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_residuals

List all residuals associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listResiduals" method="get" path="/accounts/{accountID}/residuals" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_residuals(account_id="8b40b967-ae12-4851-8be2-7b0c39978ce7", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `skip`                                                                                           | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | N/A                                                                                              | 60                                                                                               |
| `count`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | N/A                                                                                              | 20                                                                                               |
| `start_date_time`                                                                                | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Optional date-time to inclusively filter all residuals with a period start after this date-time. |                                                                                                  |
| `end_date_time`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Optional date-time to exclusively filter all residuals with a period end before this date-time.  |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.ListResidualsResponse](../../models/operations/listresidualsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_residual

Get a residual associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getResidual" method="get" path="/accounts/{accountID}/residuals/{residualID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.get_residual(account_id="4c308842-45d1-49c1-98be-7299848b1e20", residual_id="5f30e43d-1fa8-4834-8788-05a3c27a40d4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `residual_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetResidualResponse](../../models/operations/getresidualresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_residual_fees

List all fees associated with a residual.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listResidualFees" method="get" path="/accounts/{accountID}/residuals/{residualID}/fees" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.fee_plans.list_residual_fees(account_id="6b95293f-c3e7-42b5-98b7-fd9cc8d49685", residual_id="8ecb1a63-25e0-41e7-a9c7-bb8a1cf63d1c", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `residual_id`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `skip`                                                                           | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 60                                                                               |
| `count`                                                                          | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              | 20                                                                               |
| `start_date_time`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to inclusively filter all fees created after this date-time.  |                                                                                  |
| `end_date_time`                                                                  | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Optional date-time to exclusively filter all fees created before this date-time. |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.ListResidualFeesResponse](../../models/operations/listresidualfeesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |