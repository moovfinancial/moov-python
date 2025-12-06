# CardIssuing

## Overview

### Available Operations

* [request](#request) - Request a virtual card be issued.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.
* [list](#list) - List Moov issued cards existing for the account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get](#get) - Retrieve a single issued card associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [update](#update) - Update a Moov issued card.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.
* [get_full](#get_full) - Get issued card with PAN, CVV, and expiration. 

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope.

## request

Request a virtual card be issued.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="requestCard" method="post" path="/issuing/{accountID}/issued-cards" -->
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

    res = moov.card_issuing.request(account_id="d9ac71ae-fccb-4dfc-9fed-710ca654e3ed", funding_wallet_id="fd98e3b2-696f-4f67-9250-17b3474ababf", authorized_user={
        "first_name": "Milton",
        "last_name": "Stiedemann",
        "birth_date": {
            "day": 9,
            "month": 11,
            "year": 1989,
        },
    }, form_factor=components.IssuedCardFormFactor.VIRTUAL, expiration={
        "month": "01",
        "year": "21",
    }, controls={
        "velocity_limits": [
            {
                "amount": 10000,
                "interval": components.IssuingIntervalLimit.PER_TRANSACTION,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The Moov business account for which the card is to be issued.                                                                       |                                                                                                                                     |
| `funding_wallet_id`                                                                                                                 | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |
| `authorized_user`                                                                                                                   | [components.CreateAuthorizedUser](../../models/components/createauthorizeduser.md)                                                  | :heavy_check_mark:                                                                                                                  | Fields for identifying an authorized individual.                                                                                    |                                                                                                                                     |
| `form_factor`                                                                                                                       | [components.IssuedCardFormFactor](../../models/components/issuedcardformfactor.md)                                                  | :heavy_check_mark:                                                                                                                  | Specifies the type of spend card to be issued. Presently supports virtual only, providing a digital number without a physical card. |                                                                                                                                     |
| `memo`                                                                                                                              | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | An optional descriptive name for the card.                                                                                          |                                                                                                                                     |
| `expiration`                                                                                                                        | [Optional[components.CardExpiration]](../../models/components/cardexpiration.md)                                                    | :heavy_minus_sign:                                                                                                                  | The expiration date of the card or token.                                                                                           | {<br/>"month": "01",<br/>"year": "21"<br/>}                                                                                         |
| `controls`                                                                                                                          | [Optional[components.IssuingControls]](../../models/components/issuingcontrols.md)                                                  | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[operations.RequestCardResponse](../../models/operations/requestcardresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.GenericError     | 400                     | application/json        |
| errors.RequestCardError | 422                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |

## list

List Moov issued cards existing for the account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listIssuedCards" method="get" path="/issuing/{accountID}/issued-cards" -->
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

    res = moov.card_issuing.list(account_id="17c958e0-3abe-46e5-8afb-98742f1fb8ac", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The Moov business account for which the cards have been issued.                                                           |                                                                                                                           |
| `skip`                                                                                                                    | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       | 60                                                                                                                        |
| `count`                                                                                                                   | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       | 20                                                                                                                        |
| `states`                                                                                                                  | List[[components.IssuedCardState](../../models/components/issuedcardstate.md)]                                            | :heavy_minus_sign:                                                                                                        | Optional, comma-separated states to filter the Moov list issued cards response. For example `active,pending-verification` |                                                                                                                           |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.ListIssuedCardsResponse](../../models/operations/listissuedcardsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a single issued card associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIssuedCard" method="get" path="/issuing/{accountID}/issued-cards/{issuedCardID}" -->
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

    res = moov.card_issuing.get(account_id="4fde8da4-b6c5-4379-82a2-4ff6a742e41a", issued_card_id="d04885c9-ea6b-43a7-9186-63d9fbd57716")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The Moov business account for which the card was issued.            |
| `issued_card_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetIssuedCardResponse](../../models/operations/getissuedcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a Moov issued card.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateIssuedCard" method="patch" path="/issuing/{accountID}/issued-cards/{issuedCardID}" -->
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

    res = moov.card_issuing.update(account_id="44db31bc-2813-424b-9b8c-2d3f5f1300e3", issued_card_id="69ca2a7e-7bbc-4176-9d0c-2a1aa7143006", authorized_user={
        "birth_date": {
            "day": 9,
            "month": 11,
            "year": 1989,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The Moov business account for which the card was issued.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `issued_card_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `state`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[components.IssuedCardState]](../../models/components/issuedcardstate.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The `state` represents the operational status of an issued card. A card can only approve incoming authorizations if it is in an active state.<br/><br/>- `active`: The card is operational and approves authorizations. Generally becomes active shortly after card creation.<br/>- `inactive`: The card cannot approve authorizations. This is currently a temporary state assigned post-creation during the activation process.<br/>- `closed`: The card is permanently deactivated and cannot approve authorizations. A card can be closed by request or when it expires.<br/>- `pending-verification`: Awaiting additional authorized user verification before the card can be activated. |
| `memo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `authorized_user`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.CreateAuthorizedUserUpdate]](../../models/components/createauthorizeduserupdate.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Fields for identifying an authorized individual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Response

**[operations.UpdateIssuedCardResponse](../../models/operations/updateissuedcardresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.UpdateIssuedCardError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## get_full

Get issued card with PAN, CVV, and expiration. 

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFullIssuedCard" method="get" path="/issuing/{accountID}/issued-cards/{issuedCardID}/details" -->
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

    res = moov.card_issuing.get_full(account_id="512052fb-5e2c-4d24-98dd-fa893c9d8a03", issued_card_id="087ecc51-11fe-4471-a3bb-44f20c1e87a9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The Moov business account for which the card was issued.            |
| `issued_card_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetFullIssuedCardResponse](../../models/operations/getfullissuedcardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |