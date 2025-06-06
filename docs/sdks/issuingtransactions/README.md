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
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.issuing_transactions.list_authorizations(account_id="6465d95a-e945-4a49-8983-d74faa135bb4", skip=60, count=20)

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
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.issuing_transactions.get_authorization(account_id="0ccac2cc-6692-44a9-b0d1-35a1892c2db2", authorization_id="d9ee8dde-b1eb-492f-bea1-d8e09bccbc52")

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
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.issuing_transactions.list_authorization_events(account_id="f30f8cb3-64d8-4a5f-a427-965317fa559a", authorization_id="e6a0946d-f3d8-451e-9b1c-5bc346a95dd6", skip=60, count=20)

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
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.issuing_transactions.list(account_id="4efcb497-f915-4b6e-b973-e5e5bcc1fd34", skip=60, count=20)

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
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.issuing_transactions.get(account_id="b2b6e23c-a5aa-46a9-adb7-d12876e47288", card_transaction_id="d5a1aab9-eb96-409a-ab95-88ac99cf00a5")

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