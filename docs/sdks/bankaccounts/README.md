# BankAccounts
(*bank_accounts*)

## Overview

To transfer money with Moov, you’ll need to link a bank account to your Moov account, then verify that account. You can link a bank account to a Moov account by providing the bank account number, routing number, and Moov account ID.

We require micro-deposit verification to reduce the risk of fraud or unauthorized activity. You can verify a bank account by initiating [micro-deposits](https://docs.moov.io/guides/sources/bank-accounts/#micro-deposit-verification), sending two small credit transfers to the bank account you want to confirm. Note that there is no way to initiate a micro-deposit from your bank of choice.

You can simulate bank account payment methods in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#bank-accounts) guide for more information.

Alternatively, you can link and verify a bank account in one step through an instant account verification token from a third party provider like [Plaid](https://docs.moov.io/guides/sources/bank-accounts/verification/plaid/) or [MX](https://docs.moov.io/guides/sources/bank-accounts/verification/mx/). Bank accounts can have the following statuses: `new`, `pending`, `verified`, `verificationFailed`, `errored`. Learn more by reading our guide on [bank accounts](https://docs.moov.io/guides/sources/bank-accounts/).


### Available Operations

* [bank_account](#bank_account) - Bank account
* [list_bank_accounts](#list_bank_accounts) - List bank accounts
* [get_bank](#get_bank) - Get bank account
* [delete_bank](#delete_bank) - Delete bank account
* [initiate_micro_deposits](#initiate_micro_deposits) - Initiate micro-deposits
* [complete_micro_deposits](#complete_micro_deposits) - Complete micro-deposits
* [get_bank_account_verification](#get_bank_account_verification) - Check instant verification status
* [initiate_bank_account_verification](#initiate_bank_account_verification) - Send instant verification credit
* [complete_bank_account_verification](#complete_bank_account_verification) - Complete instant verification

## bank_account

Link a bank account to an existing Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked
bank-account is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.bank_account(account_id="b44cc6de-75a9-4f9d-befb-5100c138cc9d", bank_account_payload={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                           | ID of the account.                                                                                                                                                                                                                                                                                                                                                           |
| `bank_account_payload`                                                                                                                                                                                                                                                                                                                                                       | [models.BankAccountPayload](../../models/bankaccountpayload.md)                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                                                          |
| `x_wait_for`                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.BankAccountsWaitFor]](../../models/bankaccountswaitfor.md)                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                           | Optional header to wait for certain events, such as the creation of a payment method, to occur before returning a response.<br/><br/>When this header is set to `payment-method`, the response will include any payment methods that were created for the newly<br/>linked card in the `paymentMethods` field. Otherwise, the `paymentMethods` field will be omitted from the response.<br/> |
| `retries`                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                          |

### Response

**[models.BankAccountResponse1](../../models/bankaccountresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_bank_accounts

List all the bank accounts associated with a particular Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.list_bank_accounts(account_id="91095bec-ade2-4a8c-9f46-ae7f07234fee")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListBankAccountsResponse](../../models/listbankaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_bank

Retrieve bank account details (i.e. routing number or account type) associated with a specific Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.get_bank(account_id="922445ad-a82d-43ae-b951-cd8129a3d18d", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `bank_account_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the bank account                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetBankResponse](../../models/getbankresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_bank

Discontinue using a specified bank account linked to a Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.delete_bank(account_id="ecebec6b-ef3f-4904-9215-24e77cf47d2b", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `bank_account_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the bank account                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteBankResponse](../../models/deletebankresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## initiate_micro_deposits

Micro-deposits help confirm bank account ownership, helping reduce fraud and the risk of unauthorized activity. Use this method to initiate the micro-deposit verification, sending two small credit transfers to the bank account you want to confirm.

If you request micro-deposits before 4:15PM ET, they will appear that same day. If you request micro-deposits any time after 4:15PM ET, they will appear the next banking day. When the two credits are initiated, Moov simultaneously initiates a debit to recoup the micro-deposits.

`sandbox` - Micro-deposits initiated for a `sandbox` bank account will always be `$0.00` / `$0.00` and instantly verifiable once initiated.

You can simulate micro-deposit verification in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#micro-deposits) guide for more information.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.initiate_micro_deposits(account_id="ff04d5ff-8ad2-4d87-baf2-0c9dcb6d3e2a", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `bank_account_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the bank account                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.InitiateMicroDepositsResponse](../../models/initiatemicrodepositsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## complete_micro_deposits

Complete the micro-deposit validation process by passing the amounts of the two transfers within three tries. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.complete_micro_deposits(account_id="ebfc273d-980b-4a92-8dd9-bf9996f2a16e", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", complete_micro_deposits_request={
    "amounts": [
        18,
        21,
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `account_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the account.                                                                  |                                                                                     |
| `bank_account_id`                                                                   | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the bank account                                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                |
| `complete_micro_deposits_request`                                                   | [models.CompleteMicroDepositsRequest](../../models/completemicrodepositsrequest.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.CompleteMicroDepositsResponse1](../../models/completemicrodepositsresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_bank_account_verification

Retrieve the current status and details of an instant verification, including whether the verification method was instant or same-day ACH. This helps track the verification process in real-time and provides details in case of exceptions.

The status will indicate the following:

- `new`: Verification initiated, credit pending to the payment network
- `sent-credit`: Credit sent, available for verification
- `failed`: Verification failed, description provided, user needs to add a new bank account
- `expired`: Verification expired after 14 days, initiate another verification
- `max-attempts-exceeded`: Five incorrect code attempts exhausted, initiate another verification

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.get_bank_account_verification(account_id="0102058c-a936-482a-a3ca-2355850903d7", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `bank_account_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | ID of the bank account                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetBankAccountVerificationResponse](../../models/getbankaccountverificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## initiate_bank_account_verification

Instant micro-deposit verification offers a quick and efficient way to verify bank account ownership. Send a $0.01 credit with a unique verification code via RTP or same-day ACH, depending on the receiving bank’s capabilities. This feature provides a faster alternative to traditional methods, allowing verification in a single session.

It is recommended to use the `X-Wait-For: rail-response` header to synchronously receive the outcome of the instant credit in the response payload.

Possible verification methods:
  - `instant`: Real-time verification credit sent via RTP
  - `ach`: Verification credit sent via same-day ACH

Possible statuses:
  - `new`: Verification initiated, credit pending
  - `sent-credit`: Credit sent, available for verification in the external bank account
  - `failed`: Verification failed due to credit rejection/return, details in `exceptionDetails`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.initiate_bank_account_verification(account_id="c2b4967e-86a5-474e-a78e-f013315f7dcc", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | ID of the account.                                                                                                                                                                                                                          |                                                                                                                                                                                                                                             |
| `bank_account_id`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | ID of the bank account                                                                                                                                                                                                                      | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                        |
| `x_wait_for`                                                                                                                                                                                                                                | [Optional[models.BankAccountsWaitFor]](../../models/bankaccountswaitfor.md)                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                          | Optional header to wait for certain events, such as the rail response, to occur before returning a response.<br/><br/>When this header is set to `rail-response`, the endpoint will wait for a sent-credit or failed status from the payment rail.<br/> |                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                         |                                                                                                                                                                                                                                             |

### Response

**[models.InitiateBankAccountVerificationResponse](../../models/initiatebankaccountverificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## complete_bank_account_verification

Finalize the instant micro-deposit verification by submitting the verification code displayed in the user’s bank account. Upon successful verification, the bank account status will be updated to `verified` and eligible for ACH debit transactions.

The following formats are accepted:
- `MV0000`
- `mv0000`
- `0000`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.bank_accounts.complete_bank_account_verification(account_id="88cf5aa5-bf76-406e-a986-eb33cd8890e3", bank_account_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", complete_bank_account_verification={
    "code": "MV1234",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `account_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the account.                                                                        |                                                                                           |
| `bank_account_id`                                                                         | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the bank account                                                                    | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                      |
| `complete_bank_account_verification`                                                      | [models.CompleteBankAccountVerification](../../models/completebankaccountverification.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.CompleteBankAccountVerificationResponse1](../../models/completebankaccountverificationresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |