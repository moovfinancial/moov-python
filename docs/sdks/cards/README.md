# Cards
(*cards*)

## Overview

You can link credit or debit cards to Moov accounts. You can use a card as a source for making transfers, which charges the card. To link a card to a Moov account and avoid some of the burden of PCI compliance, use the [card link Moov Drop](https://docs.moov.io/moovjs/drops/card-link). You cannot add a card via the Dashboard. If you're linking a card via API, you must provide Moov with a copy of your PCI attestation of compliance. When testing cards, use the designated [card numbers for test mode](https://docs.moov.io/guides/set-up-your-account/test-mode/#card-acceptance). You must contact Moov before going live in production with cards. Read our guide on [cards](https://docs.moov.io/guides/sources/cards/) for more information.

### Available Operations

* [card](#card) - Link card
* [list_cards](#list_cards) - List cards
* [get_card](#get_card) - Get card
* [update_card](#update_card) - Update card
* [delete_card](#delete_card) - Disable card
* [register_apple_pay_merchant_domains](#register_apple_pay_merchant_domains) - Register Apple Pay domains
* [update_apple_pay_merchant_domains](#update_apple_pay_merchant_domains) - Update Apple Pay domains
* [get_apple_pay_merchant_domains](#get_apple_pay_merchant_domains) - Get Apple Pay domains
* [create_apple_pay_session](#create_apple_pay_session) - Create Apple Pay session
* [link_apple_pay_token](#link_apple_pay_token) - Link Apple Pay token

## card

Link a card to an existing Moov account. 

Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/#link-a-card) to learn more.

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance. 

During card linking, the provided data will be verified by submitting a $0 authorization (account verification) request. 
If `merchantAccountID` is provided, the authorization request will contain that account's statement descriptor and address. 
Otherwise, the platform account's profile will be used. If no statement descriptor has been set, the authorization will 
use the account's name instead.

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked 
card is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment 
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.write` scope
when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.card(account_id="5f70656d-6e6c-4a9e-b884-3e6f476645ae", card_request={
    "card_number": "4111111111111111",
    "expiration": {
        "month": "01",
        "year": "21",
    },
    "card_cvv": "0123",
    "billing_address": {
        "postal_code": "80301",
        "address_line1": "123 Main Street",
        "address_line2": "Apt 302",
        "city": "Boulder",
        "state_or_province": "CO",
        "country": "US",
    },
    "holder_name": "Jules Jackson",
    "e2ee": {
        "token": "eyJhbGciOiJFQ0RILUVTK0EyNTZLVyIsImVuYyI6IkEyNTZHQ00iLCJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTUyMSIsIngiOiJBS0NYVDM1WVdvTm8wbzExNy1SU0dqUGg3alN1NjFmLUhnYkx1dW0xVG1ueTRlcW5yX2hyU0hpY0w1d3gwODRCWDBRZjVTdEtkRUoydzY2ZUJqWHprRV9OIiwieSI6IkFIMEJfT2RaYTQtbG43dGJ4M3VBdlc1NDNQRE9HUXBCTDloRFFNWjlTQXNfOW05UWN3dnhRd1hrb1VrM3VzT1FnVV9ySVFrNFRoZ1NTUzV4UlhKcm5ZaTkifSwia2lkIjoiYmRvV3pLekpKUGw0TVFIaENDa05WYTZlZ1dmYi02V1haSjZKTFZqQ0hWMD0ifQ.HalyoHsfufBJEODd2lD9ThQvvVWw3b2kgWDLHGxmHhMv8rODyLL_Ug.rpQP178t8Ed_pUU2.Sn9UFeVoegAxiMUv11q7l3M0y9YHSLYi2n_JB7n7Pc777_47-icfaxstJemT0IC81w.akkq1EBxzWkBr4vEomSpWA",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                            | ID of the Moov account representing the cardholder.                                                                                                                                                                                                                                                                                                                           |
| `card_request`                                                                                                                                                                                                                                                                                                                                                                | [models.CardRequest](../../models/cardrequest.md)                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                           |
| `x_wait_for`                                                                                                                                                                                                                                                                                                                                                                  | [Optional[models.SchemasWaitFor]](../../models/schemaswaitfor.md)                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                            | Optional header to wait for certain events, such as the creation of a payment method, to occur before returning a response.<br/><br/>When this header is set to `payment-method`, the response will include any payment methods that were created for the newly <br/>linked card in the `paymentMethods` field. Otherwise, the `paymentMethods` field will be omitted from the response.<br/> |
| `retries`                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                           |

### Response

**[models.CardResponse](../../models/cardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_cards

List all the active cards associated with a Moov account. Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/) to learn more.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.list_cards(account_id="5881119b-63c7-492b-8c20-09d0fca99676")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the cardholder.                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListCardsResponse](../../models/listcardsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_card

Fetch a specific card associated with a Moov account. Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.get_card(account_id="21f0d82e-dc9b-4e80-ac2a-99b6babfebd7", card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the cardholder.                 |                                                                     |
| `card_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the card.                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCardResponse](../../models/getcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_card

Update a linked card and/or resubmit it for verification. If a value is provided for CVV, 
a new verification ($0 authorization) will be submitted for the card. Updating the expiration date or 
address will update the information stored on file for the card but will not be verified. <br> 
Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/#reverify-a-card) to learn more.
Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance. 
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.update_card(account_id="a960061d-fb6d-4929-99b5-c96c672840f6", card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", card_update_request={
    "expiration": {
        "month": "01",
        "year": "21",
    },
    "card_cvv": "123",
    "holder_name": "Jules Jackson",
    "billing_address": {
        "address_line1": "123 Main Street",
        "address_line2": "Apt 302",
        "city": "Boulder",
        "state_or_province": "CO",
        "postal_code": "80301",
        "country": "US",
    },
    "e2ee": {
        "token": "eyJhbGciOiJFQ0RILUVTK0EyNTZLVyIsImVuYyI6IkEyNTZHQ00iLCJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTUyMSIsIngiOiJBS0NYVDM1WVdvTm8wbzExNy1SU0dqUGg3alN1NjFmLUhnYkx1dW0xVG1ueTRlcW5yX2hyU0hpY0w1d3gwODRCWDBRZjVTdEtkRUoydzY2ZUJqWHprRV9OIiwieSI6IkFIMEJfT2RaYTQtbG43dGJ4M3VBdlc1NDNQRE9HUXBCTDloRFFNWjlTQXNfOW05UWN3dnhRd1hrb1VrM3VzT1FnVV9ySVFrNFRoZ1NTUzV4UlhKcm5ZaTkifSwia2lkIjoiYmRvV3pLekpKUGw0TVFIaENDa05WYTZlZ1dmYi02V1haSjZKTFZqQ0hWMD0ifQ.HalyoHsfufBJEODd2lD9ThQvvVWw3b2kgWDLHGxmHhMv8rODyLL_Ug.rpQP178t8Ed_pUU2.Sn9UFeVoegAxiMUv11q7l3M0y9YHSLYi2n_JB7n7Pc777_47-icfaxstJemT0IC81w.akkq1EBxzWkBr4vEomSpWA",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the cardholder.                 |                                                                     |
| `card_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the card.                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `card_update_request`                                               | [models.CardUpdateRequest](../../models/cardupdaterequest.md)       | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateCardResponse](../../models/updatecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_card

Disables a card associated with a Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.delete_card(account_id="9db0a196-7baa-4ed0-b5eb-cb15e0955c40", card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the cardholder.                 |                                                                     |
| `card_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the card.                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteCardResponse](../../models/deletecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## register_apple_pay_merchant_domains

Add domains to be registered with Apple Pay.
<br><br> Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) with Apple.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.register_apple_pay_merchant_domains(account_id="133fed79-519d-4b63-99ec-26b95076a45b", register_apple_pay_merchant_domains={
    "display_name": "Example Merchant",
    "domains": [
        "checkout.classbooker.dev",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `account_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the Moov account acting as a merchant in a card transaction.                        |
| `register_apple_pay_merchant_domains`                                                     | [models.RegisterApplePayMerchantDomains](../../models/registerapplepaymerchantdomains.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.RegisterApplePayMerchantDomainsResponse](../../models/registerapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_apple_pay_merchant_domains

Add or remove domains to be registered with Apple Pay. 
<br><br> Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) with Apple.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.update_apple_pay_merchant_domains(account_id="b7d68fce-1dbc-4562-93aa-d9ad030c78e6", update_apple_pay_merchant_domains={
    "add_domains": [
        "pay.classbooker.dev",
    ],
    "remove_domains": [
        "checkout.classbooker.dev",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `account_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | ID of the Moov account acting as a merchant in a card transaction.                    |
| `update_apple_pay_merchant_domains`                                                   | [models.UpdateApplePayMerchantDomains](../../models/updateapplepaymerchantdomains.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.UpdateApplePayMerchantDomainsResponse](../../models/updateapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_apple_pay_merchant_domains

Get domains registered with Apple Pay. Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/apple-pay.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.get_apple_pay_merchant_domains(account_id="cd0931b0-e02f-47b3-87fc-0789a05479e9")

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

**[models.GetApplePayMerchantDomainsResponse](../../models/getapplepaymerchantdomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_apple_pay_session

Create a session with Apple Pay to facilitate a payment. Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
A successful response from this endpoint should be passed through to Apple Pay unchanged. 
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.create_apple_pay_session(account_id="9107b11d-911f-4273-86e5-497e9ec3ecff", create_apple_pay_session={
    "domain": "checkout.classbooker.dev",
    "display_name": "Example Merchant",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `account_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | ID of the Moov account acting as a merchant in a card transaction.    |
| `create_apple_pay_session`                                            | [models.CreateApplePaySession](../../models/createapplepaysession.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateApplePaySessionResponse](../../models/createapplepaysessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## link_apple_pay_token

Connect an Apple Pay token to the specified account. Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
The `token` data is defined by Apple Pay and should be passed through from Apple Pay's response unmodified.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/cards.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.cards.link_apple_pay_token(account_id="f4d3b593-6370-42f3-acf5-eab4393e2a01", link_apple_pay={
    "token": {
        "payment_data": {
            "version": "EC_v1",
            "data": "3+f4oOTwPa6f1UZ6tG...CE=",
            "signature": "MIAGCSqGSIb3DQ.AAAA==",
            "header": {
                "ephemeral_public_key": "MFkwEK...Md==",
                "public_key_hash": "l0CnXdMv...D1I=",
                "transaction_id": "32b...4f3",
            },
        },
        "payment_method": {
            "display_name": "Visa 1234",
            "network": "Visa",
            "type": "debit",
        },
        "transaction_identifier": "32b...4f3",
    },
    "billing_contact": {
        "address_lines": [
            "123 Sesame Street",
        ],
        "locality": "Phoenix",
        "postal_code": "30345",
        "administrative_area": "AZ",
        "country_code": "US",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the Moov account representing the cardholder.                 |
| `link_apple_pay`                                                    | [models.LinkApplePay](../../models/linkapplepay.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LinkApplePayTokenResponse](../../models/linkapplepaytokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |