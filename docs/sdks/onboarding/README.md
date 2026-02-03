# Onboarding

## Overview

### Available Operations

* [create_invite](#create_invite) - Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.
* [list_invites](#list_invites) - List all the onboarding invites created by the caller's account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.
* [get_invite](#get_invite) - Retrieve details about an onboarding invite.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.
* [revoke_invite](#revoke_invite) - Revoke an onboarding invite, rendering the invitation link unusable.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.

## create_invite

Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOnboardingInvite" method="post" path="/onboarding-invites" -->
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

    res = moov.onboarding.create_invite(scopes=[
        components.ApplicationScope.ACCOUNTS_READ,
    ], capabilities=[
        components.CapabilityID.TRANSFERS,
    ], fee_plan_codes=[
        "merchant-direct",
    ], grant_scopes=[
        components.ApplicationScope.TRANSFERS_WRITE,
    ], prefill=components.CreateAccount(
        account_type=components.AccountType.BUSINESS,
        profile=components.CreateProfile(
            business=components.CreateBusinessProfile(
                legal_business_name="Whole Body Fitness LLC",
            ),
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            | Example                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scopes`                                                                                                                                                                                                               | List[[components.ApplicationScope](../../models/components/applicationscope.md)]                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                     |   List of [scopes](https://docs.moov.io/api/authentication/scopes/) you request to use on this<br/>  account. These values are used to determine what can be done with the account onboarded.                          | [<br/>"accounts.read"<br/>]                                                                                                                                                                                            |
| `capabilities`                                                                                                                                                                                                         | List[[components.CapabilityID](../../models/components/capabilityid.md)]                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                     |   List of [capabilities](https://docs.moov.io/guides/accounts/capabilities/) you intend to request for this<br/>  account. These values are used to determine what information to collect from the user during onboarding. | [<br/>"transfers"<br/>]                                                                                                                                                                                                |
| `fee_plan_codes`                                                                                                                                                                                                       | List[*str*]                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                     | List of fee plan codes to assign the account created by the invitee.                                                                                                                                                   | [<br/>"merchant-direct"<br/>]                                                                                                                                                                                          |
| `return_url`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Optional URL to redirect the user to after they complete the onboarding process.                                                                                                                                       |                                                                                                                                                                                                                        |
| `terms_of_service_url`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Optional URL to your organization's terms of service.                                                                                                                                                                  |                                                                                                                                                                                                                        |
| `grant_scopes`                                                                                                                                                                                                         | List[[components.ApplicationScope](../../models/components/applicationscope.md)]                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     |   List of [scopes](https://docs.moov.io/api/authentication/scopes/) you grant to allow being used <br/>  by the new account on yourself. These values are used to determine what the account onboarded can do.         | [<br/>"transfers.write"<br/>]                                                                                                                                                                                          |
| `prefill`                                                                                                                                                                                                              | [Optional[components.CreateAccount]](../../models/components/createaccount.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                    | {<br/>"accountType": "business",<br/>"profile": {<br/>"business": {<br/>"legalBusinessName": "Whole Body Fitness LLC"<br/>}<br/>}<br/>}                                                                                |
| `retries`                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                    |                                                                                                                                                                                                                        |

### Response

**[operations.CreateOnboardingInviteResponse](../../models/operations/createonboardinginviteresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GenericError          | 400, 409                     | application/json             |
| errors.OnboardingInviteError | 422                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |

## list_invites

List all the onboarding invites created by the caller's account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOnboardingInvites" method="get" path="/onboarding-invites" -->
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

    res = moov.onboarding.list_invites()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListOnboardingInvitesRequest](../../models/operations/listonboardinginvitesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListOnboardingInvitesResponse](../../models/operations/listonboardinginvitesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_invite

Retrieve details about an onboarding invite.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOnboardingInvite" method="get" path="/onboarding-invites/{code}" -->
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

    res = moov.onboarding.get_invite(code="N1IA5eWYNh")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | N1IA5eWYNh                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetOnboardingInviteResponse](../../models/operations/getonboardinginviteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## revoke_invite

Revoke an onboarding invite, rendering the invitation link unusable.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeOnboardingInvite" method="delete" path="/onboarding-invites/{code}" -->
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

    res = moov.onboarding.revoke_invite(code="N1IA5eWYNh")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | N1IA5eWYNh                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.RevokeOnboardingInviteResponse](../../models/operations/revokeonboardinginviteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |