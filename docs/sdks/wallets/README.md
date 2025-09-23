# Wallets
(*wallets*)

## Overview

### Available Operations

* [create](#create) - Create a new wallet for an account. You can specify optional attributes such as a display name and description to specify the intended use of the wallet. This will generate a new moov-wallet payment method.

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.
* [list](#list) - List the wallets associated with a Moov account. 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](#get) - Get information on a specific wallet (e.g., the available balance). 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [update](#update) - Update properties of an existing wallet such as name, description, status, or metadata.

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.

## create

Create a new wallet for an account. You can specify optional attributes such as a display name and description to specify the intended use of the wallet. This will generate a new moov-wallet payment method.

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createWallet" method="post" path="/accounts/{accountID}/wallets" -->
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

    res = moov.wallets.create(account_id="b4b3f37c-b73e-4271-b8ec-108a8593c9b9", name="My wallet", description="A general wallet used for my payments", metadata={
        "optional": "metadata",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `account_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | The Moov account ID the wallet belongs to.                                                    |                                                                                               |
| `name`                                                                                        | *str*                                                                                         | :heavy_check_mark:                                                                            | Name of the wallet.                                                                           |                                                                                               |
| `description`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Description of the wallet.                                                                    |                                                                                               |
| `metadata`                                                                                    | Dict[str, *str*]                                                                              | :heavy_minus_sign:                                                                            | Free-form key-value pair list. Useful for storing information that is not captured elsewhere. | {<br/>"optional": "metadata"<br/>}                                                            |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[operations.CreateWalletResponse](../../models/operations/createwalletresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GenericError                | 400, 409                           | application/json                   |
| errors.CreateWalletValidationError | 422                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## list

List the wallets associated with a Moov account. 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listWallets" method="get" path="/accounts/{accountID}/wallets" -->
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

    res = moov.wallets.list(account_id="25221c3c-8e3f-40db-8570-66d17b51014d", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `account_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `status`                                                                     | [Optional[components.WalletStatus]](../../models/components/walletstatus.md) | :heavy_minus_sign:                                                           | Optional parameter for filtering wallets by status.                          |                                                                              |
| `wallet_type`                                                                | [Optional[components.WalletType]](../../models/components/wallettype.md)     | :heavy_minus_sign:                                                           | Optional parameter for filtering wallets by type.                            |                                                                              |
| `skip`                                                                       | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          | 60                                                                           |
| `count`                                                                      | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          | 20                                                                           |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.ListWalletsResponse](../../models/operations/listwalletsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ListWalletsValidationError | 422                               | application/json                  |
| errors.APIError                   | 4XX, 5XX                          | \*/\*                             |

## get

Get information on a specific wallet (e.g., the available balance). 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWallet" method="get" path="/accounts/{accountID}/wallets/{walletID}" -->
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

    res = moov.wallets.get(account_id="d04dfd44-8194-422f-a666-08d30c183f9a", wallet_id="10a6bc37-8eeb-41c8-bf5f-77b40955542a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `wallet_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWalletResponse](../../models/operations/getwalletresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update properties of an existing wallet such as name, description, status, or metadata.

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWallet" method="patch" path="/accounts/{accountID}/wallets/{walletID}" -->
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

    res = moov.wallets.update(wallet_id="9f1c6e07-aae8-40e6-b290-502bb1bc486e", account_id="e4aad2fb-201d-4390-b4d3-6de7716152e1", name="My second wallet", description="My new description", metadata={
        "optional": "metadata",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                 | Type                                                                                                                                                                                                      | Required                                                                                                                                                                                                  | Description                                                                                                                                                                                               | Example                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wallet_id`                                                                                                                                                                                               | *str*                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                        | Identifier for the wallet.                                                                                                                                                                                |                                                                                                                                                                                                           |
| `account_id`                                                                                                                                                                                              | *str*                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                        | The Moov account ID the wallet belongs to.                                                                                                                                                                |                                                                                                                                                                                                           |
| `name`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |                                                                                                                                                                                                           |
| `status`                                                                                                                                                                                                  | [Optional[components.WalletStatus]](../../models/components/walletstatus.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                        | Status of a wallet.<br/>  - `active`: The wallet is available for use and has an enabled payment method.<br/>  - `closed`: The wallet is no longer active and the corresponding payment method has been disabled. |                                                                                                                                                                                                           |
| `description`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |                                                                                                                                                                                                           |
| `metadata`                                                                                                                                                                                                | Dict[str, *str*]                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                                             | {<br/>"optional": "metadata"<br/>}                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                       |                                                                                                                                                                                                           |

### Response

**[operations.UpdateWalletResponse](../../models/operations/updatewalletresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GenericError               | 400, 409                          | application/json                  |
| errors.PatchWalletValidationError | 422                               | application/json                  |
| errors.APIError                   | 4XX, 5XX                          | \*/\*                             |