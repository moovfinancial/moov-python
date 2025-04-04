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

    res = moov.transfers.create(x_idempotency_key="b1f9d459-c664-42bb-90f6-422a074eb6b5", account_id="c60bdee4-f270-4df8-a5e1-0460745a118e", source={
        "payment_method_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym dues",
            "originating_company_name": "Whole Body Fit",
            "debit_hold_period": components.DebitHoldPeriod.TWO_MINUS_DAYS,
        },
    }, destination={
        "payment_method_id": "3f9969cf-a1f3-4d83-8ddc-229a506651cf",
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym dues",
            "originating_company_name": "Whole Body Fit",
        },
    }, amount={
        "currency": "USD",
        "value": 1204,
    }, facilitator_fee={
        "total_decimal": "12.987654321",
        "markup_decimal": "0.987654321",
    }, description="Pay Instructor for May 15 Class", metadata={
        "optional": "metadata",
    }, sales_tax_amount={
        "currency": "USD",
        "value": 1204,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_idempotency_key`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Prevents duplicate transfers from being created.                                                                                                                                                                                                        |                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | The merchant's Moov account ID.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                         |
| `source`                                                                                                                                                                                                                                                | [components.CreateTransferSource](../../models/components/createtransfersource.md)                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                      | Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`.                                                                                                                                    |                                                                                                                                                                                                                                                         |
| `destination`                                                                                                                                                                                                                                           | [components.CreateTransferDestination](../../models/components/createtransferdestination.md)                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                      | The final stage of a transfer and the ultimate recipient of the funds.                                                                                                                                                                                  |                                                                                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                                                | [components.Amount](../../models/components/amount.md)                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |
| `x_wait_for`                                                                                                                                                                                                                                            | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                      | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                         |
| `facilitator_fee`                                                                                                                                                                                                                                       | [Optional[components.FacilitatorFee]](../../models/components/facilitatorfee.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Total or markup fee.                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                         |
| `description`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | An optional description of the transfer that is used on receipts and for your own internal use.                                                                                                                                                         | Pay Instructor for May 15 Class                                                                                                                                                                                                                         |
| `metadata`                                                                                                                                                                                                                                              | Dict[str, *str*]                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                                                                                           | {<br/>"optional": "metadata"<br/>}                                                                                                                                                                                                                      |
| `sales_tax_amount`                                                                                                                                                                                                                                      | [Optional[components.Amount]](../../models/components/amount.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Optional sales tax amount. `transfer.amount.value` should be inclusive of any sales tax and represents the total amount charged.                                                                                                                        |                                                                                                                                                                                                                                                         |
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

    res = moov.transfers.list(account_id="a7b433e5-531c-406b-bf40-4cde3c83fab5", skip=60, count=20)

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

    res = moov.transfers.get(transfer_id="64607ba5-82d4-4278-93b5-c5c5ca5c9cd8", account_id="cb1b48c3-1c11-4648-aa00-691b74c9ea1b")

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

    res = moov.transfers.update(transfer_id="d95fa7f0-e743-42ce-b47c-b60cc78135dd", account_id="b85898c1-25a1-4907-a1c5-562af6646dad", metadata={
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

    res = moov.transfers.create_cancellation(account_id="12dbe811-b86d-497b-ae0f-fb7cfda35251", transfer_id="6bb9450c-10a9-4c8d-a8d2-d3fa18648706")

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

    res = moov.transfers.get_cancellation(account_id="fe098575-0376-4404-9a9c-6fe55e3766af", transfer_id="b3b49c6a-9b74-4a85-9d49-864ada05cbf2", cancellation_id="5848c1db-18ac-41eb-b107-b6499987902c")

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

    res = moov.transfers.initiate_refund(x_idempotency_key="bdfa6a76-31f8-4cdf-a007-3d8aac713b91", account_id="9b1350b2-a5be-41e3-92be-61f5cf4372a8", transfer_id="7390ad29-1a0d-4a0c-8c17-da1708ee9ac2", amount=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_idempotency_key`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Prevents duplicate refunds from being created.                                                                                                                                                                                                          |                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | The merchant's Moov account ID.                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                         |
| `transfer_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                      | Identifier for the transfer.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                         |
| `x_wait_for`                                                                                                                                                                                                                                            | [Optional[components.TransferWaitFor]](../../models/components/transferwaitfor.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                      | Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an <br/>asynchronous response indicating the transfer was created (this is the default response if the header is omitted). |                                                                                                                                                                                                                                                         |
| `amount`                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Amount to refund in cents. If null, the original transfer's full amount will be refunded.                                                                                                                                                               | 1000                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |

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

    res = moov.transfers.list_refunds(account_id="7d74a845-fe17-4ebe-a05e-71847ef8c510", transfer_id="d081988f-448f-492c-8c60-836126fa0dfb")

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

    res = moov.transfers.get_refund(transfer_id="dbc09cb2-ef99-4553-8501-94323f377dbf", account_id="7f90bf73-6fb7-41e7-90aa-a9133e7d92c2", refund_id="0f86fa43-1a9b-4a5d-8227-f253063f7fb1")

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

    res = moov.transfers.create_reversal(x_idempotency_key="9d4b2ed0-777b-40e6-ba88-d6ca730c3503", account_id="16452b89-d33c-4be9-8f92-205130a46467", transfer_id="c7f1b114-0545-47ba-9d79-fdba229c3df7", amount=1000)

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