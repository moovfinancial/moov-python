# FileUploadMetadata

Additional metadata to be stored with the file.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `representative_id`                                                                                    | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | The representative ID that the file is for. Required when filePurpose is `representativeVerification`. |
| `comment`                                                                                              | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Comments or notes about the file.                                                                      |