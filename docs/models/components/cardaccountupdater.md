# CardAccountUpdater

The results of the most recent card update request.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `updated_on`                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                 | :heavy_minus_sign:                                                                   | Timestamp from the card network indicating when the card update was processed.       |                                                                                      |
| `update_type`                                                                        | [Optional[components.CardUpdateReason]](../../models/components/cardupdatereason.md) | :heavy_minus_sign:                                                                   | The results of the card update request.                                              | number-update                                                                        |