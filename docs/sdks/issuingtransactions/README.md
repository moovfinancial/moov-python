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

    res = moov.issuing_transactions.list_authorizations(account_id="8b15de20-a7c4-4720-a646-88309ab5093d", skip=60, count=20)

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

    res = moov.issuing_transactions.get_authorization(account_id="8c490d50-8951-4810-9506-ecd5648c2a39", authorization_id="f037a459-fbd3-47b9-8181-09847ea9f557")

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

    res = moov.issuing_transactions.list_authorization_events(account_id="78666549-e9e4-4769-8bd4-1456f277ddce", authorization_id="fcc21f8e-61f5-4554-a253-362fd57052bb", skip=60, count=20)

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

    res = moov.issuing_transactions.list(account_id="b137f097-2f49-4fc7-afb4-b59a6fe762cd", skip=60, count=20)

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

    res = moov.issuing_transactions.get(account_id="4bebfda4-7627-4fb8-9945-5ef57c25a867", card_transaction_id="33615eaf-e358-4f62-ac49-f7cca27d44ba")

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