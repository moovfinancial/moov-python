# Disputes
(*disputes*)

## Overview

### Available Operations

* [list](#list) - Returns the list of disputes. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](#get) - Get a dispute by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [accept](#accept) - Accepts liability for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_evidence](#list_evidence) - Returns a dispute's public evidence by its ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [upload_evidence_file](#upload_evidence_file) - Uploads a file as evidence for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [upload_evidence_text](#upload_evidence_text) - Uploads text as evidence for a dispute.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [submit_evidence](#submit_evidence) - Submit the evidence associated with a dispute.

Evidence items must be uploaded using the appropriate endpoint(s) prior to calling this endpoint to submit it. **Evidence can only
be submitted once per dispute.**

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_evidence](#get_evidence) - Get dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update_evidence](#update_evidence) - Updates dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [delete_evidence](#delete_evidence) - Deletes dispute evidence by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_evidence_data](#get_evidence_data) - Downloads dispute evidence data by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

## list

Returns the list of disputes. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.list(account_id="2cb8fed5-9089-45a7-88aa-5468adeaaddb", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `skip`                                                                                                | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   | 60                                                                                                    |
| `count`                                                                                               | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   | 20                                                                                                    |
| `start_date_time`                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Optional date-time parameter to filter all disputes created on and after the provided date and time.  |                                                                                                       |
| `end_date_time`                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Optional date-time parameter to filter all disputes created on and before the provided date and time. |                                                                                                       |
| `respond_start_date_time`                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Optional date-time which exclusively filters all disputes with respond by before this date-time.      |                                                                                                       |
| `respond_end_date_time`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Optional date-time which exclusively filters all disputes with respond by before this date-time.      |                                                                                                       |
| `status`                                                                                              | [Optional[components.DisputeStatus]](../../models/components/disputestatus.md)                        | :heavy_minus_sign:                                                                                    | Optional dispute status by which to filter the disputes.                                              |                                                                                                       |
| `merchant_account_id`                                                                                 | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Optional parameter to filter by merchant account ID.                                                  |                                                                                                       |
| `cardholder_account_id`                                                                               | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Optional parameter to filter by cardholder account ID.                                                |                                                                                                       |
| `dispute_i_ds`                                                                                        | List[*str*]                                                                                           | :heavy_minus_sign:                                                                                    | Optional parameter to filter by a comma separated list of dispute IDs.                                |                                                                                                       |
| `transfer_i_ds`                                                                                       | List[*str*]                                                                                           | :heavy_minus_sign:                                                                                    | Optional parameter to filter by a comma separated list of transfer IDs.                               |                                                                                                       |
| `order_by`                                                                                            | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[operations.ListDisputesResponse](../../models/operations/listdisputesresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get

Get a dispute by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.get(account_id="102df293-b524-4bb7-9b68-5610432a0b8d", dispute_id="2efe55e9-61a0-4b3d-aab6-423bb7f8140b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetDisputeResponse](../../models/operations/getdisputeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## accept

Accepts liability for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.accept(account_id="bfefe6f4-2658-4d3d-9be8-73ff29049dbe", dispute_id="692e1a18-8314-4a5d-bcfd-0d5ada162cf8")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.AcceptDisputeResponse](../../models/operations/acceptdisputeresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## list_evidence

Returns a dispute's public evidence by its ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.list_evidence(account_id="dcaaa24e-96d2-4b5b-997d-aa20f46c812a", dispute_id="e0434916-3828-49bb-bfa4-30f3c039d5f0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListDisputeEvidenceResponse](../../models/operations/listdisputeevidenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## upload_evidence_file

Uploads a file as evidence for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.upload_evidence_file(account_id="ac81921c-4c1a-4e7a-8a8f-dfc0d0027ac5", dispute_id="49c04fa3-f5c3-4ddd-aece-4b5fb6e8a071", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, evidence_type=components.EvidenceType.CUSTOMER_COMMUNICATION)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                 |
| `dispute_id`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                 |
| `file`                                                                                                                                                                                                                              | [components.File](../../models/components/file.md)                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                  | The file to upload as evidence. Valid types are [jpeg, tiff, pdf] with a limit of 4MB per file.<br/><br/>The `Content-Type` header for this form part must be one of the following:<br/>  - `image/jpeg`<br/>  - `image/tiff`<br/>  - `application/pdf` |
| `evidence_type`                                                                                                                                                                                                                     | [components.EvidenceType](../../models/components/evidencetype.md)                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                 |

### Response

**[operations.UploadDisputeEvidenceFileResponse](../../models/operations/uploaddisputeevidencefileresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GenericError              | 400, 409                         | application/json                 |
| errors.FileUploadValidationError | 422                              | application/json                 |
| errors.APIError                  | 4XX, 5XX                         | \*/\*                            |

## upload_evidence_text

Uploads text as evidence for a dispute.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.upload_evidence_text(account_id="d542736f-c9c3-491c-86c3-7303a97965ea", dispute_id="9487cd25-501d-4a76-8c24-54328af8a4b6", text="<value>", evidence_type=components.EvidenceType.COVER_LETTER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `text`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The text to associate with the dispute as evidence.                 |
| `evidence_type`                                                     | [components.EvidenceType](../../models/components/evidencetype.md)  | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.UploadDisputeEvidenceTextResponse](../../models/operations/uploaddisputeevidencetextresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## submit_evidence

Submit the evidence associated with a dispute.

Evidence items must be uploaded using the appropriate endpoint(s) prior to calling this endpoint to submit it. **Evidence can only
be submitted once per dispute.**

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.submit_evidence(account_id="aff4d2bf-fd2c-471e-a697-b2cc2c9f297e", dispute_id="491e05b8-7adc-440b-af36-4d2229edd4f0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.SubmitDisputeEvidenceResponse](../../models/operations/submitdisputeevidenceresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_evidence

Get dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.get_evidence(account_id="8abb6e62-d012-4f06-8c83-d993dd3155f2", dispute_id="ebf0479f-774e-4881-9e0b-2c791e0601fc", evidence_id="37534a23-990f-4bdd-b2c7-1653336983f0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetDisputeEvidenceResponse](../../models/operations/getdisputeevidenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_evidence

Updates dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.update_evidence(account_id="51c8da31-2c44-4bdf-a86e-26169242ffe0", dispute_id="584a4c46-9412-4622-8ac9-001d7ececcd4", evidence_id="743d351d-f194-45e4-8628-700f3b327c51")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `account_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `dispute_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `evidence_id`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `evidence_type`                                                              | [Optional[components.EvidenceType]](../../models/components/evidencetype.md) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `text`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | If updating text evidence, the new text to associate with the dispute.       |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.UpdateDisputeEvidenceResponse](../../models/operations/updatedisputeevidenceresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## delete_evidence

Deletes dispute evidence by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.delete_evidence(account_id="927e189d-273f-40ab-814f-1fa3ab1aa7dd", dispute_id="94451c2e-a568-4800-a669-7f6190da461d", evidence_id="1bfaf385-47fb-4da3-8072-d54e354a9910")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteDisputeEvidenceFileResponse](../../models/operations/deletedisputeevidencefileresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 409                 | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_evidence_data

Downloads dispute evidence data by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

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

    res = moov.disputes.get_evidence_data(account_id="38299899-8c4f-4a43-b73a-3cef9ba87c62", dispute_id="22c477d1-525c-4c1b-b8a3-7dcec5c4da28", evidence_id="fb1c15fd-675b-4f82-861e-f3092ed39462")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetDisputeEvidenceDataResponse](../../models/operations/getdisputeevidencedataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |