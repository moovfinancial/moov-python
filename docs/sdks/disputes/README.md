# Disputes
(*disputes*)

## Overview

A [dispute](https://docs.moov.io/guides/money-movement/cards/disputes/) is a situation where a cardholder formally questions a transaction on their account with their card issuer. This could be for a number of reasons ranging from billing errors to fraudulent activity or dissatisfactory goods/services. If the dispute is recognized as legitimate, the issuer will reverse the payment (otherwise known as a chargeback).

You can simulate disputes, including winning or losing a dispute, in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#disputes) guide for more information.


### Available Operations

* [list_disputes](#list_disputes) - List of all disputes
* [get_dispute](#get_dispute) - Dispute by ID
* [accept_dispute](#accept_dispute) - Accept dispute
* [list_dispute_evidence](#list_dispute_evidence) - List dispute evidence by dispute ID
* [submit_evidence](#submit_evidence) - Submit dispute evidence
* [upload_evidence_file](#upload_evidence_file) - Upload evidence file
* [upload_evidence_text](#upload_evidence_text) - Upload evidence text
* [get_dispute_evidence](#get_dispute_evidence) - Dispute evidence by ID
* [delete_evidence](#delete_evidence) - Delete dispute evidence by dispute ID and evidence ID
* [update_dispute_evidence](#update_dispute_evidence) - Update dispute evidence by dispute ID and evidence ID
* [get_dispute_evidence_data](#get_dispute_evidence_data) - Download dispute evidence data by evidence ID

## list_disputes

Returns the list of disputes. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.list_disputes(request={
    "count": 10,
    "skip": 10,
    "respond_start_date_time": "2009-11-10T23:00:00Z",
    "respond_end_date_time": "2009-11-13T01:00:00Z",
    "status": moov.DisputeStatus.RESPONSE_NEEDED,
    "merchant_account_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
    "cardholder_account_id": "9506dbf6-4208-44c3-ad8a-e4431660e1f2",
    "dispute_i_ds": "24858e38-dd7d-4164-a1ae-206d8214148c,c436e049-3bb3-477d-b304-5601e0c08222,9f161723-b328-4eb7-967e-096106900b7e",
    "transfer_i_ds": "44f4b83c-db0e-43d2-b039-cbe1ec6aa72c",
    "start_date_time": "2009-11-10T23:00:00Z",
    "end_date_time": "2009-11-13T01:00:00Z",
    "order_by": "created-at:desc",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListDisputesRequest](../../models/listdisputesrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDisputesResponse](../../models/listdisputesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_dispute

Returns a user's dispute by ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.get_dispute(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDisputeResponse](../../models/getdisputeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## accept_dispute

Accepts a dispute. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.accept_dispute(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AcceptDisputeResponse](../../models/acceptdisputeresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## list_dispute_evidence

Returns a dispute's public evidence by its ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.list_dispute_evidence(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListDisputeEvidenceResponse](../../models/listdisputeevidenceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## submit_evidence

Submits evidence for a dispute. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.submit_evidence(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SubmitEvidenceResponse](../../models/submitevidenceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## upload_evidence_file

Uploads a file as evidence for a dispute. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.upload_evidence_file(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_file={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
    "evidence_type": moov.EvidenceType.CUSTOMER_COMMUNICATION,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_file`                                                     | [models.EvidenceFile](../../models/evidencefile.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UploadEvidenceFileResponse](../../models/uploadevidencefileresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## upload_evidence_text

Uploads text as evidence for a dispute. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.upload_evidence_text(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_text={
    "text": "<value>",
    "evidence_type": moov.EvidenceType.CUSTOMER_COMMUNICATION,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_text`                                                     | [models.EvidenceText](../../models/evidencetext.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UploadEvidenceTextResponse](../../models/uploadevidencetextresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## get_dispute_evidence

Returns a piece of dispute evidence by evidence ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.get_dispute_evidence(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of evidence                                                      | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDisputeEvidenceResponse](../../models/getdisputeevidenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_evidence

Deletes dispute evidence by ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.delete_evidence(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of evidence                                                      | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteEvidenceResponse](../../models/deleteevidenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_dispute_evidence

Updates dispute evidence by ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.update_dispute_evidence(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of evidence                                                      | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_update`                                                   | [models.EvidenceUpdate](../../models/evidenceupdate.md)             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateDisputeEvidenceResponse](../../models/updatedisputeevidenceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 500              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## get_dispute_evidence_data

Downloads dispute evidence data by ID. Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.get_dispute_evidence_data(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dispute_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of dispute                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `evidence_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of evidence                                                      | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDisputeEvidenceDataResponse](../../models/getdisputeevidencedataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |