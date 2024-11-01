# Accounts
(*accounts*)

## Overview

[Accounts](https://docs.moov.io/guides/accounts/) represent a legal entity (either a business or an individual) in Moov. You can create an account for yourself or set up accounts for others, requesting different [capabilities](https://docs.moov.io/guides/accounts/capabilities/) depending on what you need to be able to do with that account. You can retrieve an account to get details on the business or individual account holder, such as an email address or employer identification number (EIN).

Based on the type of account and its requested capabilities, we have certain [verification requirements](https://docs.moov.io/guides/accounts/identity-verification/). To see what capabilities that account has, you can use the [GET capability endpoint](https://docs.moov.io/api/moov-accounts/capabilities/get/).

When you sign up for the Moov Dashboard, you will have a **facilitator account** which can be used to facilitate money movement between other accounts. A facilitator account will not show up in your list of accounts and cannot be created via API. To update your facilitator account information, use the settings page of the Moov Dashboard.

You can disconnect an account within the account's settings in the Moov Dashboard. This action cannot be undone. When an account is disconnected, the account's history and wallet is retained, but transfers cannot be submitted, and no actions can be taken on the account. See the [Dashboard](https://docs.moov.io/guides/dashboard/accounts/#disconnect-accounts) guide for more information. It is not possible to permanently delete an account.


### Available Operations

* [list_accounts](#list_accounts) - List accounts
* [create_account](#create_account) - Create account
* [get_account](#get_account) - Get account
* [patch_account](#patch_account) - Patch account
* [disconnect_account](#disconnect_account) - Disconnect account
* [get_terms_of_service_token](#get_terms_of_service_token) - Get terms of service token
* [get_account_countries](#get_account_countries) - Get account countries
* [assign_account_countries](#assign_account_countries) - Assign Account Countries

## list_accounts

List or search accounts to which the caller is connected.<br><br>
All supported query parameters are optional. If none are provided
the response will include all connected accounts. Pagination is
supported via the `skip` and `count` query parameters.<br><br>
Searching by name and email will overlap and return results based on relevance.
<br><br> To use this endpoint from the browser, you'll need to specify the `/accounts.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.list_accounts(request={
    "name": "Frank",
    "email": "someone@moov.io",
    "type": moov.AccountType.BUSINESS,
    "foreign_id": "4528aba-b9a1-11eb-8529-0242ac13003",
    "include_disconnected": True,
    "count": 10,
    "skip": 10,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListAccountsRequest](../../models/listaccountsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAccountsResponse](../../models/listaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_account

You can create **business** or **individual** accounts for your users (i.e., customers, merchants) by passing the required information to Moov. Requirements differ per account type and requested [capabilities](https://docs.moov.io/guides/accounts/capabilities/requirements/).

If you're requesting the `wallet`, `send-funds`, `collect-funds`, or `card-issuing` capabilities, you'll need to:
  + Send Moov the user [platform terms of service agreement](https://docs.moov.io/guides/accounts/requirements/platform-agreement/) acceptance. This can be done upon account creation, or by [patching](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account using the `termsOfService` field.

If you're creating a business account with the business type `llc`, `partnership`, or `privateCorporation`, you'll need to:
  + Provide [business representatives](https://docs.moov.io/api/moov-accounts/representatives/) after creating the account.
  + [Patch](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account to indicate that business representative ownership information is complete.

Visit our documentation to read more about [creating accounts](https://docs.moov.io/guides/accounts/create-accounts/) and [verification requirements](https://docs.moov.io/guides/accounts/requirements/identity-verification/).

Note that the `mode` field (for production or sandbox) is only required when creating a _facilitator_ account. All non-facilitator account requests will ignore the mode field and be set to the calling facilitator's mode.

To use this endpoint from the browser, you will need to specify the `/accounts.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import dateutil.parser
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.create_account(create_account_request={
    "account_type": moov.AccountType.BUSINESS,
    "profile": {
        "individual": {
            "name": {
                "first_name": "Amanda",
                "last_name": "Yang",
                "middle_name": "Amanda",
                "suffix": "Jr",
            },
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "amanda@classbooker.dev",
            "address": {
                "address_line1": "123 Main Street",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
                "address_line2": "Apt 302",
            },
            "birth_date": {
                "day": 9,
                "month": 11,
                "year": 1989,
            },
            "government_id": {
                "ssn": {
                    "full": "123-45-6789",
                    "last_four": "6789",
                },
                "itin": {
                    "full": "123-45-6789",
                    "last_four": "6789",
                },
            },
        },
        "business": {
            "legal_business_name": "Whole Body Fitness LLC",
            "doing_business_as": "Whole Body Fitness",
            "business_type": moov.CreateProfileBusinessType.LLC,
            "address": {
                "address_line1": "123 Main Street",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
                "address_line2": "Apt 302",
            },
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "amanda@classbooker.dev",
            "website": "www.wholebodyfitnessgym.com",
            "description": "Local fitness center paying out instructors",
            "tax_id": {
                "ein": {
                    "number": "123-45-6789",
                },
            },
            "industry_codes": {
                "naics": "713940",
                "sic": "7991",
                "mcc": "7997",
            },
            "primary_regulator": moov.CreateProfilePrimaryRegulator.FDIC,
        },
    },
    "mode": moov.Mode.PRODUCTION,
    "terms_of_service": {
        "accepted_date": dateutil.parser.isoparse("2023-02-09T13:16:05.687Z"),
        "accepted_ip": "127.0.0.1",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://placekitten.com/408/287",
    },
    "foreign_id": "4528aba-b9a1-11eb-8529-0242ac13003",
    "customer_support": {
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "amanda@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
            "address_line2": "Apt 302",
        },
        "website": "www.wholebodyfitnessgym.com",
    },
    "settings": {
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `create_account_request`                                                                                                     | [models.CreateAccountRequest](../../models/createaccountrequest.md)                                                          | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `x_wait_for`                                                                                                                 | [Optional[models.AccountWaitFor]](../../models/accountwaitfor.md)                                                            | :heavy_minus_sign:                                                                                                           | Optional header that indicates whether to wait for the connection to be created before returning from the account creation.<br/> |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.CreateAccountResponse](../../models/createaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_account

Retrieves details for the account with the specified ID. <br><br> To use this endpoint from the browser, you will need to specify the `/accounts/{accountID}/profile.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.get_account(account_id="45ce7519-7f28-40c8-94bf-6edae7a38315")

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

**[models.GetAccountResponse](../../models/getaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## patch_account

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.

When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.


### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.patch_account(account_id="909eaa52-1ebf-4c4c-8919-f7385408829e", patch_account_request={
    "profile": {
        "individual": {
            "name": {
                "first_name": "Amanda",
                "last_name": "Yang",
                "middle_name": "Amanda",
                "suffix": "Jr",
            },
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "amanda@classbooker.dev",
            "address": {
                "address_line1": "123 Main Street",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
                "address_line2": "Apt 302",
            },
            "birth_date": {
                "day": 9,
                "month": 11,
                "year": 1989,
            },
            "government_id": {
                "ssn": {
                    "full": "123-45-6789",
                    "last_four": "6789",
                },
                "itin": {
                    "full": "123-45-6789",
                    "last_four": "6789",
                },
            },
        },
        "business": {
            "legal_business_name": "Whole Body Fitness LLC",
            "doing_business_as": "Whole Body Fitness",
            "business_type": moov.PatchAccountRequestBusinessType.LLC,
            "address": {
                "address_line1": "123 Main Street",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
                "address_line2": "Apt 302",
            },
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "amanda@classbooker.dev",
            "website": "www.wholebodyfitnessgym.com",
            "description": "Local fitness center paying out instructors",
            "tax_id": {
                "ein": {
                    "number": "123-45-6789",
                },
            },
            "industry_codes": {
                "naics": "713940",
                "sic": "7991",
                "mcc": "7997",
            },
            "primary_regulator": moov.PatchAccountRequestPrimaryRegulator.FDIC,
        },
    },
    "terms_of_service": {
        "token": "kgT1uxoMAk7QKuyJcmQE8nqW_HjpyuXBabiXPi6T83fUQoxsyWYPcYzuHQTqrt7YRp4gCwyDQvb6U5REM9Pgl2EloCe35t-eiMAbUWGo3Kerxme6aqNcKrP_6-v0MTXViOEJ96IBxPFTvMV7EROI2dq3u4e-x4BbGSCedAX-ViAQND6hcreCDXwrO6sHuzh5Xi2IzSqZHxaovnWEboaxuZKRJkA3dsFID6fzitMpm2qrOh4",
    },
    "foreign_id": "4528aba-b9a1-11eb-8529-0242ac13003",
    "customer_support": {
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "amanda@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
            "address_line2": "Apt 302",
        },
        "website": "www.wholebodyfitnessgym.com",
    },
    "settings": {
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `patch_account_request`                                             | [models.PatchAccountRequest](../../models/patchaccountrequest.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchAccountResponse](../../models/patchaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disconnect_account

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.

This will sever the connection between you and the account specified and it will no longer be listed as active in the list of accounts. This also means you'll only have read-only access to the account going forward for reporting purposes.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.disconnect_account(account_id="97814a93-ba26-470e-bb15-3cb32711e8ea")

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

**[models.DisconnectAccountResponse](../../models/disconnectaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_terms_of_service_token

Generates a non-expiring token that can then be used to accept Moov's terms of service. This token can only be generated via API. Any Moov account requesting the `collect-funds`, `send-funds`, `wallet`, or `card-issuing` capabilities must accept Moov's terms of service, then have the generated terms of service token patched to the account. Read more in our [docs](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.get_terms_of_service_token()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TermsOfServiceToken](../../models/termsofservicetoken.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_account_countries

Retrieve the specified countries of operation for an account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.get_account_countries(account_id="df471fd8-7bb3-4db3-bf74-52fe588b8d2b")

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

**[models.GetAccountCountriesResponse](../../models/getaccountcountriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## assign_account_countries

Assign the countries of operation for an account. This endpoint will always overwrite the previously assigned values. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.accounts.assign_account_countries(account_id="9ba3f09c-c93c-4ca1-b68f-1dbb0841a40a", countries={
    "countries": [
        "United States",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `countries`                                                         | [models.Countries](../../models/countries.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AssignAccountCountriesResponse](../../models/assignaccountcountriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |