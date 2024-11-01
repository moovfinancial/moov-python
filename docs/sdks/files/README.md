# Files
(*files*)

## Overview

Files can be used for a multitude of different use cases including but not limited to, individual identity verification and business underwriting. You may need to provide documentation to enable capabilities or to keep capabilities enabled for an account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. To learn about uploading files in the Moov Dashboard, read our [file upload guide](https://docs.moov.io/guides/dashboard/accounts/#file-upload).


### Available Operations

* [upload_file](#upload_file) - Upload file
* [list_files](#list_files) - List files
* [get_file_details](#get_file_details) - Get file details

## upload_file

Upload a file and link it to the provided Moov account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.files.upload_file(account_id="97f59d46-b68f-4958-b251-ae3f3faf2789", file_upload_request={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
    "file_purpose": moov.FilePurpose.INDIVIDUAL_VERIFICATION,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `file_upload_request`                                               | [models.FileUploadRequest](../../models/fileuploadrequest.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadFileResponse](../../models/uploadfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_files

List all the files associated with a particular Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.files.list_files(account_id="a3c35406-9eb6-4801-bbac-0649c31c058a")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFilesResponse](../../models/listfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_details

Retrieve file details associated with a specific Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.files.get_file_details(account_id="346add0a-4dae-4729-8e74-1a50d00d677a", file_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Identifier for the file.                                            | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetFileDetailsResponse](../../models/getfiledetailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |