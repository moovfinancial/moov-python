# LimitedTimeRange

Return `count` number of results within time range between two timestamps and then the interval duration for each result in the specific `tz` timezone


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `every`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `tz`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `count`                                                              | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |