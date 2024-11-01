# Document

Describes an uploaded file.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `document_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | A unique identifier for this document.                               | e210a9d6                                                             |
| `type`                                                               | [models.Type](../models/type.md)                                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `content_type`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | application/pdf                                                      |
| `uploaded_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `parse_errors`                                                       | List[*str*]                                                          | :heavy_minus_sign:                                                   | Optional array of errors encountered dring automated parsing.        |                                                                      |