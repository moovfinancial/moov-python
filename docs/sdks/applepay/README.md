# ApplePay
(*apple_pay*)

## Overview

### Available Operations

* [register_merchant_domains](#register_merchant_domains) - Add domains to be registered with Apple Pay.

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [update_merchant_domains](#update_merchant_domains) - Add or remove domains to be registered with Apple Pay. 

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [get_merchant_domains](#get_merchant_domains) - Get domains registered with Apple Pay. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.read` scope.
* [create_session](#create_session) - Create a session with Apple Pay to facilitate a payment. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
A successful response from this endpoint should be passed through to Apple Pay unchanged. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [link_token](#link_token) - Connect an Apple Pay token to the specified account. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
The `token` data is defined by Apple Pay and should be passed through from Apple Pay's response unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

## register_merchant_domains

Add domains to be registered with Apple Pay.

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.apple_pay.register_merchant_domains(account_id="133fed79-519d-4b63-99ec-26b95076a45b", domains=[
        "checkout.classbooker.dev",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | ID of the Moov account representing the merchant.                                                |                                                                                                  |
| `display_name`                                                                                   | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | A UTF-8 string to display in the Buy button.                                                     |                                                                                                  |
| `domains`                                                                                        | List[*str*]                                                                                      | :heavy_minus_sign:                                                                               | A unique list of fully-qualified, top-level or sub-domain names where you will accept Apple Pay. | [<br/>"checkout.classbooker.dev"<br/>]                                                           |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.RegisterApplePayMerchantDomainsResponse](../../models/operations/registerapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## update_merchant_domains

Add or remove domains to be registered with Apple Pay. 

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.apple_pay.update_merchant_domains(account_id="b7d68fce-1dbc-4562-93aa-d9ad030c78e6", add_domains=[
        "pay.classbooker.dev",
    ], remove_domains=[
        "checkout.classbooker.dev",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | ID of the Moov account representing the merchant.                          |                                                                            |
| `add_domains`                                                              | List[*str*]                                                                | :heavy_minus_sign:                                                         | A unique list of fully-qualified, top-level or sub-domain names to add.    | [<br/>"pay.classbooker.dev"<br/>]                                          |
| `remove_domains`                                                           | List[*str*]                                                                | :heavy_minus_sign:                                                         | A unique list of fully-qualified, top-level or sub-domain names to remove. | [<br/>"checkout.classbooker.dev"<br/>]                                     |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[operations.UpdateApplePayMerchantDomainsResponse](../../models/operations/updateapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_merchant_domains

Get domains registered with Apple Pay. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.apple_pay.get_merchant_domains(account_id="cd0931b0-e02f-47b3-87fc-0789a05479e9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the merchant.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetApplePayMerchantDomainsResponse](../../models/operations/getapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_session

Create a session with Apple Pay to facilitate a payment. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
A successful response from this endpoint should be passed through to Apple Pay unchanged. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.apple_pay.create_session(account_id="1d911f27-36e5-4497-8e9e-c3ecff1a8ae0", domain="checkout.classbooker.dev", display_name="Lillie.Abbott74")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                | *str*                                                                                                       | :heavy_check_mark:                                                                                          | ID of the Moov account representing the merchant.                                                           |                                                                                                             |
| `domain`                                                                                                    | *str*                                                                                                       | :heavy_check_mark:                                                                                          | A fully qualified top-level or sub-domain name where you will accept Apple Pay. Should not include "https". | checkout.classbooker.dev                                                                                    |
| `display_name`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | A UTF-8 string to display in the Buy button.                                                                |                                                                                                             |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

### Response

**[operations.CreateApplePaySessionResponse](../../models/operations/createapplepaysessionresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409, 422       | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## link_token

Connect an Apple Pay token to the specified account. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
The `token` data is defined by Apple Pay and should be passed through from Apple Pay's response unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.apple_pay.link_token(account_id="f4d3b593-6370-42f3-acf5-eab4393e2a01", token={
        "payment_data": {
            "version": "EC_v1",
            "data": "3+f4oOTwPa6f1UZ6tG...CE=",
            "signature": "MIAGCSqGSIb3DQ.AAAA==",
            "header": {
                "public_key_hash": "l0CnXdMv...D1I=",
                "transaction_id": "32b...4f3",
                "ephemeral_public_key": "MFkwEK...Md==",
            },
        },
        "payment_method": {
            "display_name": "Visa 1234",
            "network": "Visa",
            "type": "debit",
        },
        "transaction_identifier": "32b...4f3",
    }, billing_contact={
        "address_lines": [
            "123 Sesame Street",
        ],
        "locality": "Phoenix",
        "postal_code": "30345",
        "administrative_area": "AZ",
        "country_code": "US",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                               | Type                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                | Description                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                      | ID of the Moov account representing the cardholder.                                                                                                                                                                     |
| `token`                                                                                                                                                                                                                 | [components.LinkApplePayToken](../../models/components/linkapplepaytoken.md)                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                      |   Contains the user's payment information as returned from Apple Pay.<br/><br/>  Refer to [Apple's documentation](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymenttoken) <br/>  for more information. |
| `billing_contact`                                                                                                                                                                                                       | [Optional[components.AppleBillingContact]](../../models/components/applebillingcontact.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                      |   Billing contact information as returned from Apple Pay.<br/>  <br/>  Refer to [Apple's documentation](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentcontact) <br/>  for more information. |
| `retries`                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                     |

### Response

**[operations.LinkApplePayTokenResponse](../../models/operations/linkapplepaytokenresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.GenericError      | 400, 409                 | application/json         |
| errors.LinkApplePayError | 422                      | application/json         |
| errors.APIError          | 4XX, 5XX                 | \*/\*                    |