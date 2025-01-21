# IssuingTransactions
(*issuing_transactions*)

## Overview

### Available Operations

* [list_issued_card_authorizations](#list_issued_card_authorizations) - List issued card authorizations associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.
* [get_issued_card_authorization](#get_issued_card_authorization) - Retrieves details of an authorization associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.
* [list_issued_card_authorization_events](#list_issued_card_authorization_events) - List card network and Moov platform events that affect the authorization and its hold on a wallet balance.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.
* [list_issued_card_transactions](#list_issued_card_transactions) - List issued card transactions associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.
* [get_issued_card_transaction](#get_issued_card_transaction) - Retrieves details of an issued card transaction associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

## list_issued_card_authorizations

List issued card authorizations associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.issuing_transactions.list_issued_card_authorizations(security=moov.ListIssuedCardAuthorizationsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="8b15de20-a7c4-4720-a646-88309ab5093d", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ListIssuedCardAuthorizationsSecurity](../../models/listissuedcardauthorizationssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |                                                                                                     |
| `account_id`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | The Moov business account for which cards have been issued.                                         |                                                                                                     |
| `x_moov_version`                                                                                    | [Optional[models.Versions]](../../models/versions.md)                                               | :heavy_minus_sign:                                                                                  | Specify an API version.                                                                             |                                                                                                     |
| `skip`                                                                                              | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 | 60                                                                                                  |
| `count`                                                                                             | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 | 20                                                                                                  |
| `issued_card_id`                                                                                    | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Optional ID of the issued card to filter results.                                                   |                                                                                                     |
| `start_date_time`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                | :heavy_minus_sign:                                                                                  | Optional date-time which inclusively filters all authorizations created after this date-time.       |                                                                                                     |
| `end_date_time`                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                | :heavy_minus_sign:                                                                                  | Optional date-time which exclusively filters all authorizations created before this date-time.      |                                                                                                     |
| `statuses`                                                                                          | List[[models.IssuingAuthorizationStatus](../../models/issuingauthorizationstatus.md)]               | :heavy_minus_sign:                                                                                  | Optional, comma-separated statuses of the authorization to filter results.                          |                                                                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

### Response

**[List[models.IssuedCardAuthorization]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_issued_card_authorization

Retrieves details of an authorization associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.issuing_transactions.get_issued_card_authorization(security=moov.GetIssuedCardAuthorizationSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="8c490d50-8951-4810-9506-ecd5648c2a39", authorization_id="f037a459-fbd3-47b9-8181-09847ea9f557")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetIssuedCardAuthorizationSecurity](../../models/getissuedcardauthorizationsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `account_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | The Moov business account for which cards have been issued.                                     |
| `authorization_id`                                                                              | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `x_moov_version`                                                                                | [Optional[models.Versions]](../../models/versions.md)                                           | :heavy_minus_sign:                                                                              | Specify an API version.                                                                         |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.IssuedCardAuthorization](../../models/issuedcardauthorization.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_issued_card_authorization_events

List card network and Moov platform events that affect the authorization and its hold on a wallet balance.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.issuing_transactions.list_issued_card_authorization_events(security=moov.ListIssuedCardAuthorizationEventsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="78666549-e9e4-4769-8bd4-1456f277ddce", authorization_id="fcc21f8e-61f5-4554-a253-362fd57052bb", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.ListIssuedCardAuthorizationEventsSecurity](../../models/listissuedcardauthorizationeventssecurity.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `account_id`                                                                                                  | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The Moov business account for which cards have been issued.                                                   |                                                                                                               |
| `authorization_id`                                                                                            | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `x_moov_version`                                                                                              | [Optional[models.Versions]](../../models/versions.md)                                                         | :heavy_minus_sign:                                                                                            | Specify an API version.                                                                                       |                                                                                                               |
| `skip`                                                                                                        | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           | 60                                                                                                            |
| `count`                                                                                                       | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           | 20                                                                                                            |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[List[models.IssuedCardAuthorizationEvent]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_issued_card_transactions

List issued card transactions associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.issuing_transactions.list_issued_card_transactions(security=moov.ListIssuedCardTransactionsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="b137f097-2f49-4fc7-afb4-b59a6fe762cd", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.ListIssuedCardTransactionsSecurity](../../models/listissuedcardtransactionssecurity.md)   | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `account_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | The Moov business account for which cards have been issued.                                       |                                                                                                   |
| `x_moov_version`                                                                                  | [Optional[models.Versions]](../../models/versions.md)                                             | :heavy_minus_sign:                                                                                | Specify an API version.                                                                           |                                                                                                   |
| `skip`                                                                                            | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               | 60                                                                                                |
| `count`                                                                                           | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               | 20                                                                                                |
| `issued_card_id`                                                                                  | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Optional ID of the issued card to filter results.                                                 |                                                                                                   |
| `start_date_time`                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                              | :heavy_minus_sign:                                                                                | Optional date-time which inclusively filters all card transactions created after this date-time.  |                                                                                                   |
| `end_date_time`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                              | :heavy_minus_sign:                                                                                | Optional date-time which exclusively filters all card transactions created before this date-time. |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[List[models.IssuedCardTransaction]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_issued_card_transaction

Retrieves details of an issued card transaction associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify 
the `/accounts/{accountID}/issued-cards.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.issuing_transactions.get_issued_card_transaction(security=moov.GetIssuedCardTransactionSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="4bebfda4-7627-4fb8-9945-5ef57c25a867", card_transaction_id="33615eaf-e358-4f62-ac49-f7cca27d44ba")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetIssuedCardTransactionSecurity](../../models/getissuedcardtransactionsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `account_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | The Moov business account for which cards have been issued.                                 |
| `card_transaction_id`                                                                       | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `x_moov_version`                                                                            | [Optional[models.Versions]](../../models/versions.md)                                       | :heavy_minus_sign:                                                                          | Specify an API version.                                                                     |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.IssuedCardTransaction](../../models/issuedcardtransaction.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |