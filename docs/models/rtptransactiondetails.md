# RTPTransactionDetails

RTP specific details about the transaction.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `status`                                                             | [models.RTPTransactionStatus](../models/rtptransactionstatus.md)     | :heavy_check_mark:                                                   | Status of a transaction within the RTP lifecycle.                    |
| `network_response_code`                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Response code returned by network on failure.                        |
| `failure_code`                                                       | [Optional[models.RTPFailureCode]](../models/rtpfailurecode.md)       | :heavy_minus_sign:                                                   | Status codes for RTP failures.                                       |
| `initiated_on`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `completed_on`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `failed_on`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `accepted_without_posting_on`                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |