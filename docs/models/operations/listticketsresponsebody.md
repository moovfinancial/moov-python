# ListTicketsResponseBody

A paginated list of items. The `nextPage` field is omitted if there are no more pages available.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `items`                                                                              | List[[components.Ticket](../../models/components/ticket.md)]                         | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `next_page`                                                                          | [Optional[components.ItemListNextPage]](../../models/components/itemlistnextpage.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |