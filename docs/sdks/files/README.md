# Files
(*files*)

## Overview

### Available Operations

* [upload](#upload) - Upload a file and link it to the specified Moov account. 

The maximum file size is 20MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, 
and png. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.write` scope.
* [list](#list) - List all the files associated with a particular Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.
* [get](#get) - Retrieve file details associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.

## upload

Upload a file and link it to the specified Moov account. 

The maximum file size is 20MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, 
and png. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadFile" method="post" path="/accounts/{accountID}/files" -->
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

    res = moov.files.upload(account_id="221c30bd-2551-4ae4-9a14-07bf6599b728", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, file_purpose=components.FilePurpose.REPRESENTATIVE_VERIFICATION, metadata="{\"requirement_id\": \"document.individual.verification\"}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 | Example                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | N/A                                                                                                                                                         |                                                                                                                                                             |
| `file`                                                                                                                                                      | [components.FileUploadRequestMultiPartFile](../../models/components/fileuploadrequestmultipartfile.md)                                                      | :heavy_check_mark:                                                                                                                                          | The file to be added. Valid types are `csv`, `png`, `jpeg`, `pdf`.                                                                                          |                                                                                                                                                             |
| `file_purpose`                                                                                                                                              | [components.FilePurpose](../../models/components/filepurpose.md)                                                                                            | :heavy_check_mark:                                                                                                                                          | The file's purpose.                                                                                                                                         | representative_verification                                                                                                                                 |
| `metadata`                                                                                                                                                  | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Additional metadata to be stored with the file, formatted as a JSON string.<br/><br/>Valid keys are `representative_id`, `comment`, `requirement_id`, `error_code`. | {"requirement_id": "document.individual.verification"}                                                                                                      |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |                                                                                                                                                             |

### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.GenericError        | 400, 409                   | application/json           |
| errors.FileValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

List all the files associated with a particular Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFiles" method="get" path="/accounts/{accountID}/files" -->
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

    res = moov.files.list(account_id="d1133bf2-4853-4436-9a03-23739895ab98")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve file details associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFileDetails" method="get" path="/accounts/{accountID}/files/{fileID}" -->
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

    res = moov.files.get(account_id="7f888113-d35a-4536-b9bc-c55076736ab6", file_id="af170db9-0d17-4a9f-ade6-5dd2f1b3412d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetFileDetailsResponse](../../models/operations/getfiledetailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |