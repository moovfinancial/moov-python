# ImageUploadRequestMultiPart

Multipart request body for uploading an image with optional metadata.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `image`                                                                                      | [components.Image](../../models/components/image.md)                                         | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `metadata`                                                                                   | [Optional[components.ImageMetadataRequest]](../../models/components/imagemetadatarequest.md) | :heavy_minus_sign:                                                                           | Optional, json-encoded metadata to associate with the uploaded image.                        |