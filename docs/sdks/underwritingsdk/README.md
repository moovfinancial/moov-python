# UnderwritingSDK
(*underwriting*)

## Overview

### Available Operations

* [get_underwriting](#get_underwriting) - Retrieve underwriting associated with a given Moov account. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [update_underwriting](#update_underwriting) - Update the account's underwriting by passing new values for one or more of the fields. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.

## get_underwriting

Retrieve underwriting associated with a given Moov account. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.underwriting.get_underwriting(security=moov.GetUnderwritingSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="32ccafba-5d99-40e5-a8af-d05cc5d73a4e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetUnderwritingSecurity](../../models/getunderwritingsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `account_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `x_moov_version`                                                          | [Optional[models.Versions]](../../models/versions.md)                     | :heavy_minus_sign:                                                        | Specify an API version.                                                   |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Underwriting](../../models/underwriting.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_underwriting

Update the account's underwriting by passing new values for one or more of the fields. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.underwriting.update_underwriting(security=moov.UpdateUnderwritingSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="455b1698-1657-4c75-944b-57db42578d81", average_transaction_size=686, max_transaction_size=927778, average_monthly_transaction_volume=363635, volume_by_customer_type={
        "business_to_business_percentage": 103054,
        "consumer_to_business_percentage": 891201,
    }, card_volume_distribution={
        "ecommerce_percentage": 139066,
        "card_present_percentage": 457019,
        "mail_or_phone_percentage": 477438,
        "debt_repayment_percentage": 372012,
    }, fulfillment={
        "has_physical_goods": False,
        "is_shipping_product": True,
        "shipment_duration_days": 571329,
        "return_policy": moov.ReturnPolicyType.OTHER,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.UpdateUnderwritingSecurity](../../models/updateunderwritingsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `account_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `average_transaction_size`                                                      | *int*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `max_transaction_size`                                                          | *int*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `average_monthly_transaction_volume`                                            | *int*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `volume_by_customer_type`                                                       | [models.VolumeByCustomerType](../../models/volumebycustomertype.md)             | :heavy_check_mark:                                                              | N/A                                                                             |
| `card_volume_distribution`                                                      | [models.CardVolumeDistribution](../../models/cardvolumedistribution.md)         | :heavy_check_mark:                                                              | N/A                                                                             |
| `fulfillment`                                                                   | [models.FulfillmentDetails](../../models/fulfillmentdetails.md)                 | :heavy_check_mark:                                                              | N/A                                                                             |
| `x_moov_version`                                                                | [Optional[models.Versions]](../../models/versions.md)                           | :heavy_minus_sign:                                                              | Specify an API version.                                                         |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.Underwriting](../../models/underwriting.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.GenericError            | 400, 409                       | application/json               |
| models.UpdateUnderwritingError | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |