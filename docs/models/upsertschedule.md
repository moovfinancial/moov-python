# UpsertSchedule

Describes the schedule to create or modify


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `description`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | Simple description of what the schedule is.                    |
| `recur`                                                        | [OptionalNullable[models.RecurInput]](../models/recurinput.md) | :heavy_minus_sign:                                             | Defines configuration for recurring transfers                  |
| `occurrences`                                                  | List[[models.UpsertOccurrence](../models/upsertoccurrence.md)] | :heavy_minus_sign:                                             | Occurrences to either create or modify<br/>                    |