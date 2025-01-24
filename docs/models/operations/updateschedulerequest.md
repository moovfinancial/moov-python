# UpdateScheduleRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `account_id`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `schedule_id`                                                          | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `upsert_schedule`                                                      | [components.UpsertSchedule](../../models/components/upsertschedule.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `x_moov_version`                                                       | [Optional[components.Versions]](../../models/components/versions.md)   | :heavy_minus_sign:                                                     | Specify an API version.                                                |