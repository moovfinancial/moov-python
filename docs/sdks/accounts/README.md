# Accounts
(*accounts*)

## Overview

### Available Operations

* [create_account](#create_account) - You can create **business** or **individual** accounts for your users (i.e., customers, merchants) by passing the required
information to Moov. Requirements differ per account type and requested [capabilities](https://docs.moov.io/guides/accounts/capabilities/requirements/).

If you're requesting the `wallet`, `send-funds`, `collect-funds`, or `card-issuing` capabilities, you'll need to:
  + Send Moov the user [platform terms of service agreement](https://docs.moov.io/guides/accounts/requirements/platform-agreement/) acceptance.
    This can be done upon account creation, or by [patching](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account using the `termsOfService` field.
If you're creating a business account with the business type `llc`, `partnership`, or `privateCorporation`, you'll need to:
  + Provide [business representatives](https://docs.moov.io/api/moov-accounts/representatives/) after creating the account.
  + [Patch](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account to indicate that business representative ownership information is complete.

Visit our documentation to read more about [creating accounts](https://docs.moov.io/guides/accounts/create-accounts/) and [verification requirements](https://docs.moov.io/guides/accounts/requirements/identity-verification/).
Note that the `mode` field (for production or sandbox) is only required when creating a _facilitator_ account. All non-facilitator account requests will ignore the mode field and be set to the calling facilitator's mode.
* [list_accounts](#list_accounts) - List or search accounts to which the caller is connected.

All supported query parameters are optional. If none are provided the response will include all connected accounts.
Pagination is supported via the `skip` and `count` query parameters.
Searching by name and email will overlap and return results based on relevance.
* [get_account](#get_account) - Retrieves details for the account with the specified ID.
* [patch_account](#patch_account) - When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.
* [disconnect_account](#disconnect_account) -   This will sever the connection between you and the account specified and it will no longer be listed as active in the list of accounts. 
  This also means you'll only have read-only access to the account going forward for reporting purposes.

  To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope when generating 
  a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.
* [get_account_countries](#get_account_countries) - Retrieve the specified countries of operation for an account. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [assign_account_countries](#assign_account_countries) - Assign the countries of operation for an account.

This endpoint will always overwrite the previously assigned values. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_merchant_processing_agreement](#get_merchant_processing_agreement) - Retrieve a merchant account's processing agreement.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [get_terms_of_service_token](#get_terms_of_service_token) -   Generates a non-expiring token that can then be used to accept Moov’s terms of service. 

  This token can only be generated via API. Any Moov account requesting the collect funds, send funds, wallet, or card issuing capabilities 
  must accept Moov’s terms of service, then have the generated terms of service token patched to the account. Read more in our [documentation](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

## create_account

You can create **business** or **individual** accounts for your users (i.e., customers, merchants) by passing the required
information to Moov. Requirements differ per account type and requested [capabilities](https://docs.moov.io/guides/accounts/capabilities/requirements/).

If you're requesting the `wallet`, `send-funds`, `collect-funds`, or `card-issuing` capabilities, you'll need to:
  + Send Moov the user [platform terms of service agreement](https://docs.moov.io/guides/accounts/requirements/platform-agreement/) acceptance.
    This can be done upon account creation, or by [patching](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account using the `termsOfService` field.
If you're creating a business account with the business type `llc`, `partnership`, or `privateCorporation`, you'll need to:
  + Provide [business representatives](https://docs.moov.io/api/moov-accounts/representatives/) after creating the account.
  + [Patch](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account to indicate that business representative ownership information is complete.

Visit our documentation to read more about [creating accounts](https://docs.moov.io/guides/accounts/create-accounts/) and [verification requirements](https://docs.moov.io/guides/accounts/requirements/identity-verification/).
Note that the `mode` field (for production or sandbox) is only required when creating a _facilitator_ account. All non-facilitator account requests will ignore the mode field and be set to the calling facilitator's mode.

### Example Usage

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.create_account(security=operations.CreateAccountSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_type=components.AccountType.BUSINESS, profile=components.CreateProfile(
        business={
            "legal_business_name": "Classbooker, LLC",
        },
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": dateutil.parser.isoparse("2024-02-09T13:16:05.687Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://remorseful-finger.name/",
    }, customer_support={
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "jordan.lee@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
            "address_line2": "Apt 302",
        },
    }, settings={
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                 | [operations.CreateAccountSecurity](../../models/operations/createaccountsecurity.md)                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `account_type`                                                                                                                                                                             | [components.AccountType](../../models/components/accounttype.md)                                                                                                                           | :heavy_check_mark:                                                                                                                                                                         | The type of entity represented by this account.                                                                                                                                            | business                                                                                                                                                                                   |
| `profile`                                                                                                                                                                                  | [components.CreateProfile](../../models/components/createprofile.md)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `x_moov_version`                                                                                                                                                                           | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | Specify an API version.                                                                                                                                                                    |                                                                                                                                                                                            |
| `x_wait_for`                                                                                                                                                                               | [Optional[components.AccountWaitFor]](../../models/components/accountwaitfor.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Optional header that indicates whether to wait for the connection to be created before returning from the account creation.                                                                |                                                                                                                                                                                            |
| `metadata`                                                                                                                                                                                 | Dict[str, *str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                              | {<br/>"optional": "metadata"<br/>}                                                                                                                                                         |
| `terms_of_service`                                                                                                                                                                         | [Optional[components.CreateAccountTermsOfService]](../../models/components/createaccounttermsofservice.md)                                                                                 | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `foreign_id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Optional alias from a foreign/external system which can be used to reference this resource.                                                                                                |                                                                                                                                                                                            |
| `customer_support`                                                                                                                                                                         | [Optional[components.CustomerSupport]](../../models/components/customersupport.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                         | User-provided information that can be displayed on credit card transactions for customers to use when<br/>contacting a customer support team. This data is only allowed on a business account. |                                                                                                                                                                                            |
| `settings`                                                                                                                                                                                 | [Optional[components.Settings]](../../models/components/settings.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | User provided settings to manage an account.                                                                                                                                               |                                                                                                                                                                                            |
| `capabilities`                                                                                                                                                                             | List[[components.CapabilityID](../../models/components/capabilityid.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[components.Account](../../models/components/account.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GenericError              | 400, 409                         | application/json                 |
| errors.CreateAccountResponseBody | 422                              | application/json                 |
| errors.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list_accounts

List or search accounts to which the caller is connected.

All supported query parameters are optional. If none are provided the response will include all connected accounts.
Pagination is supported via the `skip` and `count` query parameters.
Searching by name and email will overlap and return results based on relevance.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.list_accounts(security=operations.ListAccountsSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), type_=components.AccountType.BUSINESS, skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                                                                                                                  | [operations.ListAccountsSecurity](../../models/operations/listaccountssecurity.md)                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |
| `x_moov_version`                                                                                                                                                                                                                                                                                                                                                            | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Specify an API version.                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                             |
| `name`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Filter connected accounts by name.<br/><br/>If provided, this query will attempt to find matches against the following Account and Profile fields:<br/><ul><br/>  <li>Account `displayName`</li><br/>  <li>Individual Profile `firstName`, `middleName`, and `lastName`</li><br/>  <li>Business Profile `legalBusinessName`</li><br/></ul>                                  |                                                                                                                                                                                                                                                                                                                                                                             |
| `email`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by email address.<br/><br/>  Provide the full email address to filter by email.                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                             |
| `type`                                                                                                                                                                                                                                                                                                                                                                      | [Optional[components.AccountType]](../../models/components/accounttype.md)                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by AccountType.<br/><br/>  If the `type` parameter is used in combination with `name`, only the corresponding type's name fields will<br/>  be searched. For example, if `type=business` and `name=moov`, the search will attempt to find matches against<br/>  the display name and Business Profile name fields (`legalBusinessName`, and `doingBusinessAs`). | business                                                                                                                                                                                                                                                                                                                                                                    |
| `foreign_id`                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Serves as an optional alias from a foreign/external system which can be used to reference this resource.                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
| `include_disconnected`                                                                                                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Filter disconnected accounts.<br/><br/>If true, the response will include disconnected accounts.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                             |
| `capability`                                                                                                                                                                                                                                                                                                                                                                | [Optional[components.CapabilityID]](../../models/components/capabilityid.md)                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by the capability.                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                             |
| `capability_status`                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.CapabilityStatus]](../../models/components/capabilitystatus.md)                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by the capability.                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                             |
| `skip`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         | 60                                                                                                                                                                                                                                                                                                                                                                          |
| `count`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         | 20                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |

### Response

**[List[components.Account]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_account

Retrieves details for the account with the specified ID.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.get_account(security=operations.GetAccountSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="45ce7519-7f28-40c8-94bf-6edae7a38315")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.GetAccountSecurity](../../models/operations/getaccountsecurity.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `account_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `x_moov_version`                                                               | [Optional[components.Versions]](../../models/components/versions.md)           | :heavy_minus_sign:                                                             | Specify an API version.                                                        |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[components.Account](../../models/components/account.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## patch_account

When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.patch_account(security=operations.PatchAccountSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="7909eaa5-21eb-4fc4-bc91-9f7385408829", account_type=components.AccountType.BUSINESS, profile=components.CreateProfileUpdate(
        business={
            "legal_business_name": "Classbooker, LLC",
        },
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "token": "kgT1uxoMAk7QKuyJcmQE8nqW_HjpyuXBabiXPi6T83fUQoxsyWYPcYzuHQTqrt7YRp4gCwyDQvb6U5REM9Pgl2EloCe35t-eiMAbUWGo3Kerxme6aqNcKrP_6-v0MTXViOEJ96IBxPFTvMV7EROI2dq3u4e-x4BbGSCedAX-ViAQND6hcreCDXwrO6sHuzh5Xi2IzSqZHxaovnWEboaxuZKRJkA3dsFID6fzitMpm2qrOh4",
    }, customer_support={
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "jordan.lee@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "address_line2": "Apt 302",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
        },
    }, settings={
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                 | [operations.PatchAccountSecurity](../../models/operations/patchaccountsecurity.md)                                                                                                         | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `account_id`                                                                                                                                                                               | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `x_moov_version`                                                                                                                                                                           | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | Specify an API version.                                                                                                                                                                    |                                                                                                                                                                                            |
| `account_type`                                                                                                                                                                             | [Optional[components.AccountType]](../../models/components/accounttype.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                         | The type of entity represented by this account.                                                                                                                                            | business                                                                                                                                                                                   |
| `profile`                                                                                                                                                                                  | [Optional[components.CreateProfileUpdate]](../../models/components/createprofileupdate.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `metadata`                                                                                                                                                                                 | Dict[str, *str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                              | {<br/>"optional": "metadata"<br/>}                                                                                                                                                         |
| `terms_of_service`                                                                                                                                                                         | [Optional[components.CreateAccountUpdateTermsOfService]](../../models/components/createaccountupdatetermsofservice.md)                                                                     | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `foreign_id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Optional alias from a foreign/external system which can be used to reference this resource.                                                                                                |                                                                                                                                                                                            |
| `customer_support`                                                                                                                                                                         | [Optional[components.CustomerSupportUpdate]](../../models/components/customersupportupdate.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                         | User-provided information that can be displayed on credit card transactions for customers to use when<br/>contacting a customer support team. This data is only allowed on a business account. |                                                                                                                                                                                            |
| `settings`                                                                                                                                                                                 | [Optional[components.SettingsUpdate]](../../models/components/settingsupdate.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | User provided settings to manage an account.                                                                                                                                               |                                                                                                                                                                                            |
| `capabilities`                                                                                                                                                                             | List[[components.CapabilityID](../../models/components/capabilityid.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[components.Account](../../models/components/account.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GenericError             | 400, 409                        | application/json                |
| errors.PatchAccountResponseBody | 422                             | application/json                |
| errors.APIError                 | 4XX, 5XX                        | \*/\*                           |

## disconnect_account

  This will sever the connection between you and the account specified and it will no longer be listed as active in the list of accounts. 
  This also means you'll only have read-only access to the account going forward for reporting purposes.

  To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope when generating 
  a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    moov.accounts.disconnect_account(security=operations.DisconnectAccountSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="97814a93-ba26-470e-bb15-3cb32711e8ea")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.DisconnectAccountSecurity](../../models/operations/disconnectaccountsecurity.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `x_moov_version`                                                                             | [Optional[components.Versions]](../../models/components/versions.md)                         | :heavy_minus_sign:                                                                           | Specify an API version.                                                                      |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_account_countries

Retrieve the specified countries of operation for an account. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.read` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.get_account_countries(security=operations.GetAccountCountriesSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="df471fd8-7bb3-4db3-bf74-52fe588b8d2b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetAccountCountriesSecurity](../../models/operations/getaccountcountriessecurity.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `x_moov_version`                                                                                 | [Optional[components.Versions]](../../models/components/versions.md)                             | :heavy_minus_sign:                                                                               | Specify an API version.                                                                          |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[components.AccountCountries](../../models/components/accountcountries.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## assign_account_countries

Assign the countries of operation for an account.

This endpoint will always overwrite the previously assigned values. 

To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/profile.write` scope when generating 
a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.assign_account_countries(security=operations.AssignAccountCountriesSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="9ba3f09c-c93c-4ca1-b68f-1dbb0841a40a", countries=[
        "United States",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `security`                                                                                             | [operations.AssignAccountCountriesSecurity](../../models/operations/assignaccountcountriessecurity.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `account_id`                                                                                           | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `countries`                                                                                            | List[*str*]                                                                                            | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `x_moov_version`                                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                                   | :heavy_minus_sign:                                                                                     | Specify an API version.                                                                                |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[components.AccountCountries](../../models/components/accountcountries.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GenericError         | 400, 409                    | application/json            |
| errors.AssignCountriesError | 422                         | application/json            |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_merchant_processing_agreement

Retrieve a merchant account's processing agreement.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.get_merchant_processing_agreement(security=operations.GetMerchantProcessingAgreementSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="d2cfd0d3-6efb-4bc4-a193-53f35dd0d912")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                             | [operations.GetMerchantProcessingAgreementSecurity](../../models/operations/getmerchantprocessingagreementsecurity.md) | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `account_id`                                                                                                           | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |
| `x_moov_version`                                                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                                                   | :heavy_minus_sign:                                                                                                     | Specify an API version.                                                                                                |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_terms_of_service_token

  Generates a non-expiring token that can then be used to accept Moov’s terms of service. 

  This token can only be generated via API. Any Moov account requesting the collect funds, send funds, wallet, or card issuing capabilities 
  must accept Moov’s terms of service, then have the generated terms of service token patched to the account. Read more in our [documentation](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components

with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.get_terms_of_service_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `x_moov_version`                                                                                               | [Optional[components.Versions]](../../models/components/versions.md)                                           | :heavy_minus_sign:                                                                                             | Specify an API version.                                                                                        |
| `origin`                                                                                                       | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | Indicates the domain from which the request originated. Required if referer header is not present.             |
| `referer`                                                                                                      | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | Specifies the URL of the resource from which the request originated. Required if origin header is not present. |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[components.TermsOfServiceToken](../../models/components/termsofservicetoken.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |