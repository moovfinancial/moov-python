# Moov Python

The official SDK for interacting with the Moov API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=moovio-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary

Moov API: Moov is a platform that enables developers to integrate all aspects of money movement with ease and speed.
The Moov API makes it simple for platforms to send, receive, and store money. Our API is based upon REST
principles, returns JSON responses, and uses standard HTTP response codes. To learn more about how Moov
works at a high level, read our [concepts](https://docs.moov.io/guides/get-started/glossary/) guide.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Moov Python](https://github.com/moovfinancial/moov-python/blob/master/#moov-python)
  * [SDK Installation](https://github.com/moovfinancial/moov-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/moovfinancial/moov-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/moovfinancial/moov-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/moovfinancial/moov-python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/moovfinancial/moov-python/blob/master/#available-resources-and-operations)
  * [File uploads](https://github.com/moovfinancial/moov-python/blob/master/#file-uploads)
  * [Retries](https://github.com/moovfinancial/moov-python/blob/master/#retries)
  * [Error Handling](https://github.com/moovfinancial/moov-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/moovfinancial/moov-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/moovfinancial/moov-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/moovfinancial/moov-python/blob/master/#resource-management)
  * [Debugging](https://github.com/moovfinancial/moov-python/blob/master/#debugging)
* [Development](https://github.com/moovfinancial/moov-python/blob/master/#development)
  * [Maturity](https://github.com/moovfinancial/moov-python/blob/master/#maturity)
  * [Contributions](https://github.com/moovfinancial/moov-python/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install moovio_sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add moovio_sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from moovio_sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "moovio_sdk",
# ]
# ///

from moovio_sdk import Moov

sdk = Moov(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime

async def main():

    async with Moov(
        x_moov_version="v2024.01.00",
        security=components.Security(
            username="",
            password="",
        ),
    ) as moov:

        res = await moov.accounts.create_async(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
            business=components.CreateBusinessProfile(
                legal_business_name="Whole Body Fitness LLC",
            ),
        ), metadata={
            "optional": "metadata",
        }, terms_of_service={
            "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
            "accepted_ip": "172.217.2.46",
            "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
            "accepted_domain": "https://esteemed-velocity.net",
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                      | Type | Scheme     | Environment Variable                |
| ------------------------- | ---- | ---------- | ----------------------------------- |
| `username`<br/>`password` | http | HTTP Basic | `MOOV_USERNAME`<br/>`MOOV_PASSWORD` |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
    x_moov_version="v2024.01.00",
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account_terminal_applications](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accountterminalapplications/README.md)

* [link](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accountterminalapplications/README.md#link) - Link an account with a terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accountterminalapplications/README.md#list) - Retrieve all terminal applications linked to a specific account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accountterminalapplications/README.md#get) - Verifies if a specific Terminal Application is linked to an Account. This endpoint acts as a validation check for the link's existence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-applications.read` scope.
* [get_configuration](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accountterminalapplications/README.md#get_configuration) - Fetch the configuration for a given Terminal Application linked to a specific Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/terminal-configuration.read` scope.

### [accounts](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#create) - You can create **business** or **individual** accounts for your users (i.e., customers, merchants) by passing the required
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
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#list) - List or search accounts to which the caller is connected.

All supported query parameters are optional. If none are provided the response will include all connected accounts.
Pagination is supported via the `skip` and `count` query parameters. Searching by name and email will overlap and 
return results based on relevance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#get) - Retrieves details for the account with the specified ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#update) - When **can** profile data be updated:
  + For unverified accounts, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified accounts can only add missing profile data.

  When **can't** profile data be updated:
  + Verified accounts cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/profile.write` scope.
* [disconnect](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#disconnect) - This will sever the connection between you and the account specified and it will no longer be listed as 
active in the list of accounts. This also means you'll only have read-only access to the account going 
forward for reporting purposes.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.disconnect` scope.
* [get_countries](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#get_countries) - Retrieve the specified countries of operation for an account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [assign_countries](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#assign_countries) - Assign the countries of operation for an account.

This endpoint will always overwrite the previously assigned values. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [get_merchant_processing_agreement](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#get_merchant_processing_agreement) - Retrieve a merchant account's processing agreement.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [get_terms_of_service_token](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/accounts/README.md#get_terms_of_service_token) - Generates a non-expiring token that can then be used to accept Moov's terms of service. 

This token can only be generated via API. Any Moov account requesting the collect funds, send funds, wallet, 
or card issuing capabilities must accept Moov's terms of service, then have the generated terms of service 
token patched to the account. Read more in our [documentation](https://docs.moov.io/guides/accounts/requirements/platform-agreement/).

### [adjustments](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/adjustments/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/adjustments/README.md#list) - List adjustments associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/adjustments/README.md#get) - Retrieve a specific adjustment associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### [apple_pay](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md)

* [register_merchant_domains](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md#register_merchant_domains) - Add domains to be registered with Apple Pay.

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [update_merchant_domains](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md#update_merchant_domains) - Add or remove domains to be registered with Apple Pay. 

Any domains that will be used to accept payments must first be [verified](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) 
with Apple.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [get_merchant_domains](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md#get_merchant_domains) - Get domains registered with Apple Pay. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.read` scope.
* [create_session](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md#create_session) - Create a session with Apple Pay to facilitate a payment. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
A successful response from this endpoint should be passed through to Apple Pay unchanged. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/apple-pay.write` scope.
* [link_token](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/applepay/README.md#link_token) - Connect an Apple Pay token to the specified account. 

Read our [Apple Pay tutorial](https://docs.moov.io/guides/sources/cards/apple-pay/#register-your-domains) to learn more. 
The `token` data is defined by Apple Pay and should be passed through from Apple Pay's response unmodified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

### [authentication](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/authentication/README.md)

* [revoke_access_token](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/authentication/README.md#revoke_access_token) - Revoke an auth token.

Allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed.
* [create_access_token](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/authentication/README.md#create_access_token) - Create or refresh an access token.

### [avatars](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/avatars/README.md)

* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/avatars/README.md#get) - Get avatar image for an account using a unique ID.    

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/profile-enrichment.read` scope.

### [bank_accounts](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md)

* [link](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#link) - Link a bank account to an existing Moov account. Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more.

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked
bank-account is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#list) - List all the bank accounts associated with a particular Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#get) - Retrieve bank account details (i.e. routing number or account type) associated with a specific Moov account. 

Read our [bank accounts guide](https://docs.moov.io/guides/sources/bank-accounts/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope.
* [disable](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#disable) - Discontinue using a specified bank account linked to a Moov account. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.
* [initiate_micro_deposits](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#initiate_micro_deposits) - Micro-deposits help confirm bank account ownership, helping reduce fraud and the risk of unauthorized activity. 
Use this method to initiate the micro-deposit verification, sending two small credit transfers to the bank account 
you want to confirm.

If you request micro-deposits before 4:15PM ET, they will appear that same day. If you request micro-deposits any 
time after 4:15PM ET, they will appear the next banking day. When the two credits are initiated, Moov simultaneously
initiates a debit to recoup the micro-deposits. 

Micro-deposits initiated for a `sandbox` bank account will always be `$0.00` / `$0.00` and instantly verifiable once initiated.

You can simulate micro-deposit verification in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#micro-deposits)
guide for more information.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.
* [complete_micro_deposits](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#complete_micro_deposits) - Complete the micro-deposit validation process by passing the amounts of the two transfers within three tries.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.
* [get_verification](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#get_verification) - Retrieve the current status and details of an instant verification, including whether the verification method was instant or same-day 
ACH. This helps track the verification process in real-time and provides details in case of exceptions.

The status will indicate the following:

- `new`: Verification initiated, credit pending to the payment network
- `sent-credit`: Credit sent, available for verification
- `failed`: Verification failed, description provided, user needs to add a new bank account
- `expired`: Verification expired after 14 days, initiate another verification
- `max-attempts-exceeded`: Five incorrect code attempts exhausted, initiate another verification

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.read` scope.
* [initiate_verification](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#initiate_verification) - Instant micro-deposit verification offers a quick and efficient way to verify bank account ownership. 

Send a $0.01 credit with a unique verification code via RTP or same-day ACH, depending on the receiving bank's capabilities. This
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

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.
* [complete_verification](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/bankaccounts/README.md#complete_verification) - Finalize the instant micro-deposit verification by submitting the verification code displayed in the user's bank account. 

Upon successful verification, the bank account status will be updated to `verified` and eligible for ACH debit transactions.

The following formats are accepted:
- `MV0000`
- `mv0000`
- `0000`

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/bank-accounts.write` scope.

### [branding](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/branding/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/branding/README.md#create) - Create brand properties for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/branding.write` scope.
* [upsert](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/branding/README.md#upsert) - Create or replace brand properties for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/branding.write` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/branding/README.md#get) - Get brand properties for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/branding.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/branding/README.md#update) - Updates the brand properties for the specified account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/branding.write` scope.

### [capabilities](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/capabilities/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/capabilities/README.md#list) - Retrieve all the capabilities an account has requested.

Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.
* [request](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/capabilities/README.md#request) - Request capabilities for a specific account. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/capabilities/README.md#get) - Retrieve a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.read` scope.
* [disable](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/capabilities/README.md#disable) - Disable a specific capability that an account has requested. Read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/) to learn more.

  To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/capabilities.write` scope.

### [card_issuing](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md)

* [request](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md#request) - Request a virtual card be issued.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md#list) - List Moov issued cards existing for the account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md#get) - Retrieve a single issued card associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md#update) - Update a Moov issued card.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.write` scope.
* [get_full](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cardissuing/README.md#get_full) - Get issued card with PAN, CVV, and expiration. 

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read-secure` scope.

### [cards](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md)

* [link](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md#link) - Link a card to an existing Moov account. 

Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/#link-a-card) to learn more.

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance. 

During card linking, the provided data will be verified by submitting a $0 authorization (account verification) request. 
If `merchantAccountID` is provided, the authorization request will contain that account's statement descriptor and address. 
Otherwise, the platform account's profile will be used. If no statement descriptor has been set, the authorization will 
use the account's name instead.

It is strongly recommended that callers include the `X-Wait-For` header, set to `payment-method`, if the newly linked 
card is intended to be used right away. If this header is not included, the caller will need to poll the [List Payment 
Methods](https://docs.moov.io/api/sources/payment-methods/list/)
endpoint to wait for the new payment methods to be available for use.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md#list) - List all the active cards associated with a Moov account. 

Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md#get) - Fetch a specific card associated with a Moov account. 

Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md#update) - Update a linked card and/or resubmit it for verification. 

If a value is provided for CVV, a new verification ($0 authorization) will be submitted for the card. Updating the expiration 
date or 
address will update the information stored on file for the card but will not be verified.

Read our [accept card payments guide](https://docs.moov.io/guides/sources/cards/accept-card-payments/#reverify-a-card) to learn 
more.

Only use this endpoint if you have provided Moov with a copy of your PCI attestation of compliance. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.
* [disable](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/cards/README.md#disable) - Disables a card associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/cards.write` scope.

### [disputes](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#list) - Returns the list of disputes. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#get) - Get a dispute by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [accept](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#accept) - Accepts liability for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_evidence](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#list_evidence) - Returns a dispute's public evidence by its ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [upload_evidence_file](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#upload_evidence_file) - Uploads a file as evidence for a dispute. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [upload_evidence_text](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#upload_evidence_text) - Uploads text as evidence for a dispute.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [submit_evidence](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#submit_evidence) - Submit the evidence associated with a dispute.

Evidence items must be uploaded using the appropriate endpoint(s) prior to calling this endpoint to submit it. **Evidence can only
be submitted once per dispute.**

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_evidence](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#get_evidence) - Get dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update_evidence](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#update_evidence) - Updates dispute evidence by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [delete_evidence](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#delete_evidence) - Deletes dispute evidence by ID. 

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_evidence_data](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/disputes/README.md#get_evidence_data) - Downloads dispute evidence data by ID.

Read our [disputes guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/disputes/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### [end_to_end_encryption](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/endtoendencryption/README.md)

* [test_encrypted_token](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/endtoendencryption/README.md#test_encrypted_token) - Allows for testing a JWE token to ensure it's acceptable by Moov. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/ping.read` scope.
* [generate_key](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/endtoendencryption/README.md#generate_key) - Generates a public key used to create a JWE token for passing secure authentication data through non-PCI compliant intermediaries.

### [enriched_address](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/enrichedaddress/README.md)

* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/enrichedaddress/README.md#get) - Fetch enriched address suggestions. Requires a partial address. 
  
To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/profile-enrichment.read` scope.

### [enriched_profile](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/enrichedprofile/README.md)

* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/enrichedprofile/README.md#get) - Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/profile-enrichment.read` scope.

### [fee_plans](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md)

* [list_fee_plan_agreements](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#list_fee_plan_agreements) - List all fee plan agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [create_fee_plan_agreements](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#create_fee_plan_agreements) - Creates the subscription of a fee plan to a merchant account. Merchants are required to accept the fee plan terms prior to activation.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [list_fee_plans](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#list_fee_plans) - List all fee plans available for use by an account. This is intended to be used by an account when 
selecting a fee plan to apply to a connected account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [retrieve_fees](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#retrieve_fees) - Retrieve fees associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_fees_fetch](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#list_fees_fetch) - List fees associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [list_partner_pricing](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#list_partner_pricing) - List all partner pricing plans available for use by an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [list_partner_pricing_agreements](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/feeplans/README.md#list_partner_pricing_agreements) - List all partner pricing agreements associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.

### [files](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/files/README.md)

* [upload](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/files/README.md#upload) - Upload a file and link it to the specified Moov account. 

The maximum file size is 20MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, 
and png. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/files/README.md#list) - List all the files associated with a particular Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/files/README.md#get) - Retrieve file details associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/files.read` scope.

### [industries](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/industries/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/industries/README.md#list) - Returns a list of industries relevant to merchant profile enrichment.  Results are ordered by industry name.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/),
you'll need to specify the `/profile-enrichment.read` scope.

### [institutions](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/institutions/README.md)

* [search_institutions](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/institutions/README.md#search_institutions) - Search for financial institutions by name or routing number.

This endpoint returns metadata about each matched institution, including basic identifying details (such as name, routing number, and address) and information about which payment services they support (e.g., ACH, RTP, and Wire).

This can be used to validate a financial institution before initiating payment activity, or to check which payment rails are available for a given routing number.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
you'll need to specify the `/institutions.read` scope.
* [search](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/institutions/README.md#search) - Search for institutions by either their name or routing number.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/fed.read` scope.

### [issuing_transactions](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md)

* [list_authorizations](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md#list_authorizations) - List issued card authorizations associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get_authorization](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md#get_authorization) - Retrieves details of an authorization associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [list_authorization_events](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md#list_authorization_events) - List card network and Moov platform events that affect the authorization and its hold on a wallet balance.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md#list) - List issued card transactions associated with a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/issuingtransactions/README.md#get) - Retrieves details of an issued card transaction associated with a specific Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/issued-cards.read` scope.


### [onboarding](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/onboarding/README.md)

* [create_invite](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/onboarding/README.md#create_invite) - Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.
* [list_invites](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/onboarding/README.md#list_invites) - List all the onboarding invites created by the caller's account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.
* [get_invite](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/onboarding/README.md#get_invite) - Retrieve details about an onboarding invite.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.
* [revoke_invite](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/onboarding/README.md#revoke_invite) - Revoke an onboarding invite, rendering the invitation link unusable.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.

### [payment_links](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#create) - Create a payment link that allows an end user to make a payment on Moov's hosted payment link page.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#list) - List all the payment links created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#get) - Retrieve a payment link by code.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#update) - Update a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [disable](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#disable) - Disable a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_qr_code](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentlinks/README.md#get_qr_code) - Retrieve the payment link encoded in a QR code. 

Use the `Accept` header to specify the format of the response. Supported formats are `application/json` and `image/png`.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

### [payment_methods](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentmethods/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentmethods/README.md#list) - Retrieve a list of payment methods associated with a Moov account. Read our [payment methods 
guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/paymentmethods/README.md#get) - Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

### [ping](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/ping/README.md)

* [ping](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/ping/README.md#ping) - A simple endpoint to check auth.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/ping.read` scope.

### [receipts](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/receipts/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/receipts/README.md#create) -  Create receipts for transfers and scheduled transfers.

 To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
 you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/receipts/README.md#list) - List receipts by transferID, scheduleID, or occurrenceID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### [representatives](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md#create) - Moov accounts associated with businesses require information regarding individuals who represent the business. 
You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md#list) - A Moov account may have multiple representatives depending on the associated business's ownership and management structure. 
You can use this method to list all the representatives for a given Moov account. 
Note that Moov accounts associated with an individual do not have representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.
* [delete](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md#delete) - Deletes a business representative associated with a Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md#get) - Retrieve a specific representative associated with a given Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/representatives/README.md#update) - If a representative's information has changed you can patch the information associated with a specific representative ID. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

When **can** profile data be updated:

- For unverified representatives, all profile data can be edited.
- During the verification process, missing or incomplete profile data can be edited.
- Verified representatives can only add missing profile data.

When **can't** profile data be updated:

- Verified representatives cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.

### [scheduling](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#create) - Describes the schedule to create or modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#list) - Describes a list of schedules associated with an account. Append the `hydrate=accounts` query parameter to include partial account details in the response.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#update) - Describes the schedule to modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#get) - Describes a schedule associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [cancel](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#cancel) - Describes the schedule to cancel.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_occurrance](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/scheduling/README.md#get_occurrance) - Gets a specific occurrence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### [support](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md)

* [create_ticket](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md#create_ticket) - Create a support ticket for a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/tickets.write` scope.

If you're creating the ticket on behalf of another account, then you'll need to
specify the `/accounts/{partnerAccountID}/tickets.write` and `/accounts/{accountID}/profile.read` scopes.
* [list_tickets](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md#list_tickets) - List all the support tickets created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/tickets.read` scope.

If you're listing another account's tickets, then you'll need to
specify the `/accounts/{partnerAccountID}/tickets.read` and `/accounts/{accountID}/profile.read` scopes.
* [get_ticket](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md#get_ticket) - Retrieve a support ticket by ID.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/tickets.read` scope.

If you're retrieving another account's ticket, then you'll need to
specify the `/accounts/{partnerAccountID}/tickets.read` and `/accounts/{accountID}/profile.read` scopes.
* [update_ticket](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md#update_ticket) - Updates a support ticket.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/tickets.write` scope.

If you're updating the ticket on behalf of another account, then you'll need to
specify the `/accounts/{partnerAccountID}/tickets.write` and `/accounts/{accountID}/profile.read` scopes.
* [list_ticket_messages](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/support/README.md#list_ticket_messages) - List all the messages for a support ticket.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/tickets.read` scope.

If you're listing another account's messages, then you'll need to
specify the `/accounts/{partnerAccountID}/tickets.read` and `/accounts/{accountID}/profile.read` scopes.

### [sweeps](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md)

* [create_config](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#create_config) - Create a sweep config for a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.
* [list_configs](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#list_configs) - List sweep configs associated with an account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get_config](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#get_config) - Get a sweep config associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [update_config](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#update_config) - Update settings on a sweep config.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#list) - List sweeps associated with a wallet.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/sweeps/README.md#get) - Get details on a specific sweep.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### [terminal_applications](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md)

* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md#create) - Create a new terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md#list) - List all the terminal applications for a Moov Account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md#get) - Fetch a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.read` scope.
* [delete](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md#delete) - Delete a specific terminal application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.
* [create_version](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/terminalapplications/README.md#create_version) - Register a new version of a terminal application. For Android applications, this is used to register a new version code of the application.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/terminal-applications.write` scope.

### [transfers](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md)

* [generate_options](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#generate_options) - Generate available payment method options for one or multiple transfer participants depending on the accountID or paymentMethodID you 
supply in the request body.

The accountID in the route should the partner's accountID.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [create](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#create) - Move money by providing the source, destination, and amount in the request body.

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#list) - List all the transfers associated with a particular Moov account. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

When you run this request, you retrieve 200 transfers at a time. You can advance past a results set of 200 transfers by using the `skip` parameter (for example, 
if you set `skip`= 10, you will see a results set of 200 transfers after the first 10). If you are searching a high volume of transfers, the request will likely 
process very slowly. To achieve faster performance, restrict the data as much as you can by using the `StartDateTime` and `EndDateTime` parameters for a limited 
period of time. You can run multiple requests in smaller time window increments until you've retrieved all the transfers you need.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#get) - Retrieve full transfer details for an individual transfer of a particular Moov account. 

Payment rail-specific details are included in the source and destination. Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) 
to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#update) - Update the metadata contained on a transfer. 

Read our [transfers overview guide](https://docs.moov.io/guides/money-movement/overview/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [create_cancellation](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#create_cancellation) -   Initiate a cancellation for a card, ACH, or queued transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_cancellation](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#get_cancellation) -   Get details of a cancellation for a transfer.
  
  To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
  to specify the `/accounts/{accountID}/transfers.read` scope.
* [initiate_refund](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#initiate_refund) - Initiate a refund for a card transfer.

**Use the [Cancel or refund a card transfer](https://docs.moov.io/api/money-movement/refunds/cancel/) endpoint for more comprehensive cancel and refund options.**    
See the [reversals](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) guide for more information. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list_refunds](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#list_refunds) - Get a list of refunds for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get_refund](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#get_refund) - Get details of a refund for a card transfer.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [create_reversal](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/transfers/README.md#create_reversal) - Reverses a card transfer by initiating a cancellation or refund depending on the transaction status. 
Read our [reversals guide](https://docs.moov.io/guides/money-movement/accept-payments/card-acceptance/reversals/) 
to learn more.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/transfers.write` scope.

### [underwriting](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/underwriting/README.md)

* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/underwriting/README.md#get) - Retrieve underwriting associated with a given Moov account. 

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more. 

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.read` scope.
* [save](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/underwriting/README.md#save) - Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.
* [upsert](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/underwriting/README.md#upsert) - Create or update the account's underwriting.

Read our [underwriting guide](https://docs.moov.io/guides/accounts/requirements/underwriting/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/profile.write` scope.

### [wallet_transactions](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallettransactions/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallettransactions/README.md#list) - List all the transactions associated with a particular Moov wallet. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallettransactions/README.md#get) - Get details on a specific wallet transaction. 

Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

### [wallets](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallets/README.md)

* [list](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallets/README.md#list) - List the wallets associated with a Moov account. 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.
* [get](https://github.com/moovfinancial/moov-python/blob/master/docs/sdks/wallets/README.md#get) - Get information on a specific wallet (e.g., the available balance). 

Read our [Moov wallets guide](https://docs.moov.io/guides/sources/wallets/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.disputes.upload_evidence_file(account_id="c09fd2f8-75fb-4ed9-be03-f8565d3ddc67", dispute_id="ad27f84d-00b1-4db0-8cf5-be001d71251d", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, evidence_type=components.EvidenceType.CANCELATION_POLICY)

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import BackoffStrategy, RetryConfig, parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
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
    }, mode=components.Mode.PRODUCTION,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import BackoffStrategy, RetryConfig, parse_datetime


with Moov(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`MoovError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/mooverror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/moovfinancial/moov-python/blob/master/#error-classes). |

### Example
```python
from moovio_sdk import Moov
from moovio_sdk.models import components, errors
from moovio_sdk.utils import parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:
    res = None
    try:

        res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
            business=components.CreateBusinessProfile(
                legal_business_name="Whole Body Fitness LLC",
            ),
        ), metadata={
            "optional": "metadata",
        }, terms_of_service={
            "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
            "accepted_ip": "172.217.2.46",
            "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
            "accepted_domain": "https://esteemed-velocity.net",
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


    except errors.MoovError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.GenericError):
            print(e.data.error)  # str
```

### Error Classes
**Primary error:**
* [`MoovError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/mooverror.py): The base class for HTTP error responses.

<details><summary>Less common errors (42)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`MoovError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/mooverror.py)**:
* [`GenericError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/genericerror.py): Applicable to 62 of 143 methods.*
* [`BrandValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/brandvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 3 of 143 methods.*
* [`ScheduleValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/schedulevalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 2 of 143 methods.*
* [`TerminalApplicationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/terminalapplicationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 2 of 143 methods.*
* [`Transfer`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/transfer.py): Details of a Transfer. Status code `409`. Applicable to 1 of 143 methods.*
* [`CardAcquiringRefund`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/cardacquiringrefund.py): Details of a card refund. Status code `409`. Applicable to 1 of 143 methods.*
* [`CreateAccountError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/createaccounterror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`PatchAccountError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/patchaccounterror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`AssignCountriesError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/assigncountrieserror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`LinkApplePayError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/linkapplepayerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`BankAccountValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/bankaccountvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`MicroDepositValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/microdepositvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`AddCapabilitiesError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/addcapabilitieserror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`LinkCardError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/linkcarderror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpdateCardError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/updatecarderror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`FileUploadValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/fileuploadvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`FeePlanAgreementError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/feeplanagreementerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`FileValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/filevalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`CreatePaymentLinkError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/createpaymentlinkerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpdatePaymentLinkError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/updatepaymentlinkerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`RepresentativeValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/representativevalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`CreateSweepConfigError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/createsweepconfigerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`PatchSweepConfigError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/patchsweepconfigerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`AccountTerminalApplicationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/accountterminalapplicationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`CreateTicketError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/createticketerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpdateTicketError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/updateticketerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`TransferOptionsValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/transferoptionsvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`TransferValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/transfervalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`RefundValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/refundvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`ReversalValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/reversalvalidationerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpsertUnderwritingError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/upsertunderwritingerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpdateUnderwritingError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/updateunderwritingerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`RequestCardError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/requestcarderror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`UpdateIssuedCardError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/updateissuedcarderror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`RevokeTokenRequestError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/revoketokenrequesterror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`AuthTokenRequestError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/authtokenrequesterror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`OnboardingInviteError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/onboardinginviteerror.py): The request was well-formed, but the contents failed validation. Check the request for missing or invalid fields. Status code `422`. Applicable to 1 of 143 methods.*
* [`ResponseValidationError`](https://github.com/moovfinancial/moov-python/blob/master/./src/moovio_sdk/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/moovfinancial/moov-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    server_url="https://api.moov.io",
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from moovio_sdk import Moov
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Moov(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from moovio_sdk import Moov
from moovio_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Moov(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Moov` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from moovio_sdk import Moov
from moovio_sdk.models import components
def main():

    with Moov(
        x_moov_version="v2024.01.00",
        security=components.Security(
            username="",
            password="",
        ),
    ) as moov:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Moov(
        x_moov_version="v2024.01.00",
        security=components.Security(
            username="",
            password="",
        ),
    ) as moov:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from moovio_sdk import Moov
import logging

logging.basicConfig(level=logging.DEBUG)
s = Moov(debug_logger=logging.getLogger("moovio_sdk"))
```

You can also enable a default debug logger by setting an environment variable `MOOV_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=moovio-sdk&utm_campaign=python)
