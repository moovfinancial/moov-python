# AllowedSchedule

Limits card usage to specific days and times. Set to `null` to remove all schedule restrictions.


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `timezone`                                                                                    | *str*                                                                                         | :heavy_check_mark:                                                                            | IANA timezone string used to evaluate window boundaries against the authorization time.       |
| `windows`                                                                                     | List[[components.ScheduleWindow](../../models/components/schedulewindow.md)]                  | :heavy_check_mark:                                                                            | Time windows during which the card may authorize. Any matching window allows the transaction. |