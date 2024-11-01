# WalletTransactions
(*wallet_transactions*)

## Overview

Wallet transactions provide insight into funds that move in and out of an account’s wallet. For each Moov transfer, we create a corresponding transaction that represents how that initial source impacted a wallet. Read more about [wallet transactions](https://docs.moov.io/guides/wallets/transactions).


### Available Operations

* [list_wallet_transactions](#list_wallet_transactions) - List wallet transactions
* [get_wallet_transaction](#get_wallet_transaction) - Get wallet transaction

## list_wallet_transactions

List all the transactions associated with a particular Moov wallet. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.wallet_transactions.list_wallet_transactions(request={
    "account_id": "2d736837-1618-4c4a-9e51-aa9dd394b389",
    "wallet_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    "transaction_type": "card-payment",
    "source_type": "dispute",
    "source_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
    "status": "pending",
    "count": 10,
    "skip": 10,
    "created_start_date_time": "2009-11-10T23:00:00Z",
    "created_end_date_time": "2009-11-13T01:00:00Z",
    "completed_start_date_time": "2009-11-10T23:00:00Z",
    "completed_end_date_time": "2009-11-13T01:00:00Z",
    "sweep_id": "683660e3-218c-4f5a-b193-930bd6d2f98e",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.ListWalletTransactionsRequest](../../models/listwallettransactionsrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ListWalletTransactionsResponse](../../models/listwallettransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_wallet_transaction

Get details on a specific wallet transaction. Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more. <br><br> To use this endpoint from a browser, you'll need to specify the `/accounts/{accountID}/wallets.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.wallet_transactions.get_wallet_transaction(account_id="a5040923-7566-4f60-af63-86465493f971", wallet_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", transaction_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of the wallet                                                    | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID associated with the wallet transaction.                          | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetWalletTransactionResponse](../../models/getwallettransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |