# Transfers
(*transfers*)

## Overview

A [transfer](https://docs.moov.io/guides/money-movement/) is the movement of money between Moov accounts, from source to destination. You can initiate a transfer to another Moov account as long as there is a linked and verified payment method.

With Moov, you can also implement transfer groups, allowing you to associate multiple transfers together and run them sequentially. To learn more, read our guide on [transfer groups](https://docs.moov.io/guides/money-movement/transfer-groups/#transfer-statuses).

You can simulate various RTP, push to card, ACH, and declined transfer scenarios in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#transfers) guide for more information.


### Available Operations

* [create_transfer](#create_transfer) - Create a transfer
* [get_transfer](#get_transfer) - Get a transfer
* [patch_transfer](#patch_transfer) - Patch transfer metadata
* [create_transfer_options](#create_transfer_options) - Generate transfer options
* [refund_transfer](#refund_transfer) - Refund a transfer
* [get_refunds](#get_refunds) - Get a list of refunds for a card transfer
* [get_refund](#get_refund) - Get refund details
* [reverse_transfer](#reverse_transfer) - Cancel or refund a card transfer
* [list_transfers_for_account](#list_transfers_for_account) - List transfers for account
* [get_transfer_for_account](#get_transfer_for_account) - Retrieve a transfer for an account

## create_transfer

Move money by providing the source, destination, and amount in the request body. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> If you are running a **server-side** integration, you will use your API keys per our [authentication guidelines](https://docs.moov.io/api/authentication/api-authentication/#server-side-basic-authentication).

If you are running a **client-side** integration, you'll need to specify the `/accounts/{yourAccountID}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your accountID. You can find your accountID on the [Business details](https://dashboard.moov.io/settings/business) page.


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.create_transfer(x_idempotency_key="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", create_transfer={
    "source": {
        "transfer_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
        "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym Dues",
            "originating_company_name": "Whole Body Fit",
            "debit_hold_period": moov.CreateAchDetailsSourceDebitHoldPeriod.TWO_DAYS,
            "sec_code": moov.CreateAchDetailsSourceSecCode.WEB,
        },
    },
    "destination": {
        "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym Dues",
            "originating_company_name": "Whole Body Fit",
        },
    },
    "amount": {
        "currency": "USD",
        "value": 1204,
    },
    "facilitator_fee": {
        "total_decimal": "12.987654321",
        "markup_decimal": "12.987654321",
    },
    "description": "Pay Instructor for May 15 Class",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_idempotency_key`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | Prevents duplicate transfers from being created. Note that we only accept UUID v4.                                                                                                                                                                     | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                                   |
| `create_transfer`                                                                                                                                                                                                                                      | [models.CreateTransfer](../../models/createtransfer.md)                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |
| `x_wait_for`                                                                                                                                                                                                                                           | [Optional[models.WaitFor]](../../models/waitfor.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                     | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Response

**[models.CreateTransferResponse](../../models/createtransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.Error1        | 400                  | application/json     |
| models.TransferError | 409                  | application/json     |
| models.SDKError      | 4XX, 5XX             | \*/\*                |

## get_transfer

Retrieve full transfer details such as the amount, source, and destination. Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{yourAccountID}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your accountID. You can find your accountID on the [Business details](https://dashboard.moov.io/settings/business) page.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.get_transfer(transfer_id="64607ba5-82d4-4278-93b5-c5c5ca5c9cd8")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer_id`                                                                                                                                | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Identifier for the transfer.                                                                                                                 |
| `account_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account. |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetTransferResponse](../../models/gettransferresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## patch_transfer

Update the metadata contained on a transfer. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{yourAccountID}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your facilitator accountID. You can find your accountID on the [Business details](https://dashboard.moov.io/settings/business) page.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.patch_transfer(transfer_id="9cc2093a-b55d-4f3f-b8e9-e13ac2df16ab", patch_transfer={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `patch_transfer`                                                    | [models.PatchTransfer](../../models/patchtransfer.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchTransferResponse](../../models/patchtransferresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_transfer_options

Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you supply in the request. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{yourAccountID}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your accountID. You can find your accountID on the [Business details](https://dashboard.moov.io/settings/business) page.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.create_transfer_options(request={
    "source": {
        "account_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
        "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    },
    "destination": {
        "account_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
        "payment_method_id": "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    },
    "amount": {
        "currency": "USD",
        "value": 1204,
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateTransferOptions](../../models/createtransferoptions.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateTransferOptionsResponse](../../models/createtransferoptionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## refund_transfer

<strong>Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.</strong> See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. <br><br> Initiate a refund for a card transfer. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.refund_transfer(transfer_id="fcf8bc06-0dab-429a-b25f-0547cda2b142", x_idempotency_key="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", create_refund={
    "amount": 1000,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer_id`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                        | Identifier for the transfer.                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                           |
| `x_idempotency_key`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                        | Prevents duplicate refunds from being created. Note that we only accept UUID v4.                                                                                                                                                                          | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                                      |
| `x_wait_for`                                                                                                                                                                                                                                              | [Optional[models.WaitFor]](../../models/waitfor.md)                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                        | Optional header that indicates whether to return a synchronous response that includes the full refund and card transaction details or an asynchronous response indicating the refund was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                           |
| `create_refund`                                                                                                                                                                                                                                           | [Optional[models.CreateRefund]](../../models/createrefund.md)                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                       |                                                                                                                                                                                                                                                           |

### Response

**[models.RefundTransferResponse](../../models/refundtransferresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| models.Error1         | 400                   | application/json      |
| models.GetRefundError | 409                   | application/json      |
| models.SDKError       | 4XX, 5XX              | \*/\*                 |

## get_refunds

Get a list of refunds for a card transfer. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.get_refunds(transfer_id="8e97179d-1baa-473b-9508-d0d1875c1834")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer_id`                                                                                                                                | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Identifier for the transfer.                                                                                                                 |
| `account_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account. |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetRefundsResponse](../../models/getrefundsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_refund

Get details of a refund for a card transfer. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.get_refund(transfer_id="dbc09cb2-ef99-4553-8501-94323f377dbf", refund_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  | Example                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer_id`                                                                                                                                | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Identifier for the transfer.                                                                                                                 |                                                                                                                                              |
| `refund_id`                                                                                                                                  | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Identifier for the refund.                                                                                                                   | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                         |
| `account_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account. |                                                                                                                                              |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |                                                                                                                                              |

### Response

**[models.GetRefundResponse](../../models/getrefundresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## reverse_transfer

Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.reverse_transfer(transfer_id="47d7634a-2772-4a99-a0bc-2bb960cea7e2", x_idempotency_key="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", create_reversal={
    "amount": 1000,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |                                                                     |
| `x_idempotency_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | Prevents duplicate reversals from being created.                    | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `create_reversal`                                                   | [Optional[models.CreateReversal]](../../models/createreversal.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ReverseTransferResponse](../../models/reversetransferresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.Error1               | 400                         | application/json            |
| models.CreatedReversalError | 409                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## list_transfers_for_account

List all the transfers associated with a particular Moov account. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` scope. The accountID included must match the accountID being requested. <br><br> When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, if you set `skip`= 10, you will see a results set of 200 transfers after the first 2000). If you are searching a high volume of transfers, the request will likely process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.list_transfers_for_account(request={
    "account_id": "0b1121f9-1271-4064-9bb6-0b553a233e49",
    "status": moov.TransferStatus.PENDING,
    "start_date_time": "2009-11-10T23:00:00Z",
    "end_date_time": "2009-11-13T01:00:00Z",
    "group_id": "683660e3-218c-4f5a-b193-930bd6d2f98e",
    "count": 10,
    "skip": 10,
    "refunded": False,
    "disputed": False,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.ListTransfersForAccountRequest](../../models/listtransfersforaccountrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ListTransfersForAccountResponse](../../models/listtransfersforaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_transfer_for_account

Retrieve full transfer details for an individual transfer of a particular Moov account. Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. <br><br> To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` scope. The accountID included must match the accountID being requested.

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.transfers.get_transfer_for_account(transfer_id="ed9d4fd2-70b9-4340-a45a-2975448f5e40", account_id="907570fe-2d01-491a-bd99-07538a16ce98")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Identifier for an account.                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTransferForAccountResponse](../../models/gettransferforaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |