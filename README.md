# moov

Developer-friendly & type-safe Python SDK specifically catered to leverage *moov* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=moov&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/moov/moov). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Moov API: Moov is a platform that enables developers to integrate all aspects of money movement with ease and speed. The Moov API makes it simple for platforms to send, receive, and store money. Our API is based upon REST principles, returns JSON responses, and uses standard HTTP response codes. To learn more about how Moov works at a high level, read our [concepts](https://docs.moov.io/guides/get-started/glossary/) guide.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [File uploads](#file-uploads)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
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
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from moov import Moov
import os

async def main():
    s = Moov(
        gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
    )
    res = await s.signup.self_signup_async(request={
        "email": "amanda@classbooker.dev",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [access_token](docs/sdks/accesstoken/README.md)

* [create_o_auth2_token](docs/sdks/accesstoken/README.md#create_o_auth2_token) - Create access token
* [revoke_o_auth2_token](docs/sdks/accesstoken/README.md#revoke_o_auth2_token) - Revoke access token

### [accounts](docs/sdks/accounts/README.md)

* [list_accounts](docs/sdks/accounts/README.md#list_accounts) - List accounts
* [create_account](docs/sdks/accounts/README.md#create_account) - Create account
* [get_account](docs/sdks/accounts/README.md#get_account) - Get account
* [patch_account](docs/sdks/accounts/README.md#patch_account) - Patch account
* [disconnect_account](docs/sdks/accounts/README.md#disconnect_account) - Disconnect account
* [get_terms_of_service_token](docs/sdks/accounts/README.md#get_terms_of_service_token) - Get terms of service token
* [get_account_countries](docs/sdks/accounts/README.md#get_account_countries) - Get account countries
* [assign_account_countries](docs/sdks/accounts/README.md#assign_account_countries) - Assign Account Countries

### [analytics](docs/sdks/analytics/README.md)

* [analytics_transfer_sum](docs/sdks/analytics/README.md#analytics_transfer_sum) - Sum all transfers across intervals
* [analytics_transfer_largest](docs/sdks/analytics/README.md#analytics_transfer_largest) - Return the largest number of transfers
* [analytics_transfer_smallest](docs/sdks/analytics/README.md#analytics_transfer_smallest) - Return the smallest number of transfers
* [analytics_transfer_statuses](docs/sdks/analytics/README.md#analytics_transfer_statuses) - Count the transfer statuses
* [analytics_accounts_created](docs/sdks/analytics/README.md#analytics_accounts_created) - Count the number of profiles created by an individual or business

### [application](docs/sdks/applicationsdk/README.md)

* [enable_application](docs/sdks/applicationsdk/README.md#enable_application) - Enable this account as a application provider
* [list_applications](docs/sdks/applicationsdk/README.md#list_applications) - List applications
* [update_application](docs/sdks/applicationsdk/README.md#update_application) - Update an application
* [disable_application](docs/sdks/applicationsdk/README.md#disable_application) - Disables an application
* [list_application_keys](docs/sdks/applicationsdk/README.md#list_application_keys) - List keys for an application
* [create_application_keys](docs/sdks/applicationsdk/README.md#create_application_keys) - Create a new application key
* [disable_application_key](docs/sdks/applicationsdk/README.md#disable_application_key) - Disables an application key
* [update_application_key](docs/sdks/applicationsdk/README.md#update_application_key) - Updates an application key

### [avatars](docs/sdks/avatars/README.md)

* [get_avatar](docs/sdks/avatars/README.md#get_avatar) - Get avatar

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [bank_account](docs/sdks/bankaccounts/README.md#bank_account) - Bank account
* [list_bank_accounts](docs/sdks/bankaccounts/README.md#list_bank_accounts) - List bank accounts
* [get_bank](docs/sdks/bankaccounts/README.md#get_bank) - Get bank account
* [delete_bank](docs/sdks/bankaccounts/README.md#delete_bank) - Delete bank account
* [initiate_micro_deposits](docs/sdks/bankaccounts/README.md#initiate_micro_deposits) - Initiate micro-deposits
* [complete_micro_deposits](docs/sdks/bankaccounts/README.md#complete_micro_deposits) - Complete micro-deposits
* [get_bank_account_verification](docs/sdks/bankaccounts/README.md#get_bank_account_verification) - Check instant verification status
* [initiate_bank_account_verification](docs/sdks/bankaccounts/README.md#initiate_bank_account_verification) - Send instant verification credit
* [complete_bank_account_verification](docs/sdks/bankaccounts/README.md#complete_bank_account_verification) - Complete instant verification

### [branding](docs/sdks/brandingsdk/README.md)

* [get_branding](docs/sdks/brandingsdk/README.md#get_branding) - Get account branding
* [create_branding](docs/sdks/brandingsdk/README.md#create_branding) - Create a brand
* [update_branding](docs/sdks/brandingsdk/README.md#update_branding) - Update branding

### [capabilities](docs/sdks/capabilities/README.md)

* [get_capability](docs/sdks/capabilities/README.md#get_capability) - Get capability for account
* [disable_capability](docs/sdks/capabilities/README.md#disable_capability) - Disable a capability for an account.
* [list_capabilities](docs/sdks/capabilities/README.md#list_capabilities) - List capabilities for account
* [add_capabilities](docs/sdks/capabilities/README.md#add_capabilities) - Request capabilities

### [card_issuing](docs/sdks/cardissuing/README.md)

* [request_card](docs/sdks/cardissuing/README.md#request_card) - Request card
* [list_issued_cards](docs/sdks/cardissuing/README.md#list_issued_cards) - List issued cards
* [get_issued_card](docs/sdks/cardissuing/README.md#get_issued_card) - Get issued card
* [update_issued_card](docs/sdks/cardissuing/README.md#update_issued_card) - Update issued card
* [get_full_issued_card](docs/sdks/cardissuing/README.md#get_full_issued_card) - Get full card details

### [cards](docs/sdks/cards/README.md)

* [card](docs/sdks/cards/README.md#card) - Link card
* [list_cards](docs/sdks/cards/README.md#list_cards) - List cards
* [get_card](docs/sdks/cards/README.md#get_card) - Get card
* [update_card](docs/sdks/cards/README.md#update_card) - Update card
* [delete_card](docs/sdks/cards/README.md#delete_card) - Disable card
* [register_apple_pay_merchant_domains](docs/sdks/cards/README.md#register_apple_pay_merchant_domains) - Register Apple Pay domains
* [update_apple_pay_merchant_domains](docs/sdks/cards/README.md#update_apple_pay_merchant_domains) - Update Apple Pay domains
* [get_apple_pay_merchant_domains](docs/sdks/cards/README.md#get_apple_pay_merchant_domains) - Get Apple Pay domains
* [create_apple_pay_session](docs/sdks/cards/README.md#create_apple_pay_session) - Create Apple Pay session
* [link_apple_pay_token](docs/sdks/cards/README.md#link_apple_pay_token) - Link Apple Pay token

### [checkout](docs/sdks/checkoutsdk/README.md)

* [create_checkout](docs/sdks/checkoutsdk/README.md#create_checkout) - Create checkout
* [list_checkouts](docs/sdks/checkoutsdk/README.md#list_checkouts) - List checkouts
* [get_checkout](docs/sdks/checkoutsdk/README.md#get_checkout) - Get checkout
* [update_checkout](docs/sdks/checkoutsdk/README.md#update_checkout) - Update checkout
* [disable_checkout](docs/sdks/checkoutsdk/README.md#disable_checkout) - Disable checkout
* [get_checkout_qr_code](docs/sdks/checkoutsdk/README.md#get_checkout_qr_code) - Get QR code for checkout

### [connections](docs/sdks/connections/README.md)

* [list_connections](docs/sdks/connections/README.md#list_connections) - List connections

### [devices](docs/sdks/devices/README.md)

* [refresh_session](docs/sdks/devices/README.md#refresh_session) - Refresh Cookie
* [list_devices_for_user](docs/sdks/devices/README.md#list_devices_for_user) - Devices for a user
* [get_device_for_user](docs/sdks/devices/README.md#get_device_for_user) - Specific device
* [disable_device_for_user](docs/sdks/devices/README.md#disable_device_for_user) - Disable device

### [disputes](docs/sdks/disputes/README.md)

* [list_disputes](docs/sdks/disputes/README.md#list_disputes) - List of all disputes
* [get_dispute](docs/sdks/disputes/README.md#get_dispute) - Dispute by ID
* [accept_dispute](docs/sdks/disputes/README.md#accept_dispute) - Accept dispute
* [list_dispute_evidence](docs/sdks/disputes/README.md#list_dispute_evidence) - List dispute evidence by dispute ID
* [submit_evidence](docs/sdks/disputes/README.md#submit_evidence) - Submit dispute evidence
* [upload_evidence_file](docs/sdks/disputes/README.md#upload_evidence_file) - Upload evidence file
* [upload_evidence_text](docs/sdks/disputes/README.md#upload_evidence_text) - Upload evidence text
* [get_dispute_evidence](docs/sdks/disputes/README.md#get_dispute_evidence) - Dispute evidence by ID
* [delete_evidence](docs/sdks/disputes/README.md#delete_evidence) - Delete dispute evidence by dispute ID and evidence ID
* [update_dispute_evidence](docs/sdks/disputes/README.md#update_dispute_evidence) - Update dispute evidence by dispute ID and evidence ID
* [get_dispute_evidence_data](docs/sdks/disputes/README.md#get_dispute_evidence_data) - Download dispute evidence data by evidence ID

### [email_password](docs/sdks/emailpassword/README.md)

* [signin_with_password](docs/sdks/emailpassword/README.md#signin_with_password) - Signin a user with email & password
* [setup_password](docs/sdks/emailpassword/README.md#setup_password) - Register user with password
* [change_password](docs/sdks/emailpassword/README.md#change_password) - Change password
* [recover_password](docs/sdks/emailpassword/README.md#recover_password) - Recover password
* [reset_password](docs/sdks/emailpassword/README.md#reset_password) - Set password for recovery

### [end_to_end_encryption](docs/sdks/endtoendencryption/README.md)

* [generate_end_to_end_key](docs/sdks/endtoendencryption/README.md#generate_end_to_end_key) - Generate public key
* [test_end_to_end_token](docs/sdks/endtoendencryption/README.md#test_end_to_end_token) - Test JWE

### [enriched_address](docs/sdks/enrichedaddress/README.md)

* [get_enrichment_address](docs/sdks/enrichedaddress/README.md#get_enrichment_address) - Get address suggestions

### [enriched_profile](docs/sdks/enrichedprofile/README.md)

* [get_enrichment_profile](docs/sdks/enrichedprofile/README.md#get_enrichment_profile) - Get enriched profile

### [files](docs/sdks/files/README.md)

* [upload_file](docs/sdks/files/README.md#upload_file) - Upload file
* [list_files](docs/sdks/files/README.md#list_files) - List files
* [get_file_details](docs/sdks/files/README.md#get_file_details) - Get file details

### [industries](docs/sdks/industriessdk/README.md)

* [list_industries](docs/sdks/industriessdk/README.md#list_industries) - List all industries

### [institutions](docs/sdks/institutions/README.md)

* [search_institutions](docs/sdks/institutions/README.md#search_institutions) - Search institutions

### [invites](docs/sdks/invites/README.md)

* [list_invites](docs/sdks/invites/README.md#list_invites) - List invites
* [send_invite](docs/sdks/invites/README.md#send_invite) - Send invite
* [disable_invite](docs/sdks/invites/README.md#disable_invite) - Disable invite
* [accept_invite](docs/sdks/invites/README.md#accept_invite) - Accept invite
* [decline_invite](docs/sdks/invites/README.md#decline_invite) - Decline invite
* [resend_invite](docs/sdks/invites/README.md#resend_invite) - Resend invite
* [confirm_invite](docs/sdks/invites/README.md#confirm_invite) - Confirm invite

### [issuing_transactions](docs/sdks/issuingtransactions/README.md)

* [list_account_issued_card_authorizations](docs/sdks/issuingtransactions/README.md#list_account_issued_card_authorizations) - Get account authorizations
* [get_account_issued_card_authorization](docs/sdks/issuingtransactions/README.md#get_account_issued_card_authorization) - Retrieve an authorization
* [list_authorization_events](docs/sdks/issuingtransactions/README.md#list_authorization_events) - Get authorization events
* [list_account_issued_card_transactions](docs/sdks/issuingtransactions/README.md#list_account_issued_card_transactions) - Get account card transactions
* [get_account_issued_card_transaction](docs/sdks/issuingtransactions/README.md#get_account_issued_card_transaction) - Retrieve an issued card transaction


### [moov_internal](docs/sdks/moovinternal/README.md)

* [redeem_onboarding_invite](docs/sdks/moovinternal/README.md#redeem_onboarding_invite) - Redeem onboarding invite
* [get_network_i_ds](docs/sdks/moovinternal/README.md#get_network_i_ds) - Get network IDs of an account
* [list_fee_plans](docs/sdks/moovinternal/README.md#list_fee_plans) - List fee plans
* [create_fee_plan_agreement](docs/sdks/moovinternal/README.md#create_fee_plan_agreement) - Create fee plan agreement
* [list_fee_plan_agreements](docs/sdks/moovinternal/README.md#list_fee_plan_agreements) - List fee plan agreements
* [list_partner_pricing](docs/sdks/moovinternal/README.md#list_partner_pricing) - List partner pricing plans
* [list_partner_pricing_agreements](docs/sdks/moovinternal/README.md#list_partner_pricing_agreements) - List partner pricing agreements
* [create_checkout](docs/sdks/moovinternal/README.md#create_checkout) - Create checkout
* [list_checkouts](docs/sdks/moovinternal/README.md#list_checkouts) - List checkouts
* [get_checkout](docs/sdks/moovinternal/README.md#get_checkout) - Get checkout
* [update_checkout](docs/sdks/moovinternal/README.md#update_checkout) - Update checkout
* [disable_checkout](docs/sdks/moovinternal/README.md#disable_checkout) - Disable checkout
* [get_checkout_qr_code](docs/sdks/moovinternal/README.md#get_checkout_qr_code) - Get QR code for checkout

### [onboarding](docs/sdks/onboarding/README.md)

* [create_onboarding_invite](docs/sdks/onboarding/README.md#create_onboarding_invite) - Create onboarding invite
* [list_onboarding_invites](docs/sdks/onboarding/README.md#list_onboarding_invites) - List onboarding invites
* [get_onboarding_invite_details](docs/sdks/onboarding/README.md#get_onboarding_invite_details) - Get onboarding invite
* [revoke_onboarding_invite](docs/sdks/onboarding/README.md#revoke_onboarding_invite) - Revoke onboarding invite

### [open_id_connect](docs/sdks/openidconnect/README.md)

* [oidc_authentication](docs/sdks/openidconnect/README.md#oidc_authentication) - Authenticate with OIDC Provider
* [oidc_callback](docs/sdks/openidconnect/README.md#oidc_callback) - Callback from OIDC Provider

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [get_payment_methods](docs/sdks/paymentmethods/README.md#get_payment_methods) - List payment methods
* [get_payment_method](docs/sdks/paymentmethods/README.md#get_payment_method) - Get payment method

### [ping](docs/sdks/ping/README.md)

* [ping](docs/sdks/ping/README.md#ping) - Test Authentication

### [representatives](docs/sdks/representatives/README.md)

* [create_representative](docs/sdks/representatives/README.md#create_representative) - Create representative
* [list_representatives](docs/sdks/representatives/README.md#list_representatives) - List representatives
* [get_representative](docs/sdks/representatives/README.md#get_representative) - Get representative
* [delete_representative](docs/sdks/representatives/README.md#delete_representative) - Delete a representative
* [patch_representative](docs/sdks/representatives/README.md#patch_representative) - Patch representative

### [roles](docs/sdks/roles/README.md)

* [list_roles](docs/sdks/roles/README.md#list_roles) - List roles
* [create_role](docs/sdks/roles/README.md#create_role) - Create role
* [get_role](docs/sdks/roles/README.md#get_role) - Get Role
* [update_role](docs/sdks/roles/README.md#update_role) - Update role
* [disable_role](docs/sdks/roles/README.md#disable_role) - Delete role
* [members_list](docs/sdks/roles/README.md#members_list) - List members

### [schedules](docs/sdks/schedules/README.md)

* [list_schedules](docs/sdks/schedules/README.md#list_schedules) - List schedules
* [create_schedule](docs/sdks/schedules/README.md#create_schedule) - Create schedule
* [get_schedules](docs/sdks/schedules/README.md#get_schedules) - Get schedule
* [update_schedule](docs/sdks/schedules/README.md#update_schedule) - Update schedule
* [cancel_schedule](docs/sdks/schedules/README.md#cancel_schedule) - Cancel schedule
* [get_scheduled_occurrence](docs/sdks/schedules/README.md#get_scheduled_occurrence) - Get occurrence

### [session](docs/sdks/sessionsdk/README.md)

* [get_session](docs/sdks/sessionsdk/README.md#get_session) - Get current session information
* [disable_session](docs/sdks/sessionsdk/README.md#disable_session) - Delete this session and logout

### [signup](docs/sdks/signupsdk/README.md)

* [self_signup](docs/sdks/signupsdk/README.md#self_signup) - Self signup

### [sweeps](docs/sdks/sweeps/README.md)

* [create_sweep_config](docs/sdks/sweeps/README.md#create_sweep_config) - Create a sweep config
* [list_sweep_configs](docs/sdks/sweeps/README.md#list_sweep_configs) - List sweep configs
* [patch_sweep_config](docs/sdks/sweeps/README.md#patch_sweep_config) - Patch a sweep config
* [get_sweep_config](docs/sdks/sweeps/README.md#get_sweep_config) - Get a sweep config
* [list_sweeps](docs/sdks/sweeps/README.md#list_sweeps) - List sweeps
* [get_sweep](docs/sdks/sweeps/README.md#get_sweep) - Get a sweep

### [transfers](docs/sdks/transfers/README.md)

* [create_transfer](docs/sdks/transfers/README.md#create_transfer) - Create a transfer
* [get_transfer](docs/sdks/transfers/README.md#get_transfer) - Get a transfer
* [patch_transfer](docs/sdks/transfers/README.md#patch_transfer) - Patch transfer metadata
* [create_transfer_options](docs/sdks/transfers/README.md#create_transfer_options) - Generate transfer options
* [refund_transfer](docs/sdks/transfers/README.md#refund_transfer) - Refund a transfer
* [get_refunds](docs/sdks/transfers/README.md#get_refunds) - Get a list of refunds for a card transfer
* [get_refund](docs/sdks/transfers/README.md#get_refund) - Get refund details
* [reverse_transfer](docs/sdks/transfers/README.md#reverse_transfer) - Cancel or refund a card transfer
* [list_transfers_for_account](docs/sdks/transfers/README.md#list_transfers_for_account) - List transfers for account
* [get_transfer_for_account](docs/sdks/transfers/README.md#get_transfer_for_account) - Retrieve a transfer for an account

### [underwriting](docs/sdks/underwritingsdk/README.md)

* [get_underwriting](docs/sdks/underwritingsdk/README.md#get_underwriting) - Retrieve underwriting details
* [update_underwriting](docs/sdks/underwritingsdk/README.md#update_underwriting) - Update underwriting details

### [users](docs/sdks/users/README.md)

* [get_user](docs/sdks/users/README.md#get_user) - Get user
* [update_user](docs/sdks/users/README.md#update_user) - Update User
* [get_user_accounts](docs/sdks/users/README.md#get_user_accounts) - Get accounts user has access to
* [get_user_invites](docs/sdks/users/README.md#get_user_invites) - Get pending invites sent for user

### [verification](docs/sdks/verificationsdk/README.md)

* [is_device_verified](docs/sdks/verificationsdk/README.md#is_device_verified) - Device verification
* [check_verification_code_from_email](docs/sdks/verificationsdk/README.md#check_verification_code_from_email) - Device verification
* [send_verification_code_via_email](docs/sdks/verificationsdk/README.md#send_verification_code_via_email) - Send code via email

### [wallet_transactions](docs/sdks/wallettransactions/README.md)

* [list_wallet_transactions](docs/sdks/wallettransactions/README.md#list_wallet_transactions) - List wallet transactions
* [get_wallet_transaction](docs/sdks/wallettransactions/README.md#get_wallet_transaction) - Get wallet transaction

### [wallets](docs/sdks/wallets/README.md)

* [list_wallets_for_account](docs/sdks/wallets/README.md#list_wallets_for_account) - List wallets
* [get_wallet_for_account](docs/sdks/wallets/README.md#get_wallet_for_account) - Get wallet

### [webhooks](docs/sdks/webhooks/README.md)

* [create_webhook](docs/sdks/webhooks/README.md#create_webhook) - Create webhook
* [list_webhooks](docs/sdks/webhooks/README.md#list_webhooks) - List webhooks
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Get webhook
* [update_webhook](docs/sdks/webhooks/README.md#update_webhook) - Update webhook
* [delete_hook](docs/sdks/webhooks/README.md#delete_hook) - Delete webhook
* [ping_webhook](docs/sdks/webhooks/README.md#ping_webhook) - Send ping
* [get_webhook_secret](docs/sdks/webhooks/README.md#get_webhook_secret) - Get webhook secret
* [list_event_types](docs/sdks/webhooks/README.md#list_event_types) - List event types

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
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.disputes.upload_evidence_file(dispute_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", evidence_file={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
    "evidence_type": moov.EvidenceType.CUSTOMER_COMMUNICATION,
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from moov import Moov
from moov.utils import BackoffStrategy, RetryConfig
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from moov import Moov
from moov.utils import BackoffStrategy, RetryConfig
import os

s = Moov(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_o_auth2_token_async` method may raise the following exceptions:

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.AccessTokenErrorResponse | 400                             | application/json                |
| models.SDKError                 | 4XX, 5XX                        | \*/\*                           |

### Example

```python
from .clientcredentialsgranttoaccesstokenerrorresponse import ClientCredentialsGrantToAccessTokenErrorResponseData
import moov
from moov import Moov, models
import os

s = Moov()

res = None
try:
    res = s.access_token.create_o_auth2_token(security=moov.CreateOAuth2TokenSecurity(
        username=os.getenv("MOOV_USERNAME", ""),
        password=os.getenv("MOOV_PASSWORD", ""),
    ), request={
        "grant_type": moov.GrantType.REFRESH_TOKEN,
        "client_id": "5clTR_MdVrrkgxw2",
        "client_secret": "dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-",
        "scope": "/accounts.write",
        "refresh_token": "i1qxz68gu50zp4i8ceyxqogmq7y0yienm52351c6...",
    })

    if res is not None:
        # handle response
        pass

except models.AccessTokenErrorResponse as e:
    if isinstance(e.data, ClientCredentialsGrantToAccessTokenErrorResponseData):
        # handle custom error data
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.moov.io` | None |

#### Example

```python
from moov import Moov
import os

s = Moov(
    server_idx=0,
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from moov import Moov
import os

s = Moov(
    server_url="https://api.moov.io",
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from moov import Moov
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Moov(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from moov import Moov
from moov.httpclient import AsyncHttpClient
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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                 | Type                 | Scheme               | Environment Variable |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `gateway_auth`       | http                 | HTTP Bearer          | `MOOV_GATEWAY_AUTH`  |

To authenticate with the API the `gateway_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import moov
from moov import Moov
import os

s = Moov()

res = s.access_token.create_o_auth2_token(security=moov.CreateOAuth2TokenSecurity(
    username=os.getenv("MOOV_USERNAME", ""),
    password=os.getenv("MOOV_PASSWORD", ""),
), request={
    "grant_type": moov.GrantType.REFRESH_TOKEN,
    "client_id": "5clTR_MdVrrkgxw2",
    "client_secret": "dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-",
    "scope": "/accounts.write",
    "refresh_token": "i1qxz68gu50zp4i8ceyxqogmq7y0yienm52351c6...",
})

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from moov import Moov
import logging

logging.basicConfig(level=logging.DEBUG)
s = Moov(debug_logger=logging.getLogger("moov"))
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

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=moov&utm_campaign=python)
