# IssuingTransactions
(*issuing_transactions*)

## Overview

### Available Operations

* [list_account_issued_card_authorizations](#list_account_issued_card_authorizations) - Get account authorizations
* [get_account_issued_card_authorization](#get_account_issued_card_authorization) - Retrieve an authorization
* [list_authorization_events](#list_authorization_events) - Get authorization events
* [list_account_issued_card_transactions](#list_account_issued_card_transactions) - Get account card transactions
* [get_account_issued_card_transaction](#get_account_issued_card_transaction) - Retrieve an issued card transaction

## list_account_issued_card_authorizations

List issued card authorizations associated with a Moov account.


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.issuing_transactions.list_account_issued_card_authorizations(request={
    "account_id": "b745bc6b-779d-4129-9d1d-3d8076cebfbf",
    "issued_card_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "start_date_time": "2009-11-10T23:00:00Z",
    "end_date_time": "2009-11-13T01:00:00Z",
    "statuses": moov.IssuedCardAuthorizationStatus.DECLINED,
    "count": 10,
    "skip": 10,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                       | [models.ListAccountIssuedCardAuthorizationsRequest](../../models/listaccountissuedcardauthorizationsrequest.md) | :heavy_check_mark:                                                                                              | The request object to use for the request.                                                                      |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.ListAccountIssuedCardAuthorizationsResponse](../../models/listaccountissuedcardauthorizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_account_issued_card_authorization

Retrieves details of an authorization associated with a specific Moov account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.issuing_transactions.get_account_issued_card_authorization(account_id="2800d9c8-992a-4082-89f3-a9b101be3293", authorization_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `authorization_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | ID of the authorization.                                            | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetAccountIssuedCardAuthorizationResponse](../../models/getaccountissuedcardauthorizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_authorization_events

List card network and Moov platform events that affect the authorization and its hold on a wallet balance.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.issuing_transactions.list_authorization_events(account_id="e52b1b82-54cb-42aa-911b-6359b8490650", authorization_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", count=10, skip=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `account_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | ID of the account.                                                       |                                                                          |
| `authorization_id`                                                       | *str*                                                                    | :heavy_check_mark:                                                       | ID of the authorization.                                                 | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                     |
| `count`                                                                  | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Optional parameter to limit the number of results in the query.          | 10                                                                       |
| `skip`                                                                   | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | The number of items to offset before starting to collect the result set. | 10                                                                       |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |                                                                          |

### Response

**[models.ListAuthorizationEventsResponse](../../models/listauthorizationeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_account_issued_card_transactions

List issued card transactions associated with a Moov account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.issuing_transactions.list_account_issued_card_transactions(request={
    "account_id": "84bc75bd-7804-4e31-99ad-dbaa54a62a3f",
    "count": 10,
    "skip": 10,
    "start_date_time": "2009-11-10T23:00:00Z",
    "end_date_time": "2009-11-13T01:00:00Z",
    "issued_card_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.ListAccountIssuedCardTransactionsRequest](../../models/listaccountissuedcardtransactionsrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.ListAccountIssuedCardTransactionsResponse](../../models/listaccountissuedcardtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_account_issued_card_transaction

Retrieves details of an issued card transaction associated with a specific Moov account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.issuing_transactions.get_account_issued_card_transaction(account_id="87f7a4fc-25fd-44a9-810f-fcdba2be4fef", card_transaction_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `card_transaction_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | ID of the card transaction.                                         | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetAccountIssuedCardTransactionResponse](../../models/getaccountissuedcardtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |