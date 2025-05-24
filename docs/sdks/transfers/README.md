# Transfers
(*transfers*)

## Overview

### Available Operations

* [create](#create) - Move money by providing the source, destination, and amount in the request body.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](#list) - List all the transfers associated with a particular Moov account. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, 
if you set `skip`= 10, you will see a results set of 200 transfers after the first 10). If you are searching a high volume of transfers, the request will likely 
process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited 
period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](#get) - Retrieve full transfer details for an individual transfer of a particular Moov account. 

Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) 
to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](#update) - Update the metadata contained on a transfer. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [create_cancellation](#create_cancellation) -   Initiate a cancellation for a card, ACH, or queued transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_cancellation](#get_cancellation) -   Get details of a cancellation for a transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.read` scope.
* [initiate_refund](#initiate_refund) - Initiate a refund for a card transfer.

**Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.**    
See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list_refunds](#list_refunds) - Get a list of refunds for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get_refund](#get_refund) - Get details of a refund for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [create_reversal](#create_reversal) - Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. 
Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/transfers.write` scope.
* [generate_options](#generate_options) - Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you 
supply in the request. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

## create

Move money by providing the source, destination, and amount in the request body.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.transfers.create(x_idempotency_key="d6903402-776f-48d6-8fba-0358959d34e5", account_id="ea9f2225-403b-4e2c-93b0-0eda090ffa65", source={
        "payment_method_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
    }, destination={
        "payment_method_id": "3f9969cf-a1f3-4d83-8ddc-229a506651cf",
    }, amount={
        "currency": "USD",
        "value": 32945,
    }, facilitator_fee={
        "total_decimal": "12.987654321",
        "markup_decimal": "0.987654321",
    }, description="Transfer from card to wallet", metadata={
        "optional": "metadata",
    }, sales_tax_amount={
        "currency": "USD",
        "value": 1204,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_idempotency_key`                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Prevents duplicate transfers from being created.                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                |
| `account_id`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Your Moov account ID.                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                |
| `source`                                                                                                                                                                                                                                                                                       | [components.CreateTransferSource](../../models/components/createtransfersource.md)                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`.                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                |
| `destination`                                                                                                                                                                                                                                                                                  | [components.CreateTransferDestination](../../models/components/createtransferdestination.md)                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                             | The final stage of a transfer and the ultimate recipient of the funds.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                |
| `amount`                                                                                                                                                                                                                                                                                       | [components.Amount](../../models/components/amount.md)                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `x_wait_for`                                                                                                                                                                                                                                                                                   | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). A timeout will occur after 15 seconds. |                                                                                                                                                                                                                                                                                                |
| `facilitator_fee`                                                                                                                                                                                                                                                                              | [Optional[components.FacilitatorFee]](../../models/components/facilitatorfee.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Total or markup fee.                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                |
| `description`                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | An optional description of the transfer that is used on receipts and for your own internal use.                                                                                                                                                                                                | Pay Instructor for May 15 Class                                                                                                                                                                                                                                                                |
| `metadata`                                                                                                                                                                                                                                                                                     | Dict[str, *str*]                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                                                                                                                                  | {<br/>"optional": "metadata"<br/>}                                                                                                                                                                                                                                                             |
| `sales_tax_amount`                                                                                                                                                                                                                                                                             | [Optional[components.Amount]](../../models/components/amount.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional sales tax amount. `transfer.amount.value` should be inclusive of any sales tax and represents the total amount charged.                                                                                                                                                               |                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |

### Response

**[operations.CreateTransferResponse](../../models/operations/createtransferresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400                            | application/json               |
| errors.Transfer                | 409                            | application/json               |
| errors.TransferValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## list

List all the transfers associated with a particular Moov account. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, 
if you set `skip`= 10, you will see a results set of 200 transfers after the first 10). If you are searching a high volume of transfers, the request will likely 
process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited 
period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.list(account_id="0579c895-4d2b-4024-8092-f71b80ab5d00", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           | Example                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                          | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |                                                                                                                                       |
| `account_i_ds`                                                                                                                        | List[*str*]                                                                                                                           | :heavy_minus_sign:                                                                                                                    | Optional, comma-separated account IDs by which the response is filtered based on whether the account ID is the source or destination. |                                                                                                                                       |
| `status`                                                                                                                              | [Optional[components.TransferStatus]](../../models/components/transferstatus.md)                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter for filtering transfers by status.                                                                                 |                                                                                                                                       |
| `start_date_time`                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                  | :heavy_minus_sign:                                                                                                                    | Optional date-time which inclusively filters all transfers created after this date-time.                                              |                                                                                                                                       |
| `end_date_time`                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                  | :heavy_minus_sign:                                                                                                                    | Optional date-time which exclusively filters all transfers created before this date-time.                                             |                                                                                                                                       |
| `group_id`                                                                                                                            | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Optional ID to filter for transfers in the same group.                                                                                |                                                                                                                                       |
| `schedule_id`                                                                                                                         | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Optional ID to filter for transfer occurrences belonging to the same schedule.                                                        |                                                                                                                                       |
| `refunded`                                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter to only return refunded transfers.                                                                                 |                                                                                                                                       |
| `disputed`                                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | Optional parameter to only return disputed transfers.                                                                                 |                                                                                                                                       |
| `skip`                                                                                                                                | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   | 60                                                                                                                                    |
| `count`                                                                                                                               | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   | 20                                                                                                                                    |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |                                                                                                                                       |

### Response

**[operations.ListTransfersResponse](../../models/operations/listtransfersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve full transfer details for an individual transfer of a particular Moov account. 

Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) 
to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.get(transfer_id="960cf5a2-50a3-4914-ad86-d54c022bf5df", account_id="31113f7b-9f68-44e9-9338-6d8e655c7c96")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTransferResponse](../../models/operations/gettransferresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update the metadata contained on a transfer. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.transfers.update(transfer_id="de30c075-4245-4d62-bfb3-f76d4d7d3b9c", account_id="18a7907d-2f89-493a-b15a-3aad91c24496", metadata={
        "optional": "metadata",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |                                                                     |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `metadata`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 | {<br/>"optional": "metadata"<br/>}                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.UpdateTransferResponse](../../models/operations/updatetransferresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_cancellation

  Initiate a cancellation for a card, ACH, or queued transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.transfers.create_cancellation(account_id="10ae862c-6658-4f87-967d-46e995737204", transfer_id="36c80a6c-ceb2-4e5d-a437-8a39afdfdc58")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The partner's Moov account ID.                                      |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The transfer ID to cancel.                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateCancellationResponse](../../models/operations/createcancellationresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_cancellation

  Get details of a cancellation for a transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.get_cancellation(account_id="55cb62c2-22e4-4a36-bd53-3b9adc77ee81", transfer_id="bc13b680-bac3-432e-bf44-e9aa6426cbb2", cancellation_id="770cb4b5-d5b0-4e8b-995b-86b790296ba5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Moov account ID of the partner or transfer's source or destination. |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `cancellation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the cancellation.                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetCancellationResponse](../../models/operations/getcancellationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## initiate_refund

Initiate a refund for a card transfer.

**Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.**    
See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.transfers.initiate_refund(x_idempotency_key="8d9af6b8-67e1-4efa-8188-68039f34097d", account_id="cb6ae9f9-afab-4f06-9eb0-8abf54a3ada2", transfer_id="04022119-95be-4ef4-9dd4-b3782f6aa7b9", amount=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_idempotency_key`                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Prevents duplicate refunds from being created.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                |
| `account_id`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | The merchant's Moov account ID.                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                |
| `transfer_id`                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Identifier for the transfer.                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                |
| `x_wait_for`                                                                                                                                                                                                                                                                                   | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). A timeout will occur after 15 seconds. |                                                                                                                                                                                                                                                                                                |
| `amount`                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Amount to refund in cents. If null, the original transfer's full amount will be refunded.                                                                                                                                                                                                      | 1000                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |

### Response

**[operations.InitiateRefundResponse](../../models/operations/initiaterefundresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400                          | application/json             |
| errors.CardAcquiringRefund   | 409                          | application/json             |
| errors.RefundValidationError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_refunds

Get a list of refunds for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.list_refunds(account_id="03f5baaa-f5d8-44bd-90db-868745fe66e8", transfer_id="6b1aa1a1-bff1-43b9-9126-2806fdc9c732")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListRefundsResponse](../../models/operations/listrefundsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_refund

Get details of a refund for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.get_refund(transfer_id="e90d3386-c5b2-4e2b-b841-efc590eba6c0", account_id="bbb69538-edaa-4a0b-b107-f46f2da89864", refund_id="8e12687e-a4e8-46c9-9e11-a57bbd781e44")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the transfer.                                        |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `refund_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the refund.                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRefundResponse](../../models/operations/getrefundresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_reversal

Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. 
Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.transfers.create_reversal(x_idempotency_key="b91d00b2-4ecb-4eb4-a67f-d6f76c0b7ad8", account_id="f225b49d-911b-440b-baed-6065968b69cb", transfer_id="a17b29e2-4af6-4c9d-ad3a-dd0ded2966ad", amount=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `x_idempotency_key`                                                                                        | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Prevents duplicate reversals from being created.                                                           |                                                                                                            |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The Moov account ID.                                                                                       |                                                                                                            |
| `transfer_id`                                                                                              | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The transfer ID to reverse.                                                                                |                                                                                                            |
| `amount`                                                                                                   | *int*                                                                                                      | :heavy_check_mark:                                                                                         | Amount to reverse in cents. Partial amounts will automatically trigger a refund instead of a cancellation. | 1000                                                                                                       |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[operations.CreateReversalResponse](../../models/operations/createreversalresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ReversalValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## generate_options

Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you 
supply in the request. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.transfers.generate_options(source={}, destination={}, amount={
        "currency": "USD",
        "value": 1204,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `source`                                                                                   | [components.SourceDestinationOptions](../../models/components/sourcedestinationoptions.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `destination`                                                                              | [components.SourceDestinationOptions](../../models/components/sourcedestinationoptions.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `amount`                                                                                   | [components.Amount](../../models/components/amount.md)                                     | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateTransferOptionsResponse](../../models/operations/createtransferoptionsresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GenericError                   | 400                                   | application/json                      |
| errors.TransferOptionsValidationError | 422                                   | application/json                      |
| errors.APIError                       | 4XX, 5XX                              | \*/\*                                 |