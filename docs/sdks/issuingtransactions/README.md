# IssuingTransactions
(*issuing_transactions*)

## Overview

### Available Operations

* [list_authorizations](#list_authorizations) - List issued card authorizations associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get_authorization](#get_authorization) - Retrieves details of an authorization associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [list_authorization_events](#list_authorization_events) - List card network and Moov platform events that affect the authorization and its hold on a wallet balance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [list](#list) - List issued card transactions associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get](#get) - Retrieves details of an issued card transaction associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

## list_authorizations

List issued card authorizations associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

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

    res = moov.issuing_transactions.list_authorizations(account_id="c2c85e2d-634b-4cc0-8c5b-763c22a727b6", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The Moov business account for which cards have been issued.                                          |                                                                                                      |
| `skip`                                                                                               | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | 60                                                                                                   |
| `count`                                                                                              | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | 20                                                                                                   |
| `issued_card_id`                                                                                     | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | Optional ID of the issued card to filter results.                                                    |                                                                                                      |
| `start_date_time`                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                 | :heavy_minus_sign:                                                                                   | Optional date-time which inclusively filters all authorizations created after this date-time.        |                                                                                                      |
| `end_date_time`                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                 | :heavy_minus_sign:                                                                                   | Optional date-time which exclusively filters all authorizations created before this date-time.       |                                                                                                      |
| `statuses`                                                                                           | List[[components.IssuingAuthorizationStatus](../../models/components/issuingauthorizationstatus.md)] | :heavy_minus_sign:                                                                                   | Optional, comma-separated statuses of the authorization to filter results.                           |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.ListIssuedCardAuthorizationsResponse](../../models/operations/listissuedcardauthorizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_authorization

Retrieves details of an authorization associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

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

    res = moov.issuing_transactions.get_authorization(account_id="7fe28e4d-1e30-4ebb-8d22-aae768170b82", authorization_id="8db4b0c4-d99d-4878-bcde-c2700f82e331")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The Moov business account for which cards have been issued.         |
| `authorization_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetIssuedCardAuthorizationResponse](../../models/operations/getissuedcardauthorizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_authorization_events

List card network and Moov platform events that affect the authorization and its hold on a wallet balance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

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

    res = moov.issuing_transactions.list_authorization_events(account_id="e52b1b82-54cb-42aa-911b-6359b8490650", authorization_id="f1a90d72-3787-49c4-a11d-9e7efe0b3763", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The Moov business account for which cards have been issued.         |                                                                     |
| `authorization_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `skip`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 60                                                                  |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListIssuedCardAuthorizationEventsResponse](../../models/operations/listissuedcardauthorizationeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list

List issued card transactions associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

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

    res = moov.issuing_transactions.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | The Moov business account for which cards have been issued.                                       |                                                                                                   |
| `skip`                                                                                            | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               | 60                                                                                                |
| `count`                                                                                           | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               | 20                                                                                                |
| `issued_card_id`                                                                                  | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Optional ID of the issued card to filter results.                                                 |                                                                                                   |
| `start_date_time`                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                              | :heavy_minus_sign:                                                                                | Optional date-time which inclusively filters all card transactions created after this date-time.  |                                                                                                   |
| `end_date_time`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                              | :heavy_minus_sign:                                                                                | Optional date-time which exclusively filters all card transactions created before this date-time. |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[operations.ListIssuedCardTransactionsResponse](../../models/operations/listissuedcardtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves details of an issued card transaction associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.

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

    res = moov.issuing_transactions.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", card_transaction_id="e50f7622-81da-484b-9c66-1c8a99c6b71b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The Moov business account for which cards have been issued.         |
| `card_transaction_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetIssuedCardTransactionResponse](../../models/operations/getissuedcardtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |