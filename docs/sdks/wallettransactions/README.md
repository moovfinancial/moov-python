# WalletTransactions
(*wallet_transactions*)

## Overview

### Available Operations

* [list_wallet_transactions](#list_wallet_transactions) - List all the transactions associated with a particular Moov wallet. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_wallet_transaction](#get_wallet_transaction) - Get details on a specific wallet transaction. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To use this endpoint from a browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## list_wallet_transactions

List all the transactions associated with a particular Moov wallet. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.wallet_transactions.list_wallet_transactions(security=operations.ListWalletTransactionsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="2d736837-1618-4c4a-9e51-aa9dd394b389", wallet_id="99432d06-8ac3-4c17-afc1-a12a328564ac", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                 | [operations.ListWalletTransactionsSecurity](../../models/operations/listwallettransactionssecurity.md)     | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `wallet_id`                                                                                                | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `x_moov_version`                                                                                           | [Optional[components.Versions]](../../models/components/versions.md)                                       | :heavy_minus_sign:                                                                                         | Specify an API version.                                                                                    |                                                                                                            |
| `skip`                                                                                                     | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        | 60                                                                                                         |
| `count`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        | 20                                                                                                         |
| `transaction_type`                                                                                         | [Optional[components.WalletTransactionType]](../../models/components/wallettransactiontype.md)             | :heavy_minus_sign:                                                                                         | Optional parameter to filter by transaction type.                                                          |                                                                                                            |
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

**[List[components.WalletTransaction]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_wallet_transaction

Get details on a specific wallet transaction. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To use this endpoint from a browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.wallet_transactions.get_wallet_transaction(security=operations.GetWalletTransactionSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="a5040923-7566-4f60-af63-86465493f971", wallet_id="a49156a6-65e8-4c24-a71a-eca54c2c3855", transaction_id="8b5c4f2a-2bb8-4145-b0ea-69212338b5a1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `security`                                                                                         | [operations.GetWalletTransactionSecurity](../../models/operations/getwallettransactionsecurity.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `account_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `wallet_id`                                                                                        | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `transaction_id`                                                                                   | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `x_moov_version`                                                                                   | [Optional[components.Versions]](../../models/components/versions.md)                               | :heavy_minus_sign:                                                                                 | Specify an API version.                                                                            |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[components.WalletTransaction](../../models/components/wallettransaction.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |