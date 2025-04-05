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

    res = moov.disputes.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6", skip=60, count=20)

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

    res = moov.disputes.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", dispute_id="e50f7622-81da-484b-9c66-1c8a99c6b71b")

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

    res = moov.disputes.accept(account_id="a155a634-52c8-4ade-b619-6958b5f88a84", dispute_id="e67dcdcf-56b8-44e6-b2b0-a9297f858656")

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

    res = moov.disputes.list_evidence(account_id="613e59d0-0cb8-462c-be9c-7f2b955ec234", dispute_id="1bb71474-4bf0-40b8-899f-01914b8ad7e5")

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

    res = moov.disputes.upload_evidence_file(account_id="190d267b-ea77-4231-9939-ba89cb7df82b", dispute_id="94aabddc-d855-40e6-ab0a-1e547e0dcc9d", file={
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

    res = moov.disputes.upload_evidence_text(account_id="a4f06189-7f74-4b7e-b76a-f3c7af17b8d9", dispute_id="fb79f20c-b948-445c-a145-3e20ce4f769c", text="<value>", evidence_type=components.EvidenceType.CUSTOMER_COMMUNICATION)

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

    res = moov.disputes.submit_evidence(account_id="7cf55b42-45bd-49ff-883c-0017334607a6", dispute_id="f6e86188-8533-46e8-a184-ec17f223c86b")

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

    res = moov.disputes.get_evidence(account_id="3a49ec36-8a92-4fae-81e6-868bfc90b4c9", dispute_id="7128e90f-9089-47d5-92b9-87bbfe6bd9b3", evidence_id="614a5588-4d0f-4d00-b8d9-2ae60f6124bf")

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

    res = moov.disputes.update_evidence(account_id="f19d220a-55c9-476d-9cfa-d9a536b8065f", dispute_id="da248348-9f0d-4df8-a9c6-66cc2492e87a", evidence_id="a204faa9-3cce-4628-b833-5b0694ac47bb")

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

    res = moov.disputes.delete_evidence(account_id="21999434-0e9c-4cd1-890a-4af813ad91ae", dispute_id="41954292-f363-4ea3-9b4b-bc417e55f6be", evidence_id="ac7b6eef-7513-4ff4-996b-a85b1f62d499")

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

    res = moov.disputes.get_evidence_data(account_id="4ebc37c5-a566-452b-8b54-ef280fcb888b", dispute_id="4bd05222-78bc-49a7-92a8-f1e5ee0edd6b", evidence_id="01098426-242d-4693-8716-ec08cd8da86e")

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