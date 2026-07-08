# CreateDepositAccountRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `account_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `x_source_system`                                                         | [components.SourceSystem](../../models/components/sourcesystem.md)        | :heavy_check_mark:                                                        | Identifies the core banking source system that produced the request body. |
| `request_body`                                                            | *Union[bytes, IO[bytes], io.IOBase]*                                      | :heavy_check_mark:                                                        | N/A                                                                       |