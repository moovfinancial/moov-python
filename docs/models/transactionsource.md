# TransactionSource

Specifies the nature and initiator of a transaction. Crucial for recurring and merchant-initiated transactions as per card scheme rules. Omit for customer-initiated e-commerce transactions.

- `first-recurring`: Initial transaction in a recurring series or saving a card for future merchant-initiated charges
- `recurring`: Regular, merchant-initiated scheduled transactions
- `unscheduled`: Non-regular, merchant-initiated transactions like account top-ups



## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `FIRST_RECURRING` | first-recurring   |
| `RECURRING`       | recurring         |
| `UNSCHEDULED`     | unscheduled       |