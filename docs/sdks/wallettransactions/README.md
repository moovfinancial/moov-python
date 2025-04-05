# WalletTransactions
(*wallet_transactions*)

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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.wallet_transactions.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6", wallet_id="21e27667-18d6-4d46-812e-0aee1b9ddf12", skip=60, count=20)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get details on a specific wallet transaction. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

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

    res = moov.wallet_transactions.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", wallet_id="e50f7622-81da-484b-9c66-1c8a99c6b71b", transaction_id="ecd62b8f-7112-4aaf-90ab-4e43b4cca371")

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