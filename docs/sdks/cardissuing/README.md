# CardIssuing
(*card_issuing*)

## Overview

A Moov wallet can serve as a funding source for issuing virtual cards. Note that we currently only issue Visa cards. Virtual cards can then be used to spend funds from the wallet.

<em> The `card-issuing` and `wallet` capabilities are required to be enabled before any card issuing functionality is available. Moov is in a private beta with select customers for card issuing.</em>


### Available Operations

* [request_card](#request_card) - Request card
* [list_issued_cards](#list_issued_cards) - List issued cards
* [get_issued_card](#get_issued_card) - Get issued card
* [update_issued_card](#update_issued_card) - Update issued card
* [get_full_issued_card](#get_full_issued_card) - Get full card details

## request_card

Request a virtual card be created.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.card_issuing.request_card(account_id="df7610a6-b14e-4eee-9a55-1890b6b3207c", request_card={
    "funding_wallet_id": "<id>",
    "authorized_user": {
        "first_name": "Jane",
        "last_name": "Doe",
        "birth_date": {
            "day": 9,
            "month": 11,
            "year": 1989,
        },
    },
    "form_factor": moov.IssuedCardFormFactor.VIRTUAL,
    "expiration": {
        "month": "01",
        "year": "21",
    },
    "controls": {
        "velocity_limits": [
            {
                "amount": 10000,
                "interval": moov.IssuingIntervalLimit.PER_TRANSACTION,
            },
        ],
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
| `request_card`                                                      | [models.RequestCard](../../models/requestcard.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestCardResponse](../../models/requestcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_issued_cards

List Moov issued cards existing for the account.
<br><br> All supported query parameters are optional.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.card_issuing.list_issued_cards(account_id="33bbd03b-931d-4e6d-b831-8698f4aee791", states=moov.IssuedCardState.ACTIVE, count=10, skip=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | ID of the account.                                                                                                         |                                                                                                                            |
| `states`                                                                                                                   | [Optional[models.IssuedCardState]](../../models/issuedcardstate.md)                                                        | :heavy_minus_sign:                                                                                                         | Optional, comma-separated states to filter the Moov list issued cards response. For example `active,pending-verification`<br/> | active                                                                                                                     |
| `count`                                                                                                                    | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Optional parameter to limit the number of results in the query.                                                            | 10                                                                                                                         |
| `skip`                                                                                                                     | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | The number of items to offset before starting to collect the result set.                                                   | 10                                                                                                                         |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |

### Response

**[models.ListIssuedCardsResponse](../../models/listissuedcardsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_issued_card

Retrieve a single issued card associated with a Moov account.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.card_issuing.get_issued_card(account_id="c63d9bae-2097-4bfa-8ac7-e9e8dff6e9ae", issued_card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `issued_card_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the issued card.                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetIssuedCardResponse](../../models/getissuedcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_issued_card

Update a Moov issued card.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.card_issuing.update_issued_card(account_id="fc445a8c-5b64-4ab9-ba30-5bdb0ffc02b0", issued_card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", update_issued_card={
    "authorized_user": {
        "first_name": "Jane",
        "last_name": "Doe",
        "birth_date": {
            "day": 9,
            "month": 11,
            "year": 1989,
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `issued_card_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the issued card.                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `update_issued_card`                                                | [models.UpdateIssuedCard](../../models/updateissuedcard.md)         | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateIssuedCardResponse](../../models/updateissuedcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_full_issued_card

Get issued card with PAN, CVV, and expiration. Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.card_issuing.get_full_issued_card(account_id="f03c4c3e-2685-44e6-8d4b-0d5bd082a301", issued_card_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `issued_card_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the issued card.                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetFullIssuedCardResponse](../../models/getfullissuedcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |