# Accounts
(*accounts*)

## Overview

### Available Operations

* [create](#create) - You can create **business** or **individual** accounts for your users (i.e., customers, merchants) by passing the required
information to Moov. Requirements differ per account type and requested [capabilities](https://docs.moov.io/guides/accounts/capabilities/requirements/).

If you're requesting the `wallet`, `send-funds`, `collect-funds`, or `card-issuing` capabilities, you'll need to:
  + Send Moov the user [platform terms of service agreement](https://docs.moov.io/guides/accounts/requirements/platform-agreement/) acceptance.
    This can be done upon account creation, or by [patching](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account using the `termsOfService` field.
If you're creating a business account with the business type `llc`, `partnership`, or `privateCorporation`, you'll need to:
  + Provide [business representatives](https://docs.moov.io/api/moov-accounts/representatives/) after creating the account.
  + [Patch](https://docs.moov.io/api/moov-accounts/accounts/patch/) the account to indicate that business representative ownership information is complete.

Visit our documentation to read more about [creating accounts](https://docs.moov.io/guides/accounts/create-accounts/) and [verification requirements](https://docs.moov.io/guides/accounts/requirements/identity-verification/).
Note that the `mode` field (for production or sandbox) is only required when creating a _facilitator_ account. All non-facilitator account requests will ignore the mode field and be set to the calling facilitator's mode.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.
* [list](#list) - List or search accounts to which the caller is connected.

All supported query parameters are optional. If none are provided the response will include all connected accounts.
Pagination is supported via the `skip` and `count` query parameters. Searching by name and email will overlap and 
return results based on relevance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.
* [get](#get) - Retrieves details for the account with the specified ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [update](#update) - When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.
* [disconnect](#disconnect) - This will sever the connection between you and the account specified and it will no longer be listed as 
active in the list of accounts. This also means you'll only have read-only access to the account going 
forward for reporting purposes.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope.
* [get_countries](#get_countries) - Retrieve the specified countries of operation for an account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [assign_countries](#assign_countries) - Assign the countries of operation for an account.

This endpoint will always overwrite the previously assigned values. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [get_merchant_processing_agreement](#get_merchant_processing_agreement) - Retrieve a merchant account's processing agreement.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [get_terms_of_service_token](#get_terms_of_service_token) - Generates a non-expiring token that can then be used to accept Moov's terms of service. 

This token can only be generated via API. Any Moov account requesting the collect funds, send funds, wallet, 
or card issuing capabilities must accept Moov's terms of service, then have the generated terms of service 
token patched to the account. Read more in our [documentation](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

## create

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

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.

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

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        individual=components.CreateIndividualProfile(
            name=components.IndividualName(
                first_name="Jordan",
                middle_name="Reese",
                last_name="Lee",
                suffix="Jr",
            ),
            phone=components.PhoneNumber(
                number="8185551212",
                country_code="1",
            ),
            email="jordan.lee@classbooker.dev",
            address=components.Address(
                address_line1="123 Main Street",
                address_line2="Apt 302",
                city="Boulder",
                state_or_province="CO",
                postal_code="80301",
                country="US",
            ),
            birth_date=components.BirthDate(
                day=9,
                month=11,
                year=1989,
            ),
        ),
        business=components.CreateBusinessProfile(
            legal_business_name="Classbooker, LLC",
            business_type=components.BusinessType.LLC,
            address=components.Address(
                address_line1="123 Main Street",
                address_line2="Apt 302",
                city="Boulder",
                state_or_province="CO",
                postal_code="80301",
                country="US",
            ),
            phone=components.PhoneNumber(
                number="8185551212",
                country_code="1",
            ),
            email="jordan.lee@classbooker.dev",
            description="Local fitness gym paying out instructors",
            tax_id=components.TaxID(
                ein=components.Ein(
                    number="12-3456789",
                ),
            ),
            industry_codes=components.IndustryCodes(
                naics="713940",
                sic="7991",
                mcc="7997",
            ),
        ),
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
    }, mode=components.Mode.PRODUCTION)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_type`                                                                                                                                                                             | [components.CreateAccountType](../../models/components/createaccounttype.md)                                                                                                               | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `profile`                                                                                                                                                                                  | [components.CreateProfile](../../models/components/createprofile.md)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `metadata`                                                                                                                                                                                 | Dict[str, *str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Free-form key-value pair list. Useful for storing information that is not captured elsewhere.                                                                                              | {<br/>"optional": "metadata"<br/>}                                                                                                                                                         |
| `terms_of_service`                                                                                                                                                                         | [Optional[components.CreateAccountTermsOfService]](../../models/components/createaccounttermsofservice.md)                                                                                 | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `foreign_id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Optional alias from a foreign/external system which can be used to reference this resource.                                                                                                |                                                                                                                                                                                            |
| `customer_support`                                                                                                                                                                         | [Optional[components.CustomerSupport]](../../models/components/customersupport.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                         | User-provided information that can be displayed on credit card transactions for customers to use when<br/>contacting a customer support team. This data is only allowed on a business account. |                                                                                                                                                                                            |
| `settings`                                                                                                                                                                                 | [Optional[components.Settings]](../../models/components/settings.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | User provided settings to manage an account.                                                                                                                                               |                                                                                                                                                                                            |
| `capabilities`                                                                                                                                                                             | List[[components.CapabilityID](../../models/components/capabilityid.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |                                                                                                                                                                                            |
| `mode`                                                                                                                                                                                     | [Optional[components.Mode]](../../models/components/mode.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                         | The operating mode for an account.                                                                                                                                                         | production                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[operations.CreateAccountResponse](../../models/operations/createaccountresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GenericError              | 400, 409                         | application/json                 |
| errors.CreateAccountResponseBody | 422                              | application/json                 |
| errors.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list

List or search accounts to which the caller is connected.

All supported query parameters are optional. If none are provided the response will include all connected accounts.
Pagination is supported via the `skip` and `count` query parameters. Searching by name and email will overlap and 
return results based on relevance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.

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

    res = moov.accounts.list(type_=components.AccountType.BUSINESS, skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Filter connected accounts by name.<br/><br/>If provided, this query will attempt to find matches against the following Account and Profile fields:<br/><ul><br/>  <li>Account `displayName`</li><br/>  <li>Individual Profile `firstName`, `middleName`, and `lastName`</li><br/>  <li>Business Profile `legalBusinessName`</li><br/></ul>                                  |                                                                                                                                                                                                                                                                                                                                                                             |
| `email`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by email address.<br/><br/>  Provide the full email address to filter by email.                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                             |
| `type`                                                                                                                                                                                                                                                                                                                                                                      | [Optional[components.AccountType]](../../models/components/accounttype.md)                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by AccountType.<br/><br/>  If the `type` parameter is used in combination with `name`, only the corresponding type's name fields will<br/>  be searched. For example, if `type=business` and `name=moov`, the search will attempt to find matches against<br/>  the display name and Business Profile name fields (`legalBusinessName`, and `doingBusinessAs`). | business                                                                                                                                                                                                                                                                                                                                                                    |
| `include_guest`                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter accounts with AccountType guest.<br/>  <br/>  If true, the response will include guest accounts.                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                             |
| `foreign_id`                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Serves as an optional alias from a foreign/external system which can be used to reference this resource.                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
| `include_disconnected`                                                                                                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Filter disconnected accounts.<br/><br/>If true, the response will include disconnected accounts.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                             |
| `capability`                                                                                                                                                                                                                                                                                                                                                                | [Optional[components.CapabilityID]](../../models/components/capabilityid.md)                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by the capability.                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                             |
| `capability_status`                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.CapabilityStatus]](../../models/components/capabilitystatus.md)                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          |   Filter connected accounts by the capability.                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                             |
| `skip`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         | 60                                                                                                                                                                                                                                                                                                                                                                          |
| `count`                                                                                                                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                         | 20                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |

### Response

**[operations.ListAccountsResponse](../../models/operations/listaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves details for the account with the specified ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.

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

    res = moov.accounts.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAccountResponse](../../models/operations/getaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.

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

    res = moov.accounts.update(account_id="95fa7f0e-7432-4ce4-a7cb-60cc78135dde", profile=components.PatchProfile(
        individual=components.PatchIndividual(
            name=components.IndividualNameUpdate(
                first_name="Jordan",
                middle_name="Reese",
                last_name="Lee",
                suffix="Jr",
            ),
            phone=components.PhoneNumber(
                number="8185551212",
                country_code="1",
            ),
            email="jordan.lee@classbooker.dev",
            address=components.AddressUpdate(
                address_line1="123 Main Street",
                address_line2="Apt 302",
                city="Boulder",
                state_or_province="CO",
                postal_code="80301",
                country="US",
            ),
            birth_date=components.BirthDateUpdate(
                day=9,
                month=11,
                year=1989,
            ),
        ),
        business=components.PatchBusiness(
            business_type=components.BusinessType.LLC,
            address=components.AddressUpdate(
                address_line1="123 Main Street",
                address_line2="Apt 302",
                city="Boulder",
                state_or_province="CO",
                postal_code="80301",
                country="US",
            ),
            phone=components.PhoneNumber(
                number="8185551212",
                country_code="1",
            ),
            email="jordan.lee@classbooker.dev",
            tax_id=components.TaxIDUpdate(
                ein=components.TaxIDUpdateEin(
                    number="12-3456789",
                ),
            ),
            industry_codes=components.IndustryCodes(
                naics="713940",
                sic="7991",
                mcc="7997",
            ),
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
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
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                 | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `profile`                                                                                                                    | [Optional[components.PatchProfile]](../../models/components/patchprofile.md)                                                 | :heavy_minus_sign:                                                                                                           | Describes the fields available when patching a profile.<br/>Each object can be patched independent of patching the other fields. |                                                                                                                              |
| `metadata`                                                                                                                   | Dict[str, *str*]                                                                                                             | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          | {<br/>"optional": "metadata"<br/>}                                                                                           |
| `terms_of_service`                                                                                                           | [Optional[components.PatchAccountTermsOfService]](../../models/components/patchaccounttermsofservice.md)                     | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `foreign_id`                                                                                                                 | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `customer_support`                                                                                                           | [OptionalNullable[components.PatchAccountCustomerSupport]](../../models/components/patchaccountcustomersupport.md)           | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `settings`                                                                                                                   | [Optional[components.CreateAccountSettings]](../../models/components/createaccountsettings.md)                               | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[operations.UpdateAccountResponse](../../models/operations/updateaccountresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GenericError              | 400, 409                         | application/json                 |
| errors.UpdateAccountResponseBody | 422                              | application/json                 |
| errors.APIError                  | 4XX, 5XX                         | \*/\*                            |

## disconnect

This will sever the connection between you and the account specified and it will no longer be listed as 
active in the list of accounts. This also means you'll only have read-only access to the account going 
forward for reporting purposes.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope.

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

    res = moov.accounts.disconnect(account_id="ac3cbe09-fcd4-4c5e-ada2-89eaaa9c149e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DisconnectAccountResponse](../../models/operations/disconnectaccountresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_countries

Retrieve the specified countries of operation for an account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

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

    res = moov.accounts.get_countries(account_id="b49c57bf-7b36-4308-8206-c1f5ce8067ac")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAccountCountriesResponse](../../models/operations/getaccountcountriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## assign_countries

Assign the countries of operation for an account.

This endpoint will always overwrite the previously assigned values. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

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

    res = moov.accounts.assign_countries(account_id="aa2dc19b-77dd-481f-a0a8-c76f2cfc1372", countries=[
        "United States",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `countries`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.AssignAccountCountriesResponse](../../models/operations/assignaccountcountriesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GenericError         | 400, 409                    | application/json            |
| errors.AssignCountriesError | 422                         | application/json            |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_merchant_processing_agreement

Retrieve a merchant account's processing agreement.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

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

    res = moov.accounts.get_merchant_processing_agreement(account_id="d2cfd0d3-6efb-4bc4-a193-53f35dd0d912")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetMerchantProcessingAgreementResponse](../../models/operations/getmerchantprocessingagreementresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_terms_of_service_token

Generates a non-expiring token that can then be used to accept Moov's terms of service. 

This token can only be generated via API. Any Moov account requesting the collect funds, send funds, wallet, 
or card issuing capabilities must accept Moov's terms of service, then have the generated terms of service 
token patched to the account. Read more in our [documentation](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

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
| `origin`                                                                                                       | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | Indicates the domain from which the request originated. Required if referer header is not present.             |
| `referer`                                                                                                      | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | Specifies the URL of the resource from which the request originated. Required if origin header is not present. |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.GetTermsOfServiceTokenResponse](../../models/operations/gettermsofservicetokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |