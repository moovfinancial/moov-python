# Transfers
(*transfers*)

## Overview

### Available Operations

* [create_transfer](#create_transfer) - Move money by providing the source, destination, and amount in the request body.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.
* [list_transfers](#list_transfers) - List all the transfers associated with a particular Moov account. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, 
if you set `skip`= 10, you will see a results set of 200 transfers after the first 2000). If you are searching a high volume of transfers, the request will likely 
process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited 
period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.
* [get_transfer](#get_transfer) - Retrieve full transfer details for an individual transfer of a particular Moov account. 

Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.
* [patch_transfer](#patch_transfer) - Update the metadata contained on a transfer. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.
* [refund_transfer](#refund_transfer) - Initiate a refund for a card transfer.

**Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.**    
See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.
* [list_refunds](#list_refunds) - Get a list of refunds for a card transfer.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.
* [get_refund](#get_refund) - Get details of a refund for a card transfer.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.
* [reverse_transfer](#reverse_transfer) - Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. 
Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/transfers.write` scope.
* [create_transfer_options](#create_transfer_options) - Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you 
supply in the request. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{yourAccountID}/transfers.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your accountID. You can find your 
accountID on the [Business details](https://dashboard.moov.io/settings/business) page.

## create_transfer

Move money by providing the source, destination, and amount in the request body.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.create_transfer(security=operations.CreateTransferSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), x_idempotency_key="b1f9d459-c664-42bb-90f6-422a074eb6b5", account_id="c60bdee4-f270-4df8-a5e1-0460745a118e", source={
        "payment_method_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
    }, destination={
        "payment_method_id": "3f9969cf-a1f3-4d83-8ddc-229a506651cf",
    }, amount={
        "currency": "USD",
        "value": 1204,
    }, facilitator_fee={
        "total_decimal": "12.987654321",
        "markup_decimal": "0.987654321",
    }, description="Pay Instructor for May 15 Class", metadata={
        "optional": "metadata",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                              | [operations.CreateTransferSecurity](../../models/operations/createtransfersecurity.md)                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |
| `x_idempotency_key`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Prevents duplicate transfers from being created.                                                                                                                                                                                                        |                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | The merchant's Moov account ID.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                         |
| `source`                                                                                                                                                                                                                                                | [components.CreateTransferSource](../../models/components/createtransfersource.md)                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                      | Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`.                                                                                                                                    |                                                                                                                                                                                                                                                         |
| `destination`                                                                                                                                                                                                                                           | [components.CreateTransferDestination](../../models/components/createtransferdestination.md)                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                      | The final stage of a transfer and the ultimate recipient of the funds.                                                                                                                                                                                  |                                                                                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                                                | [components.Amount](../../models/components/amount.md)                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |
| `x_moov_version`                                                                                                                                                                                                                                        | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                      | Specify an API version.                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                         |
| `x_wait_for`                                                                                                                                                                                                                                            | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                      | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                         |
| `facilitator_fee`                                                                                                                                                                                                                                       | [Optional[components.FacilitatorFee]](../../models/components/facilitatorfee.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Total or markup fee.                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                         |
| `description`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | An optional description of the transfer for your own internal use.                                                                                                                                                                                      | Pay Instructor for May 15 Class                                                                                                                                                                                                                         |
| `metadata`                                                                                                                                                                                                                                              | Dict[str, *str*]                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                                                                                           | {<br/>"optional": "metadata"<br/>}                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |

### Response

**[operations.CreateTransferResponse](../../models/operations/createtransferresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400                            | application/json               |
| errors.Transfer                | 409                            | application/json               |
| errors.TransferValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## list_transfers

List all the transfers associated with a particular Moov account. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, 
if you set `skip`= 10, you will see a results set of 200 transfers after the first 2000). If you are searching a high volume of transfers, the request will likely 
process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited 
period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.list_transfers(security=operations.ListTransfersSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="a7b433e5-531c-406b-bf40-4cde3c83fab5", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           | Example                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                            | [operations.ListTransfersSecurity](../../models/operations/listtransferssecurity.md)                                                  | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |                                                                                                                                       |
| `account_id`                                                                                                                          | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |                                                                                                                                       |
| `x_moov_version`                                                                                                                      | [Optional[components.Versions]](../../models/components/versions.md)                                                                  | :heavy_minus_sign:                                                                                                                    | Specify an API version.                                                                                                               |                                                                                                                                       |
| `account_i_ds`                                                                                                                        | List[*str*]                                                                                                                           | :heavy_minus_sign:                                                                                                                    | Optional, comma-separated account IDs by which the response is filtered based on whether the account ID is the source or destination. |                                                                                                                                       |
| `status`                                                                                                                              | [Optional[components.TransferStatus]](../../models/components/transferstatus.md)                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter for filtering transfers by status.                                                                                 |                                                                                                                                       |
| `start_date_time`                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                  | :heavy_minus_sign:                                                                                                                    | Optional date-time which inclusively filters all transfers created after this date-time.                                              |                                                                                                                                       |
| `end_date_time`                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                  | :heavy_minus_sign:                                                                                                                    | Optional date-time which exclusively filters all transfers created before this date-time.                                             |                                                                                                                                       |
| `group_id`                                                                                                                            | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Optional ID to filter for transfers in the same group.                                                                                |                                                                                                                                       |
| `refunded`                                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter to only return refunded transfers.                                                                                 |                                                                                                                                       |
| `disputed`                                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter to only return disputed transfers.                                                                                 |                                                                                                                                       |
| `skip`                                                                                                                                | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   | 60                                                                                                                                    |
| `count`                                                                                                                               | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   | 20                                                                                                                                    |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |                                                                                                                                       |

### Response

**[List[components.Transfer]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_transfer

Retrieve full transfer details for an individual transfer of a particular Moov account. 

Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.get_transfer(security=operations.GetTransferSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), transfer_id="64607ba5-82d4-4278-93b5-c5c5ca5c9cd8", account_id="cb1b48c3-1c11-4648-aa00-691b74c9ea1b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.GetTransferSecurity](../../models/operations/gettransfersecurity.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `transfer_id`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | Identifier for the transfer.                                                     |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `x_moov_version`                                                                 | [Optional[components.Versions]](../../models/components/versions.md)             | :heavy_minus_sign:                                                               | Specify an API version.                                                          |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[components.Transfer](../../models/components/transfer.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## patch_transfer

Update the metadata contained on a transfer. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.patch_transfer(security=operations.PatchTransferSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), transfer_id="9cc2093a-b55d-4f3f-b8e9-e13ac2df16ab", account_id="f0dfbcc6-c1a2-42ff-b3f9-a41de383cabc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.PatchTransferSecurity](../../models/operations/patchtransfersecurity.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `transfer_id`                                                                        | *str*                                                                                | :heavy_check_mark:                                                                   | Identifier for the transfer.                                                         |
| `account_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `x_moov_version`                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                 | :heavy_minus_sign:                                                                   | Specify an API version.                                                              |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[components.Transfer](../../models/components/transfer.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## refund_transfer

Initiate a refund for a card transfer.

**Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.**    
See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.write` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.refund_transfer(security=operations.RefundTransferSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), x_idempotency_key="3ba7635c-ceda-4c22-b383-46b4447b555b", account_id="fcf8bc06-0dab-429a-b25f-0547cda2b142", transfer_id="9032ecd3-7cf8-4760-a23e-09456a22dfb6", amount=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                              | [operations.RefundTransferSecurity](../../models/operations/refundtransfersecurity.md)                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |
| `x_idempotency_key`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Prevents duplicate refunds from being created.                                                                                                                                                                                                          |                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | The merchant's Moov account ID.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                         |
| `transfer_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Identifier for the transfer.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                         |
| `x_moov_version`                                                                                                                                                                                                                                        | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                      | Specify an API version.                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                         |
| `x_wait_for`                                                                                                                                                                                                                                            | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                      | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Amount to refund in cents. If null, the original transfer's full amount will be refunded.                                                                                                                                                               | 1000                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |

### Response

**[operations.RefundTransferResponse](../../models/operations/refundtransferresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400                          | application/json             |
| errors.CardAcquiringRefund   | 409                          | application/json             |
| errors.RefundValidationError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_refunds

Get a list of refunds for a card transfer.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.list_refunds(security=operations.ListRefundsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="7d74a845-fe17-4ebe-a05e-71847ef8c510", transfer_id="d081988f-448f-492c-8c60-836126fa0dfb")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.ListRefundsSecurity](../../models/operations/listrefundssecurity.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `transfer_id`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | Identifier for the transfer.                                                     |
| `x_moov_version`                                                                 | [Optional[components.Versions]](../../models/components/versions.md)             | :heavy_minus_sign:                                                               | Specify an API version.                                                          |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[List[components.CardAcquiringRefund]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_refund

Get details of a refund for a card transfer.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the `/accounts/{accountID}/transfers.read` 
scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.get_refund(security=operations.GetRefundSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), transfer_id="dbc09cb2-ef99-4553-8501-94323f377dbf", account_id="7f90bf73-6fb7-41e7-90aa-a9133e7d92c2", refund_id="0f86fa43-1a9b-4a5d-8227-f253063f7fb1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [operations.GetRefundSecurity](../../models/operations/getrefundsecurity.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `transfer_id`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | Identifier for the transfer.                                                 |
| `account_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `refund_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | Identifier for the refund.                                                   |
| `x_moov_version`                                                             | [Optional[components.Versions]](../../models/components/versions.md)         | :heavy_minus_sign:                                                           | Specify an API version.                                                      |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[components.CardAcquiringRefund](../../models/components/cardacquiringrefund.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reverse_transfer

Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. 
Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/transfers.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.reverse_transfer(security=operations.ReverseTransferSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), x_idempotency_key="16ad771b-54f6-4f38-86a5-09d5f907e897", account_id="47d7634a-2772-4a99-a0bc-2bb960cea7e2", transfer_id="c39f87ae-8349-4b5b-9f87-1669f5d784aa", amount=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                 | [operations.ReverseTransferSecurity](../../models/operations/reversetransfersecurity.md)                   | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `x_idempotency_key`                                                                                        | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Prevents duplicate reversals from being created.                                                           |                                                                                                            |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The Moov account ID.                                                                                       |                                                                                                            |
| `transfer_id`                                                                                              | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The transfer ID to reverse.                                                                                |                                                                                                            |
| `amount`                                                                                                   | *int*                                                                                                      | :heavy_check_mark:                                                                                         | Amount to reverse in cents. Partial amounts will automatically trigger a refund instead of a cancellation. | 1000                                                                                                       |
| `x_moov_version`                                                                                           | [Optional[components.Versions]](../../models/components/versions.md)                                       | :heavy_minus_sign:                                                                                         | Specify an API version.                                                                                    |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[components.Reversal](../../models/components/reversal.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ReversalValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## create_transfer_options

Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you 
supply in the request. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{yourAccountID}/transfers.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/). The accountID included must be your accountID. You can find your 
accountID on the [Business details](https://dashboard.moov.io/settings/business) page.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.transfers.create_transfer_options(security=operations.CreateTransferOptionsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.CreateTransferOptionsSecurity](../../models/operations/createtransferoptionssecurity.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `x_moov_version`                                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                                 | :heavy_minus_sign:                                                                                   | Specify an API version.                                                                              |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[components.TransferOptions](../../models/components/transferoptions.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GenericError                   | 400                                   | application/json                      |
| errors.TransferOptionsValidationError | 422                                   | application/json                      |
| errors.APIError                       | 4XX, 5XX                              | \*/\*                                 |