# Onboarding
(*onboarding*)

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

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
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
    ], prefill=components.CreateAccount(
        account_type=components.AccountType.BUSINESS,
        profile=components.CreateProfile(
            individual={
                "name": {
                    "first_name": "Jordan",
                    "last_name": "Lee",
                    "middle_name": "Reese",
                    "suffix": "Jr",
                },
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
                "birth_date": {
                    "day": 9,
                    "month": 11,
                    "year": 1989,
                },
            },
            business={
                "legal_business_name": "Classbooker, LLC",
                "business_type": components.BusinessType.LLC,
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
                "email": "jordan.lee@classbooker.dev",
                "description": "Local fitness gym paying out instructors",
                "tax_id": {
                    "ein": {
                        "number": "12-3456789",
                    },
                },
                "industry_codes": {
                    "naics": "713940",
                    "sic": "7991",
                    "mcc": "7997",
                },
            },
        ),
        metadata={
            "optional": "metadata",
        },
        terms_of_service={
            "accepted_date": dateutil.parser.isoparse("2024-12-17T23:29:29.246Z"),
            "accepted_ip": "172.217.2.46",
            "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
            "accepted_domain": "https://odd-brace.biz/",
        },
        customer_support={
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
        },
        settings={
            "card_payment": {
                "statement_descriptor": "Whole Body Fitness",
            },
            "ach_payment": {
                "company_name": "WholeBodyFitness",
            },
        },
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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
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