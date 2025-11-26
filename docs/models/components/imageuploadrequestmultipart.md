# ImageUploadRequestMultiPart


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `image`                                                                                      | [components.Image](../../models/components/image.md)                                         | :heavy_check_mark:                                                                           | A PNG, JPEG, or WebP image file to upload.                                                   |
| `metadata`                                                                                   | [Optional[components.ImageMetadataRequest]](../../models/components/imagemetadatarequest.md) | :heavy_minus_sign:                                                                           | Optional, json-encoded metadata to associate with the uploaded image.                        |