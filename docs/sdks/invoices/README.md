# Invoices
(*invoices*)

## Overview

### Available Operations

* [create_invoice](#create_invoice) - Create an invoice for a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.
* [list_invoices](#list_invoices) - List all the invoices created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.read` scope.
* [get_invoice](#get_invoice) - Retrieve an invoice by ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.read` scope.
* [update_invoice](#update_invoice) - Updates an invoice.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.
* [mark_paid_invoice](#mark_paid_invoice) - Marks an invoice as paid outside of the Moov platform.
If a payment link was created, the corresponding payment link is canceled, but a receipt is still sent.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.

## create_invoice

Create an invoice for a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createInvoice" method="post" path="/accounts/{accountID}/invoices" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.invoices.create_invoice(account_id="241bf524-e777-4941-a5e4-d7f3f34d7a00", customer_account_id="<id>", description="austere gah under ew failing provided repeatedly pick onto", line_items={
        "items": [],
    }, tax_amount={
        "currency": "USD",
        "value_decimal": "12.987654321",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `account_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `customer_account_id`                                                          | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `description`                                                                  | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `line_items`                                                                   | [components.InvoiceLineItems](../../models/components/invoicelineitems.md)     | :heavy_check_mark:                                                             | A collection of line items for an invoice.                                     |
| `invoice_date`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `due_date`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `tax_amount`                                                                   | [Optional[components.AmountDecimal]](../../models/components/amountdecimal.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CreateInvoiceResponse](../../models/operations/createinvoiceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GenericError       | 400, 409                  | application/json          |
| errors.CreateInvoiceError | 422                       | application/json          |
| errors.APIError           | 4XX, 5XX                  | \*/\*                     |

## list_invoices

List all the invoices created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listInvoices" method="get" path="/accounts/{accountID}/invoices" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.invoices.list_invoices(account_id="114b02db-e4ca-47de-acc9-5624f4afccb5", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `account_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |                                                                                |
| `skip`                                                                         | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            | 60                                                                             |
| `count`                                                                        | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            | 20                                                                             |
| `status`                                                                       | [Optional[components.InvoiceStatus]](../../models/components/invoicestatus.md) | :heavy_minus_sign:                                                             | N/A                                                                            |                                                                                |
| `customer_account_id`                                                          | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |                                                                                |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |                                                                                |

### Response

**[operations.ListInvoicesResponse](../../models/operations/listinvoicesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ListInvoicesValidationError | 422                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_invoice

Retrieve an invoice by ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInvoice" method="get" path="/accounts/{accountID}/invoices/{invoiceID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.invoices.get_invoice(account_id="3ecce96f-a052-4c96-b389-98e880af1ab4", invoice_id="fc90d016-39ea-4110-b77a-2e1c95827f46")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `invoice_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetInvoiceResponse](../../models/operations/getinvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_invoice

Updates an invoice.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateInvoice" method="patch" path="/accounts/{accountID}/invoices/{invoiceID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.invoices.update_invoice(account_id="ce46d65a-8504-4afa-b3f7-303401bd08b3", invoice_id="ef510999-370a-4350-87d5-bc81fc02a2ea", line_items={
        "items": [
            {
                "name": "<value>",
                "base_price": {
                    "currency": "USD",
                    "value_decimal": "12.987654321",
                },
                "quantity": 984515,
                "options": [
                    {
                        "name": "<value>",
                        "quantity": 761923,
                        "price_modifier": {
                            "currency": "USD",
                            "value_decimal": "12.987654321",
                        },
                    },
                ],
            },
        ],
    }, tax_amount={
        "currency": "USD",
        "value_decimal": "12.987654321",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `invoice_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `description`                                                                                        | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `line_items`                                                                                         | [Optional[components.InvoiceLineItemsUpdate]](../../models/components/invoicelineitemsupdate.md)     | :heavy_minus_sign:                                                                                   | A collection of line items for an invoice.                                                           |
| `invoice_date`                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                 | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `due_date`                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                 | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `status`                                                                                             | [Optional[components.InvoiceStatus]](../../models/components/invoicestatus.md)                       | :heavy_minus_sign:                                                                                   | Status can only be updated to `canceled` when the status is either `draft`, `unpaid`,  or `overdue`. |
| `tax_amount`                                                                                         | [Optional[components.AmountDecimalUpdate]](../../models/components/amountdecimalupdate.md)           | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateInvoiceResponse](../../models/operations/updateinvoiceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GenericError       | 400, 409                  | application/json          |
| errors.UpdateInvoiceError | 422                       | application/json          |
| errors.APIError           | 4XX, 5XX                  | \*/\*                     |

## mark_paid_invoice

Marks an invoice as paid outside of the Moov platform.
If a payment link was created, the corresponding payment link is canceled, but a receipt is still sent.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/invoices.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="markPaidInvoice" method="put" path="/accounts/{accountID}/invoices/{invoiceID}/mark-paid" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="<value>",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.invoices.mark_paid_invoice(account_id="e270fffe-637f-4828-ace1-3813031d3274", invoice_id="9a08a44d-da9a-4385-8870-bb488c363e91")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `invoice_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `foreign_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `payment_date`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.MarkPaidInvoiceResponse](../../models/operations/markpaidinvoiceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GenericError         | 400, 409                    | application/json            |
| errors.MarkInvoicePaidError | 422                         | application/json            |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |