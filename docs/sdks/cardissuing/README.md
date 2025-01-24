# CardIssuing
(*card_issuing*)

## Overview

### Available Operations

* [request_card](#request_card) - Request a virtual card be issued.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [list_issued_cards](#list_issued_cards) - List Moov issued cards existing for the account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_issued_card](#get_issued_card) - Retrieve a single issued card associated with a Moov account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [update_issued_card](#update_issued_card) - Update a Moov issued card.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_full_issued_card](#get_full_issued_card) - Get issued card with PAN, CVV, and expiration. 

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

## request_card

Request a virtual card be issued.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.card_issuing.request_card(security=operations.RequestCardSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="9c0ff49b-9aaf-4815-b4a4-3e412558f6bc", funding_wallet_id="df7610a6-b14e-4eee-9a55-1890b6b3207c", authorized_user={
        "first_name": "Tanya",
        "last_name": "Flatley",
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
| `security`                                                                                                                          | [operations.RequestCardSecurity](../../models/operations/requestcardsecurity.md)                                                    | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |
| `account_id`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The Moov business account for which the card is to be issued.                                                                       |                                                                                                                                     |
| `funding_wallet_id`                                                                                                                 | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |
| `authorized_user`                                                                                                                   | [components.CreateAuthorizedUser](../../models/components/createauthorizeduser.md)                                                  | :heavy_check_mark:                                                                                                                  | Fields for identifying an authorized individual.                                                                                    |                                                                                                                                     |
| `form_factor`                                                                                                                       | [components.IssuedCardFormFactor](../../models/components/issuedcardformfactor.md)                                                  | :heavy_check_mark:                                                                                                                  | Specifies the type of spend card to be issued. Presently supports virtual only, providing a digital number without a physical card. |                                                                                                                                     |
| `x_moov_version`                                                                                                                    | [Optional[components.Versions]](../../models/components/versions.md)                                                                | :heavy_minus_sign:                                                                                                                  | Specify an API version.                                                                                                             |                                                                                                                                     |
| `memo`                                                                                                                              | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | An optional descriptive name for the card.                                                                                          |                                                                                                                                     |
| `expiration`                                                                                                                        | [Optional[components.CardExpiration]](../../models/components/cardexpiration.md)                                                    | :heavy_minus_sign:                                                                                                                  | The expiration date of the card or token.                                                                                           | {<br/>"month": "01",<br/>"year": "21"<br/>}                                                                                         |
| `controls`                                                                                                                          | [Optional[components.IssuingControls]](../../models/components/issuingcontrols.md)                                                  | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[components.IssuedCard](../../models/components/issuedcard.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.GenericError     | 400                     | application/json        |
| errors.RequestCardError | 422                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |

## list_issued_cards

List Moov issued cards existing for the account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.card_issuing.list_issued_cards(security=operations.ListIssuedCardsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="33bbd03b-931d-4e6d-b831-8698f4aee791", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                | [operations.ListIssuedCardsSecurity](../../models/operations/listissuedcardssecurity.md)                                  | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |                                                                                                                           |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The Moov business account for which the cards have been issued.                                                           |                                                                                                                           |
| `x_moov_version`                                                                                                          | [Optional[components.Versions]](../../models/components/versions.md)                                                      | :heavy_minus_sign:                                                                                                        | Specify an API version.                                                                                                   |                                                                                                                           |
| `skip`                                                                                                                    | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       | 60                                                                                                                        |
| `count`                                                                                                                   | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       | 20                                                                                                                        |
| `states`                                                                                                                  | List[[components.IssuedCardState](../../models/components/issuedcardstate.md)]                                            | :heavy_minus_sign:                                                                                                        | Optional, comma-separated states to filter the Moov list issued cards response. For example `active,pending-verification` |                                                                                                                           |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[List[components.IssuedCard]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_issued_card

Retrieve a single issued card associated with a Moov account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.card_issuing.get_issued_card(security=operations.GetIssuedCardSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="c63d9bae-2097-4bfa-8ac7-e9e8dff6e9ae", issued_card_id="aa0c86df-7f7d-4200-9ee4-24ba8870a7d4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.GetIssuedCardSecurity](../../models/operations/getissuedcardsecurity.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `account_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | The Moov business account for which the card was issued.                             |
| `issued_card_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `x_moov_version`                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                 | :heavy_minus_sign:                                                                   | Specify an API version.                                                              |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[components.IssuedCard](../../models/components/issuedcard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_issued_card

Update a Moov issued card.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    moov.card_issuing.update_issued_card(security=operations.UpdateIssuedCardSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="fc445a8c-5b64-4ab9-ba30-5bdb0ffc02b0", issued_card_id="064f9e03-fc5f-4a7d-83d2-2ec946f77ff2", authorized_user={
        "birth_date": {
            "day": 9,
            "month": 11,
            "year": 1989,
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [operations.UpdateIssuedCardSecurity](../../models/operations/updateissuedcardsecurity.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The Moov business account for which the card was issued.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `issued_card_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `x_moov_version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Specify an API version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `state`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[components.IssuedCardState]](../../models/components/issuedcardstate.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The `state` represents the operational status of an issued card. A card can only approve incoming authorizations if it is in an active state.<br/><br/>- `active`: The card is operational and approves authorizations. Generally becomes active shortly after card creation.<br/>- `inactive`: The card cannot approve authorizations. This is currently a temporary state assigned post-creation during the activation process.<br/>- `closed`: The card is permanently deactivated and cannot approve authorizations. A card can be closed by request or when it expires.<br/>- `pending-verification`: Awaiting additional authorized user verification before the card can be activated. |
| `memo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `authorized_user`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.CreateAuthorizedUserUpdate]](../../models/components/createauthorizeduserupdate.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Fields for identifying an authorized individual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.UpdateIssuedCardError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## get_full_issued_card

Get issued card with PAN, CVV, and expiration. 

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.card_issuing.get_full_issued_card(security=operations.GetFullIssuedCardSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="f03c4c3e-2685-44e6-8d4b-0d5bd082a301", issued_card_id="1da6b593-679e-44ab-a9e4-6db6db4b8f46")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.GetFullIssuedCardSecurity](../../models/operations/getfullissuedcardsecurity.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | The Moov business account for which the card was issued.                                     |
| `issued_card_id`                                                                             | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `x_moov_version`                                                                             | [Optional[components.Versions]](../../models/components/versions.md)                         | :heavy_minus_sign:                                                                           | Specify an API version.                                                                      |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[components.FullIssuedCard](../../models/components/fullissuedcard.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |