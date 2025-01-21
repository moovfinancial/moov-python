# BankAccounts
(*bank_accounts*)

## Overview

### Available Operations

* [link_bank_account](#link_bank_account) - Link a bank account to an existing Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked
bank-account is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.
* [list_bank_accounts](#list_bank_accounts) - List all the bank accounts associated with a particular Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. To use this endpoint 
from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_bank_account](#get_bank_account) - Retrieve bank account details (i.e. routing number or account type) associated with a specific Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. To use this 
endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when 
generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [disable_bank_account](#disable_bank_account) - Discontinue using a specified bank account linked to a Moov account. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope 
when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [initiate_micro_deposits](#initiate_micro_deposits) - Micro-deposits help confirm bank account ownership, helping reduce fraud and the risk of unauthorized activity. Use this method to initiate the micro-deposit verification, sending two small credit transfers to the bank account you want to confirm.

If you request micro-deposits before 4:15PM ET, they will appear that same day. If you request micro-deposits any time after 4:15PM ET, they will appear the next banking day. When the two credits are initiated, Moov simultaneously initiates a debit to recoup the micro-deposits. 

`sandbox` - Micro-deposits initiated for a `sandbox` bank account will always be `$0.00` / `$0.00` and instantly verifiable once initiated.

You can simulate micro-deposit verification in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#micro-deposits) guide for more information.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [complete_micro_deposits](#complete_micro_deposits) - Complete the micro-deposit validation process by passing the amounts of the two transfers within three tries.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_bank_account_verification](#get_bank_account_verification) - Retrieve the current status and details of an instant verification, including whether the verification method was instant or same-day 
ACH. This helps track the verification process in real-time and provides details in case of exceptions.

The status will indicate the following:

- `new`: Verification initiated, credit pending to the payment network
- `sent-credit`: Credit sent, available for verification
- `failed`: Verification failed, description provided, user needs to add a new bank account
- `expired`: Verification expired after 14 days, initiate another verification
- `max-attempts-exceeded`: Five incorrect code attempts exhausted, initiate another verification

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).
* [initiate_bank_account_verification](#initiate_bank_account_verification) - Instant micro-deposit verification offers a quick and efficient way to verify bank account ownership. 

Send a $0.01 credit with a unique verification code via RTP or same-day ACH, depending on the receiving bank’s capabilities. This
feature provides a faster alternative to traditional methods, allowing verification in a single session.

It is recommended to use the `X-Wait-For: rail-response` header to synchronously receive the outcome of the instant credit in the
 response payload.

Possible verification methods:
  - `instant`: Real-time verification credit sent via RTP
  - `ach`: Verification credit sent via same-day ACH

Possible statuses:
  - `new`: Verification initiated, credit pending
  - `sent-credit`: Credit sent, available for verification in the external bank account
  - `failed`: Verification failed due to credit rejection/return, details in `exceptionDetails`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).
* [complete_bank_account_verification](#complete_bank_account_verification) - Finalize the instant micro-deposit verification by submitting the verification code displayed in the user’s bank account. 

Upon successful verification, the bank account status will be updated to `verified` and eligible for ACH debit transactions.

The following formats are accepted:
- `MV0000`
- `mv0000`
- `0000`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when 
generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

## link_bank_account

Link a bank account to an existing Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked
bank-account is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.link_bank_account(security=moov.LinkBankAccountSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="5049418d-b6dc-4a6f-a285-091c0e15dc6a", link_bank_account={
        "plaid": {
            "token": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                                                                                                                  | [models.LinkBankAccountSecurity](../../models/linkbankaccountsecurity.md)                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         |
| `link_bank_account`                                                                                                                                                                                                                                                                                                                                                         | [models.LinkBankAccount](../../models/linkbankaccount.md)                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         |
| `x_moov_version`                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.Versions]](../../models/versions.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Specify an API version.                                                                                                                                                                                                                                                                                                                                                     |
| `x_wait_for`                                                                                                                                                                                                                                                                                                                                                                | [Optional[models.BankAccountWaitFor]](../../models/bankaccountwaitfor.md)                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Optional header to wait for certain events, such as the creation of a payment method, to occur before returning a response.<br/><br/>When this header is set to `payment-method`, the response will include any payment methods that were created for the newly<br/>linked card in the `paymentMethods` field. Otherwise, the `paymentMethods` field will be omitted from the response. |
| `retries`                                                                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                         |

### Response

**[models.BankAccount](../../models/bankaccount.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GenericError               | 400, 409                          | application/json                  |
| models.BankAccountValidationError | 422                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## list_bank_accounts

List all the bank accounts associated with a particular Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. To use this endpoint 
from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.list_bank_accounts(security=moov.ListBankAccountsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="91095bec-ade2-4a8c-9f46-ae7f07234fee")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.ListBankAccountsSecurity](../../models/listbankaccountssecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `account_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `x_moov_version`                                                            | [Optional[models.Versions]](../../models/versions.md)                       | :heavy_minus_sign:                                                          | Specify an API version.                                                     |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[List[models.BankAccount]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_bank_account

Retrieve bank account details (i.e. routing number or account type) associated with a specific Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. To use this 
endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when 
generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.get_bank_account(security=moov.GetBankAccountSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="30085225-d87e-47cd-8f08-001465f8cd22", bank_account_id="6c5a7be6-792b-4628-af28-a852f8c9de5b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.GetBankAccountSecurity](../../models/getbankaccountsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `account_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `bank_account_id`                                                       | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `x_moov_version`                                                        | [Optional[models.Versions]](../../models/versions.md)                   | :heavy_minus_sign:                                                      | Specify an API version.                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.BankAccount](../../models/bankaccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## disable_bank_account

Discontinue using a specified bank account linked to a Moov account. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope 
when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    moov.bank_accounts.disable_bank_account(security=moov.DisableBankAccountSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="d01209e7-2701-46cc-b0ba-56eabf4e1ec7", bank_account_id="0ae3f56a-e391-4a80-962d-9fe4c7a45b97")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.DisableBankAccountSecurity](../../models/disablebankaccountsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `account_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `bank_account_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `x_moov_version`                                                                | [Optional[models.Versions]](../../models/versions.md)                           | :heavy_minus_sign:                                                              | Specify an API version.                                                         |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## initiate_micro_deposits

Micro-deposits help confirm bank account ownership, helping reduce fraud and the risk of unauthorized activity. Use this method to initiate the micro-deposit verification, sending two small credit transfers to the bank account you want to confirm.

If you request micro-deposits before 4:15PM ET, they will appear that same day. If you request micro-deposits any time after 4:15PM ET, they will appear the next banking day. When the two credits are initiated, Moov simultaneously initiates a debit to recoup the micro-deposits. 

`sandbox` - Micro-deposits initiated for a `sandbox` bank account will always be `$0.00` / `$0.00` and instantly verifiable once initiated.

You can simulate micro-deposit verification in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#micro-deposits) guide for more information.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    moov.bank_accounts.initiate_micro_deposits(security=moov.InitiateMicroDepositsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="ff04d5ff-8ad2-4d87-baf2-0c9dcb6d3e2a", bank_account_id="10ed8688-d7e2-4a70-827d-af795759945d")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.InitiateMicroDepositsSecurity](../../models/initiatemicrodepositssecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `account_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `bank_account_id`                                                                     | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `x_moov_version`                                                                      | [Optional[models.Versions]](../../models/versions.md)                                 | :heavy_minus_sign:                                                                    | Specify an API version.                                                               |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## complete_micro_deposits

Complete the micro-deposit validation process by passing the amounts of the two transfers within three tries.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.complete_micro_deposits(security=moov.CompleteMicroDepositsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="ebfc273d-980b-4a92-8dd9-bf9996f2a16e", bank_account_id="3e6af61e-a5cb-4281-b0e6-e7e3d39edf65", amounts=[
        18,
        21,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [models.CompleteMicroDepositsSecurity](../../models/completemicrodepositssecurity.md)                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `bank_account_id`                                                                                    | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `amounts`                                                                                            | List[*int*]                                                                                          | :heavy_check_mark:                                                                                   | Two positive integers, in cents, equal to the values of the micro-deposits sent to the bank account. | [<br/>18,<br/>21<br/>]                                                                               |
| `x_moov_version`                                                                                     | [Optional[models.Versions]](../../models/versions.md)                                                | :heavy_minus_sign:                                                                                   | Specify an API version.                                                                              |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[models.CompletedMicroDeposits](../../models/completedmicrodeposits.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.GenericError                | 400, 409                           | application/json                   |
| models.MicroDepositValidationError | 422                                | application/json                   |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_bank_account_verification

Retrieve the current status and details of an instant verification, including whether the verification method was instant or same-day 
ACH. This helps track the verification process in real-time and provides details in case of exceptions.

The status will indicate the following:

- `new`: Verification initiated, credit pending to the payment network
- `sent-credit`: Credit sent, available for verification
- `failed`: Verification failed, description provided, user needs to add a new bank account
- `expired`: Verification expired after 14 days, initiate another verification
- `max-attempts-exceeded`: Five incorrect code attempts exhausted, initiate another verification

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.get_bank_account_verification(security=moov.GetBankAccountVerificationSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="0102058c-a936-482a-a3ca-2355850903d7", bank_account_id="ee6888ef-544e-4146-bab7-ea04e31b2274")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetBankAccountVerificationSecurity](../../models/getbankaccountverificationsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `account_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `bank_account_id`                                                                               | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `x_moov_version`                                                                                | [Optional[models.Versions]](../../models/versions.md)                                           | :heavy_minus_sign:                                                                              | Specify an API version.                                                                         |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.BankAccountVerification](../../models/bankaccountverification.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## initiate_bank_account_verification

Instant micro-deposit verification offers a quick and efficient way to verify bank account ownership. 

Send a $0.01 credit with a unique verification code via RTP or same-day ACH, depending on the receiving bank’s capabilities. This
feature provides a faster alternative to traditional methods, allowing verification in a single session.

It is recommended to use the `X-Wait-For: rail-response` header to synchronously receive the outcome of the instant credit in the
 response payload.

Possible verification methods:
  - `instant`: Real-time verification credit sent via RTP
  - `ach`: Verification credit sent via same-day ACH

Possible statuses:
  - `new`: Verification initiated, credit pending
  - `sent-credit`: Credit sent, available for verification in the external bank account
  - `failed`: Verification failed due to credit rejection/return, details in `exceptionDetails`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when generating a 
[token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.initiate_bank_account_verification(security=moov.InitiateBankAccountVerificationSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), x_wait_for=moov.BankAccountWaitFor.PAYMENT_METHOD, account_id="c2b4967e-86a5-474e-a78e-f013315f7dcc", bank_account_id="d648f8f3-7641-4e40-8a99-c08de14889c8")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                                 | [models.InitiateBankAccountVerificationSecurity](../../models/initiatebankaccountverificationsecurity.md)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                        |
| `x_wait_for`                                                                                                                                                                                                                               | [models.BankAccountWaitFor](../../models/bankaccountwaitfor.md)                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                         | Optional header to wait for certain events, such as the rail response, to occur before returning a response.<br/><br/>When this header is set to `rail-response`, the endpoint will wait for a sent-credit or failed status from the payment rail. |
| `account_id`                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                        |
| `bank_account_id`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                        |
| `x_moov_version`                                                                                                                                                                                                                           | [Optional[models.Versions]](../../models/versions.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                         | Specify an API version.                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                        |

### Response

**[models.BankAccountVerificationCreated](../../models/bankaccountverificationcreated.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## complete_bank_account_verification

Finalize the instant micro-deposit verification by submitting the verification code displayed in the user’s bank account. 

Upon successful verification, the bank account status will be updated to `verified` and eligible for ACH debit transactions.

The following formats are accepted:
- `MV0000`
- `mv0000`
- `0000`

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope when 
generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.bank_accounts.complete_bank_account_verification(security=moov.CompleteBankAccountVerificationSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="88cf5aa5-bf76-406e-a986-eb33cd8890e3", bank_account_id="0157260f-ae3c-496c-a9d8-24de5fbc6b31", code="MV1234")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.CompleteBankAccountVerificationSecurity](../../models/completebankaccountverificationsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `account_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `bank_account_id`                                                                                         | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `code`                                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Code provided by user from their bank account transactions                                                | MV1234                                                                                                    |
| `x_moov_version`                                                                                          | [Optional[models.Versions]](../../models/versions.md)                                                     | :heavy_minus_sign:                                                                                        | Specify an API version.                                                                                   |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.BankAccountVerification](../../models/bankaccountverification.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409, 422       | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |