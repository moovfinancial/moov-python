# EventTypeObject

The type of event that Moov can generate.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `event_type_id`                            | *str*                                      | :heavy_check_mark:                         | UUID v4                                    | ec7e1848-dc80-4ab0-8827-dd7fc0737b43       |
| `type`                                     | [models.EventType](../models/eventtype.md) | :heavy_check_mark:                         | The event type a webhook can subscribe to. |                                            |
| `description`                              | *str*                                      | :heavy_check_mark:                         | N/A                                        |                                            |