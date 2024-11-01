# Representatives
(*representatives*)

## Overview

We think of a representative as an individual who can take major actions on behalf of a business. A representative can be the business owner, or anyone who owns 25% or more of the business. Some examples of representatives are the CEO, CFO, COO, or president. We require all business accounts to have valid information for at least one representative. Moov accounts must have verified business representatives before a business account can send funds, collect money from other accounts, or store funds in a wallet. To learn more, read our guide on [business representatives](https://docs.moov.io/guides/accounts/business-representatives/).


### Available Operations

* [create_representative](#create_representative) - Create representative
* [list_representatives](#list_representatives) - List representatives
* [get_representative](#get_representative) - Get representative
* [delete_representative](#delete_representative) - Delete a representative
* [patch_representative](#patch_representative) - Patch representative

## create_representative

Moov accounts associated with businesses require information regarding individuals who represent the business. You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. Read our [business representatives](https://docs.moov.io/guides/accounts/requirements/business-representatives/) guide to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.representatives.create_representative(account_id="602bcb92-e33e-47e9-874b-f8c8cdea8a6e", create_representative={
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
    "responsibilities": {
        "ownership_percentage": 38,
        "job_title": "CEO",
        "is_controller": False,
        "is_owner": True,
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
| `create_representative`                                             | [models.CreateRepresentative](../../models/createrepresentative.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateRepresentativeResponse](../../models/createrepresentativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_representatives

A Moov account may have multiple representatives depending on the associated business's ownership and management structure. You can use this method to list all the representatives for a given Moov account. Note that Moov accounts associated with an individual do not have representatives. Read our [business representatives](https://docs.moov.io/guides/accounts/requirements/business-representatives/) guide to learn more. <br><br> To use this endpoint from the browser, you need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.representatives.list_representatives(account_id="33c72fc5-9781-4400-9547-0fa6966c8791")

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

**[models.ListRepresentativesResponse](../../models/listrepresentativesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_representative

Retrieve a specific representative associated with a given Moov account. Read our [business representatives](https://docs.moov.io/guides/accounts/requirements/business-representatives/) guide to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.representatives.get_representative(account_id="64980616-9a3a-476e-b482-151eb6571b76", representative_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `representative_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | ID of the representative.                                           | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRepresentativeResponse](../../models/getrepresentativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_representative

Deletes a business representative associated with a Moov account. Read our [business representatives](https://docs.moov.io/guides/accounts/requirements/business-representatives/) guide to learn more. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.representatives.delete_representative(account_id="8c15ae30-39cc-45a6-a9b1-f96dfd44efa8", representative_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `representative_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | ID of the representative.                                           | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteRepresentativeResponse](../../models/deleterepresentativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## patch_representative

If a representative's information has changed you can patch the information associated with a specific representative ID. Read our [business representatives](https://docs.moov.io/guides/accounts/requirements/business-representatives/) guide to learn more. <br>  
To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/), and provide the changed information.

When **can** profile data be updated:
  + For unverified representatives, all profile data can be edited.
  + During the verification process, missing or incomplete profile data can be edited.
  + Verified representatives can only add missing profile data.

  When **can't** profile data be updated:
  + Verified representatives cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.representatives.patch_representative(account_id="356ead8f-1956-431d-a095-7878b3151fee", representative_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", patch_representative_request={
    "name": {
        "first_name": "Amanda",
        "middle_name": "Amanda",
        "last_name": "Yang",
        "suffix": "Jr",
    },
    "phone": {
        "number": "8185551212",
        "country_code": "1",
    },
    "email": "amanda@classbooker.dev",
    "address": {
        "address_line1": "123 Main Street",
        "address_line2": "Apt 302",
        "city": "Boulder",
        "state_or_province": "CO",
        "postal_code": "80301",
        "country": "US",
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
    "responsibilities": {
        "is_controller": False,
        "is_owner": True,
        "ownership_percentage": 38,
        "job_title": "CEO",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `account_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | ID of the account.                                                              |                                                                                 |
| `representative_id`                                                             | *str*                                                                           | :heavy_check_mark:                                                              | ID of the representative.                                                       | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                            |
| `patch_representative_request`                                                  | [models.PatchRepresentativeRequest](../../models/patchrepresentativerequest.md) | :heavy_check_mark:                                                              | N/A                                                                             |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.PatchRepresentativeResponse](../../models/patchrepresentativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |