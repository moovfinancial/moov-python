# InvoicePayment

Payment made towards an invoice, will be either a transfer or an external payment.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `payment_type`                                                                                   | [components.InvoicePaymentType](../../models/components/invoicepaymenttype.md)                   | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `transfer`                                                                                       | [Optional[components.InvoiceTransferPayment]](../../models/components/invoicetransferpayment.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `external`                                                                                       | [Optional[components.InvoiceExternalPayment]](../../models/components/invoiceexternalpayment.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |