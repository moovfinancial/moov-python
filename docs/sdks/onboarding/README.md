# Onboarding
(*onboarding*)

## Overview

### Available Operations

* [create_onboarding_invite](#create_onboarding_invite) - Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.
* [list_onboarding_invites](#list_onboarding_invites) - List all the onboarding invites created by the caller's account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.
* [get_onboarding_invite](#get_onboarding_invite) - Retrieve details about an onboarding invite.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.
* [revoke_onboarding_invite](#revoke_onboarding_invite) - Revoke an onboarding invite, rendering the invitation link unusable.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.

## create_onboarding_invite

Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.onboarding.create_onboarding_invite(security=operations.CreateOnboardingInviteSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), scopes=[
        components.ApplicationScope.ACCOUNTS_READ,
    ], capabilities=[
        components.CapabilityID.TRANSFERS,
    ], fee_plan_codes=[
        "merchant-direct",
    ], prefill=components.CreateAccount(
        account_type=components.AccountType.BUSINESS,
        profile=components.CreateProfile(
            business={
                "legal_business_name": "Classbooker, LLC",
            },
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            | Example                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                             | [operations.CreateOnboardingInviteSecurity](../../models/operations/createonboardinginvitesecurity.md)                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                    |                                                                                                                                                                                                                        |
| `scopes`                                                                                                                                                                                                               | List[[components.ApplicationScope](../../models/components/applicationscope.md)]                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                     |   List of [scopes](https://docs.moov.io/api/authentication/scopes/) you request to use on this<br/>  account. These values are used to determine what can be done with the account onboarded.                          | [<br/>"accounts.read"<br/>]                                                                                                                                                                                            |
| `capabilities`                                                                                                                                                                                                         | List[[components.CapabilityID](../../models/components/capabilityid.md)]                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                     |   List of [capabilities](https://docs.moov.io/guides/accounts/capabilities/) you intend to request for this<br/>  account. These values are used to determine what information to collect from the user during onboarding. | [<br/>"transfers"<br/>]                                                                                                                                                                                                |
| `fee_plan_codes`                                                                                                                                                                                                       | List[*str*]                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                     | List of fee plan codes to assign the account created by the invitee.                                                                                                                                                   | [<br/>"merchant-direct"<br/>]                                                                                                                                                                                          |
| `x_moov_version`                                                                                                                                                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                     | Specify an API version.                                                                                                                                                                                                |                                                                                                                                                                                                                        |
| `return_url`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Optional URL to redirect the user to after they complete the onboarding process.                                                                                                                                       |                                                                                                                                                                                                                        |
| `terms_of_service_url`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Optional URL to your organization's terms of service.                                                                                                                                                                  |                                                                                                                                                                                                                        |
| `prefill`                                                                                                                                                                                                              | [Optional[components.CreateAccount]](../../models/components/createaccount.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                    | {<br/>"accountType": "business",<br/>"profile": {<br/>"business": {<br/>"legalBusinessName": "Whole Body Fitness LLC"<br/>}<br/>}<br/>}                                                                                |
| `retries`                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                    |                                                                                                                                                                                                                        |

### Response

**[components.OnboardingInvite](../../models/components/onboardinginvite.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.OnboardingInviteError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_onboarding_invites

List all the onboarding invites created by the caller's account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.onboarding.list_onboarding_invites(security=operations.ListOnboardingInvitesSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.ListOnboardingInvitesSecurity](../../models/operations/listonboardinginvitessecurity.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `x_moov_version`                                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                                 | :heavy_minus_sign:                                                                                   | Specify an API version.                                                                              |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[List[components.OnboardingInvite]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_onboarding_invite

Retrieve details about an onboarding invite.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.read` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.onboarding.get_onboarding_invite(security=operations.GetOnboardingInviteSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), code="N1IA5eWYNh")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetOnboardingInviteSecurity](../../models/operations/getonboardinginvitesecurity.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `code`                                                                                           | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              | N1IA5eWYNh                                                                                       |
| `x_moov_version`                                                                                 | [Optional[components.Versions]](../../models/components/versions.md)                             | :heavy_minus_sign:                                                                               | Specify an API version.                                                                          |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[components.OnboardingInvite](../../models/components/onboardinginvite.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## revoke_onboarding_invite

Revoke an onboarding invite, rendering the invitation link unusable.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts.write` scope.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    moov.onboarding.revoke_onboarding_invite(security=operations.RevokeOnboardingInviteSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), code="N1IA5eWYNh")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `security`                                                                                             | [operations.RevokeOnboardingInviteSecurity](../../models/operations/revokeonboardinginvitesecurity.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `code`                                                                                                 | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | N1IA5eWYNh                                                                                             |
| `x_moov_version`                                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                                   | :heavy_minus_sign:                                                                                     | Specify an API version.                                                                                |                                                                                                        |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |                                                                                                        |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |