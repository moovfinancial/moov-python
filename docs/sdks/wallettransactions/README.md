# WalletTransactions

## Overview

### Available Operations

* [list](#list) - List all the transactions associated with a particular Moov wallet. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](#get) - Get details on a specific wallet transaction. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

## list

List all the transactions associated with a particular Moov wallet. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listWalletTransactions" method="get" path="/accounts/{accountID}/wallets/{walletID}/transactions" -->
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

    res = moov.wallet_transactions.list(account_id="69e4529b-baf0-4f00-877b-123cfd9d6116", wallet_id="4f971587-62fe-42c9-bc61-7409d9c8660c", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `wallet_id`                                                                                                | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `skip`                                                                                                     | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        | 60                                                                                                         |
| `count`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        | 20                                                                                                         |
| `transaction_type`                                                                                         | [Optional[components.WalletTransactionType]](../../models/components/wallettransactiontype.md)             | :heavy_minus_sign:                                                                                         | Optional parameter to filter by transaction type.                                                          |                                                                                                            |
| `transaction_types`                                                                                        | List[[components.WalletTransactionType](../../models/components/wallettransactiontype.md)]                 | :heavy_minus_sign:                                                                                         | Optional, comma-separated parameter to filter by transaction types.                                        |                                                                                                            |
| `source_type`                                                                                              | [Optional[components.WalletTransactionSourceType]](../../models/components/wallettransactionsourcetype.md) | :heavy_minus_sign:                                                                                         | Optional parameter to filter by source type (i.e. transfer, dispute, issuing-transaction).                 |                                                                                                            |
| `source_id`                                                                                                | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Optional parameter to filter by source ID.                                                                 |                                                                                                            |
| `status`                                                                                                   | [Optional[components.WalletTransactionStatus]](../../models/components/wallettransactionstatus.md)         | :heavy_minus_sign:                                                                                         | Optional parameter to filter by status (`pending` or `completed`).                                         |                                                                                                            |
| `created_start_date_time`                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                       | :heavy_minus_sign:                                                                                         | Optional date-time which inclusively filters all transactions created after this date-time.                |                                                                                                            |
| `created_end_date_time`                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                       | :heavy_minus_sign:                                                                                         | Optional date-time which exclusively filters all transactions created before this date-time.               |                                                                                                            |
| `completed_start_date_time`                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                       | :heavy_minus_sign:                                                                                         | Optional date-time which inclusively filters all transactions completed after this date-time.              |                                                                                                            |
| `completed_end_date_time`                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                       | :heavy_minus_sign:                                                                                         | Optional date-time which exclusively filters all transactions completed before this date-time.             |                                                                                                            |
| `sweep_id`                                                                                                 | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Optional ID to filter for transactions accrued in a sweep.                                                 |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[operations.ListWalletTransactionsResponse](../../models/operations/listwallettransactionsresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.ListWalletTransactionsValidationError | 422                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## get

Get details on a specific wallet transaction. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWalletTransaction" method="get" path="/accounts/{accountID}/wallets/{walletID}/transactions/{transactionID}" -->
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

    res = moov.wallet_transactions.get(account_id="f0b02d73-10dc-42e6-8030-fd78fcbc114f", wallet_id="03db97f6-c308-4595-8f43-fd247f1bd3f2", transaction_id="e0a32cf5-5758-49ba-83da-75bf02c9c6d7")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWalletTransactionResponse](../../models/operations/getwallettransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |