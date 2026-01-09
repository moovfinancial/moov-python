# UpdateWebhook

Request body for updating an existing webhook.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `url`                                                                            | *str*                                                                            | :heavy_check_mark:                                                               | The URL where webhook events will be sent.                                       |
| `status`                                                                         | [components.WebhookStatus](../../models/components/webhookstatus.md)             | :heavy_check_mark:                                                               | The status of the webhook.                                                       |
| `event_types`                                                                    | List[[components.WebhookEventType](../../models/components/webhookeventtype.md)] | :heavy_check_mark:                                                               | The list of event types this webhook should subscribe to.                        |
| `description`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | A description of the webhook for reference. Can be an empty string.              |