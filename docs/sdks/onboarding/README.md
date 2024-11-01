# Onboarding
(*onboarding*)

## Overview

<b>Coming soon -</b> Invite organizations to onboard with Moov. Create an invitation containing a unique link that allows the recipient to provide data necessary to fulfill capability requirements, agree to pricing, and accept Moov's terms.

You can create and send an onboarding link directly from the Moov Dashboard. See our [documentation](https://docs.moov.io/guides/accounts/hosted-onboarding/) for details.


### Available Operations

* [create_onboarding_invite](#create_onboarding_invite) - Create onboarding invite
* [list_onboarding_invites](#list_onboarding_invites) - List onboarding invites
* [get_onboarding_invite_details](#get_onboarding_invite_details) - Get onboarding invite
* [revoke_onboarding_invite](#revoke_onboarding_invite) - Revoke onboarding invite

## create_onboarding_invite

Create an invitation containing a unique link that allows the recipient to onboard their organization with Moov.


### Example Usage

```python
import dateutil.parser
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.onboarding.create_onboarding_invite(request={
    "capabilities": [
        moov.CapabilityID.TRANSFERS,
    ],
    "fee_plan_codes": [
        "merchant-direct",
    ],
    "return_url": "https://mycompany.com/account",
    "terms_of_service_url": "https://mycompany.com/terms-of-service",
    "scopes": [
        moov.ApplicationScope.ACCOUNTS_READ,
    ],
    "prefill": {
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
            "accepted_date": dateutil.parser.isoparse("2023-06-13T19:13:18.810Z"),
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
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.OnboardingInviteRequest](../../models/onboardinginviterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateOnboardingInviteResponse](../../models/createonboardinginviteresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## list_onboarding_invites

List all the onboarding invites created by the caller's account.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.onboarding.list_onboarding_invites()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOnboardingInvitesResponse](../../models/listonboardinginvitesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_onboarding_invite_details

Retrieve details about an onboarding invite.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.onboarding.get_onboarding_invite_details(code="N1IA5eWYNh")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The unique code that identifies the onboarding invite.              | N1IA5eWYNh                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOnboardingInviteDetailsResponse](../../models/getonboardinginvitedetailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## revoke_onboarding_invite

Revoke an onboarding invite, rendering the invitation link unusable.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.onboarding.revoke_onboarding_invite(code="N1IA5eWYNh")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The unique code that identifies the onboarding invite.              | N1IA5eWYNh                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RevokeOnboardingInviteResponse](../../models/revokeonboardinginviteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |