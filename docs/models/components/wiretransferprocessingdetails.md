# WireTransferProcessingDetails

Wire-specific processing details returned on a transfer.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `status`                                                                             | [components.WireTransactionStatus](../../models/components/wiretransactionstatus.md) | :heavy_check_mark:                                                                   | Status of a transaction within the wire lifecycle.                                   |
| `network_response_code`                                                              | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Response code returned by the network on failure.                                    |
| `failure_code`                                                                       | [Optional[components.WireFailureCode]](../../models/components/wirefailurecode.md)   | :heavy_minus_sign:                                                                   | Status codes for wire failures.                                                      |