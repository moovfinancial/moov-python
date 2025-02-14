# EvidenceUploadResponse

Details of a successfully uploaded evidence file.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `evidence_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The ID of the evidence.                                              |
| `dispute_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The ID of the dispute the evidence is associated with.               |
| `filename`                                                           | *str*                                                                | :heavy_check_mark:                                                   | The name of the evidence file.                                       |
| `mime_type`                                                          | *str*                                                                | :heavy_check_mark:                                                   | The MIME type of the evidence file.                                  |
| `size`                                                               | *int*                                                                | :heavy_check_mark:                                                   | The size of the evidence file.                                       |
| `evidence_type`                                                      | [components.EvidenceType](../../models/components/evidencetype.md)   | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_on`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date and time the evidence was uploaded.                         |