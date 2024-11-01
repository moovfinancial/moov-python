# UnderwritingSDK
(*underwriting*)

## Overview

[Underwriting](https://docs.moov.io/guides/accounts/underwriting) is a tool Moov uses to understand a business’s profile before allowing them to collect funds on our platform. This profile includes information like a description of the company or the merchant’s business model, the industry they operate in, and transaction volume. Through underwriting, we can understand and prevent unnecessary financial risk for Moov and those transacting on our platform. Note that underwriting can be instant, but in some cases make take around 2 business days before approval.


### Available Operations

* [get_underwriting](#get_underwriting) - Retrieve underwriting details
* [update_underwriting](#update_underwriting) - Update underwriting details

## get_underwriting

Retrieve underwriting associated with a given Moov account. Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.underwriting.get_underwriting(account_id="32ccafba-5d99-40e5-a8af-d05cc5d73a4e")

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

**[models.GetUnderwritingResponse](../../models/getunderwritingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_underwriting

Update the account's underwriting by passing new values for one or more of the fields. Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. <br><br> To use this endpoint from a browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.underwriting.update_underwriting(account_id="0e51e277-5c09-4f45-a5b1-6981657c7544", underwriting_request={
    "average_transaction_size": 10000,
    "max_transaction_size": 50000,
    "average_monthly_transaction_volume": 250000,
    "volume_by_customer_type": {
        "business_to_business_percentage": 20,
        "consumer_to_business_percentage": 20,
    },
    "card_volume_distribution": {
        "ecommerce_percentage": 20,
        "card_present_percentage": 20,
        "mail_or_phone_percentage": 20,
        "debt_repayment_percentage": 20,
    },
    "fulfillment": {
        "has_physical_goods": True,
        "is_shipping_product": True,
        "shipment_duration_days": 7,
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `underwriting_request`                                              | [models.UnderwritingRequest](../../models/underwritingrequest.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateUnderwritingResponse](../../models/updateunderwritingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |