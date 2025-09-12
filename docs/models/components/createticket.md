# CreateTicket

Request to create a new support ticket.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `title`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `body`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `author`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `contact`                                                            | [components.TicketContact](../../models/components/ticketcontact.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `foreign_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |