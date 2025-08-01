# Underwriting
(*underwriting*)

## Overview

### Available Operations

* [get](#get) - Retrieve underwriting associated with a given Moov account. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [save](#save) - Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [upsert](#upsert) - Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

## get

Retrieve underwriting associated with a given Moov account. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnderwriting" method="get" path="/accounts/{accountID}/underwriting" -->
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

    res = moov.underwriting.get(account_id="efe07546-f697-4da5-bf73-d9987efd4cdd")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetUnderwritingResponse](../../models/operations/getunderwritingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## save

Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="saveUnderwriting" method="post" path="/accounts/{accountID}/underwriting" -->
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

    res = moov.underwriting.save(account_id="ffe3ca1b-de3f-4305-8d8c-cfd28f279cad")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                           | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `geographic_reach`                                                                                     | [Optional[components.GeographicReach]](../../models/components/geographicreach.md)                     | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `business_presence`                                                                                    | [Optional[components.BusinessPresence]](../../models/components/businesspresence.md)                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `pending_litigation`                                                                                   | [Optional[components.PendingLitigation]](../../models/components/pendinglitigation.md)                 | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `volume_share_by_customer_type`                                                                        | [Optional[components.VolumeShareByCustomerType]](../../models/components/volumesharebycustomertype.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `collect_funds`                                                                                        | [Optional[components.CollectFunds]](../../models/components/collectfunds.md)                           | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `money_transfer`                                                                                       | [Optional[components.MoneyTransfer]](../../models/components/moneytransfer.md)                         | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `send_funds`                                                                                           | [Optional[components.SendFunds]](../../models/components/sendfunds.md)                                 | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `submission_intent`                                                                                    | [Optional[components.SubmissionIntent]](../../models/components/submissionintent.md)                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.SaveUnderwritingResponse](../../models/operations/saveunderwritingresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.UpsertUnderwritingError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## upsert

Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="upsertUnderwriting" method="put" path="/accounts/{accountID}/underwriting" -->
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

    res = moov.underwriting.upsert(account_id="371bf394-45df-4ba8-a615-ad5483b1f963", average_transaction_size=622191, max_transaction_size=123692, average_monthly_transaction_volume=438164, volume_by_customer_type={
        "business_to_business_percentage": 671399,
        "consumer_to_business_percentage": 482010,
    }, card_volume_distribution={
        "ecommerce_percentage": 47450,
        "card_present_percentage": 146275,
        "mail_or_phone_percentage": 309315,
        "debt_repayment_percentage": 990303,
    }, fulfillment={
        "has_physical_goods": True,
        "is_shipping_product": True,
        "shipment_duration_days": 388451,
        "return_policy": components.ReturnPolicyType.OTHER,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `average_transaction_size`                                                             | *int*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `max_transaction_size`                                                                 | *int*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `average_monthly_transaction_volume`                                                   | *int*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `volume_by_customer_type`                                                              | [components.VolumeByCustomerType](../../models/components/volumebycustomertype.md)     | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `card_volume_distribution`                                                             | [components.CardVolumeDistribution](../../models/components/cardvolumedistribution.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `fulfillment`                                                                          | [components.FulfillmentDetails](../../models/components/fulfillmentdetails.md)         | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpsertUnderwritingResponse](../../models/operations/upsertunderwritingresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.UpdateUnderwritingError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |