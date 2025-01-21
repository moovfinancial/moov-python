# Files
(*files*)

## Overview

### Available Operations

* [upload_file](#upload_file) - Upload a file and link it to the specified Moov account. 

The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, 
and png. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.write` scope.
* [list_files](#list_files) - List all the files associated with a particular Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.read` scope.
* [get_file_details](#get_file_details) - Retrieve file details associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.read` scope.

## upload_file

Upload a file and link it to the specified Moov account. 

The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, 
and png. 

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.write` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.files.upload_file(security=moov.UploadFileSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="997f59d4-6b68-4f95-a825-1ae3f3faf278", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, file_purpose=moov.FilePurpose.REPRESENTATIVE_VERIFICATION, metadata="{\"requirement_id\": \"document.individual.verification\"}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 | Example                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                  | [models.UploadFileSecurity](../../models/uploadfilesecurity.md)                                                                                             | :heavy_check_mark:                                                                                                                                          | N/A                                                                                                                                                         |                                                                                                                                                             |
| `account_id`                                                                                                                                                | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | N/A                                                                                                                                                         |                                                                                                                                                             |
| `file`                                                                                                                                                      | [models.FileUploadRequestMultiPartFile](../../models/fileuploadrequestmultipartfile.md)                                                                     | :heavy_check_mark:                                                                                                                                          | The file to be added. Valid types are `csv`, `png`, `jpeg`, `pdf`.                                                                                          |                                                                                                                                                             |
| `file_purpose`                                                                                                                                              | [models.FilePurpose](../../models/filepurpose.md)                                                                                                           | :heavy_check_mark:                                                                                                                                          | The file's purpose.                                                                                                                                         | representative_verification                                                                                                                                 |
| `x_moov_version`                                                                                                                                            | [Optional[models.Versions]](../../models/versions.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                          | Specify an API version.                                                                                                                                     |                                                                                                                                                             |
| `metadata`                                                                                                                                                  | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Additional metadata to be stored with the file, formatted as a JSON string.<br/><br/>Valid keys are `representative_id`, `comment`, `requirement_id`, `error_code`. | {"requirement_id": "document.individual.verification"}                                                                                                      |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |                                                                                                                                                             |

### Response

**[models.FileDetails](../../models/filedetails.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.GenericError        | 400, 409                   | application/json           |
| models.FileValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_files

List all the files associated with a particular Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.files.list_files(security=moov.ListFilesSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="a3c35406-9eb6-4801-bbac-0649c31c058a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ListFilesSecurity](../../models/listfilessecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_moov_version`                                                    | [Optional[models.Versions]](../../models/versions.md)               | :heavy_minus_sign:                                                  | Specify an API version.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.FileDetails]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_file_details

Retrieve file details associated with a specific Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need to specify the 
`/accounts/{accountID}/files.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.files.get_file_details(security=moov.GetFileDetailsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="346add0a-4dae-4729-8e74-1a50d00d677a", file_id="bf657841-ba2d-4060-ad21-eb2b7372cf85")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetFileDetailsSecurity](../../models/getfiledetailssecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `account_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `file_id`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `x_moov_version`                                                        | [Optional[models.Versions]](../../models/versions.md)                   | :heavy_minus_sign:                                                      | Specify an API version.                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.FileDetails](../../models/filedetails.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |