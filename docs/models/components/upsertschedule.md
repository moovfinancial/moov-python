# UpsertSchedule


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Simple description of what the schedule is.                          |
| `occurrences`                                                        | List[[components.Occurrence](../../models/components/occurrence.md)] | :heavy_minus_sign:                                                   | N/A                                                                  |
| `recur`                                                              | [Optional[components.Recur]](../../models/components/recur.md)       | :heavy_minus_sign:                                                   | Defines configuration for recurring transfers.                       |