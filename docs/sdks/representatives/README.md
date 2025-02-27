# Representatives
(*representatives*)

## Overview

### Available Operations

* [create](#create) - Moov accounts associated with businesses require information regarding individuals who represent the business. 
You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.
* [list](#list) - A Moov account may have multiple representatives depending on the associated business's ownership and management structure. 
You can use this method to list all the representatives for a given Moov account. 
Note that Moov accounts associated with an individual do not have representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.
* [delete](#delete) - Deletes a business representative associated with a Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.
* [get](#get) - Retrieve a specific representative associated with a given Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.
* [update](#update) - If a representative's information has changed you can patch the information associated with a specific representative ID. 
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

## create

Moov accounts associated with businesses require information regarding individuals who represent the business. 
You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.

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

    res = moov.representatives.create(account_id="602bcb92-e33e-47e9-874b-f8c8cdea8a6e", name={
        "first_name": "Jordan",
        "last_name": "Lee",
        "middle_name": "Reese",
        "suffix": "Jr",
    }, phone={
        "number": "8185551212",
        "country_code": "1",
    }, email="jordan.lee@classbooker.dev", address={
        "address_line1": "123 Main Street",
        "city": "Boulder",
        "state_or_province": "CO",
        "postal_code": "80301",
        "country": "US",
        "address_line2": "Apt 302",
    }, birth_date={
        "day": 9,
        "month": 11,
        "year": 1989,
    }, responsibilities={
        "ownership_percentage": 38,
        "job_title": "CEO",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | ID of the account.                                                                                               |                                                                                                                  |
| `name`                                                                                                           | [components.IndividualName](../../models/components/individualname.md)                                           | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `phone`                                                                                                          | [Optional[components.PhoneNumber]](../../models/components/phonenumber.md)                                       | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `email`                                                                                                          | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | N/A                                                                                                              | jordan.lee@classbooker.dev                                                                                       |
| `address`                                                                                                        | [Optional[components.Address]](../../models/components/address.md)                                               | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `birth_date`                                                                                                     | [Optional[components.BirthDate]](../../models/components/birthdate.md)                                           | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `government_id`                                                                                                  | [Optional[components.GovernmentID]](../../models/components/governmentid.md)                                     | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `responsibilities`                                                                                               | [Optional[components.RepresentativeResponsibilities]](../../models/components/representativeresponsibilities.md) | :heavy_minus_sign:                                                                                               | Describes the job responsibilities of a business representative.                                                 |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.CreateRepresentativeResponse](../../models/operations/createrepresentativeresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400, 409                             | application/json                     |
| errors.RepresentativeValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## list

A Moov account may have multiple representatives depending on the associated business's ownership and management structure. 
You can use this method to list all the representatives for a given Moov account. 
Note that Moov accounts associated with an individual do not have representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.

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

    res = moov.representatives.list(account_id="33c72fc5-9781-4400-9547-0fa6966c8791")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListRepresentativesResponse](../../models/operations/listrepresentativesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a business representative associated with a Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.write` scope.

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

    res = moov.representatives.delete(account_id="8c15ae30-39cc-45a6-a9b1-f96dfd44efa8", representative_id="302eff0a-1b46-4437-bfa0-532d4401ffcd")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `representative_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | ID of the representative.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteRepresentativeResponse](../../models/operations/deleterepresentativeresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get

Retrieve a specific representative associated with a given Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/representatives.read` scope.

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

    res = moov.representatives.get(account_id="64980616-9a3a-476e-b482-151eb6571b76", representative_id="7b611595-93d0-48cc-9da4-3aac709d069a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `representative_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | ID of the representative.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRepresentativeResponse](../../models/operations/getrepresentativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

If a representative's information has changed you can patch the information associated with a specific representative ID. 
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

    res = moov.representatives.update(account_id="377d9553-179a-45f6-8ed4-c92810fbb4d0", representative_id="54619159-548e-45ed-b917-271fb71fc438", name={
        "first_name": "Jordan",
        "middle_name": "Reese",
        "last_name": "Lee",
        "suffix": "Jr",
    }, phone={
        "number": "8185551212",
        "country_code": "1",
    }, address={
        "address_line1": "123 Main Street",
        "address_line2": "Apt 302",
        "city": "Boulder",
        "state_or_province": "CO",
        "postal_code": "80301",
        "country": "US",
    }, birth_date={
        "day": 9,
        "month": 11,
        "year": 1989,
    }, responsibilities={
        "ownership_percentage": 38,
        "job_title": "CEO",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                 | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | ID of the account.                                                                                                           |
| `representative_id`                                                                                                          | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | ID of the representative.                                                                                                    |
| `name`                                                                                                                       | [Optional[components.IndividualNameUpdate]](../../models/components/individualnameupdate.md)                                 | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `phone`                                                                                                                      | [OptionalNullable[components.Phone]](../../models/components/phone.md)                                                       | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `email`                                                                                                                      | [OptionalNullable[components.Email]](../../models/components/email.md)                                                       | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `address`                                                                                                                    | [OptionalNullable[components.UpdateRepresentativeAddress]](../../models/components/updaterepresentativeaddress.md)           | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `birth_date`                                                                                                                 | [OptionalNullable[components.UpdateRepresentativeBirthDate]](../../models/components/updaterepresentativebirthdate.md)       | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `government_id`                                                                                                              | [OptionalNullable[components.UpdateRepresentativeGovernmentID]](../../models/components/updaterepresentativegovernmentid.md) | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `responsibilities`                                                                                                           | [OptionalNullable[components.Responsibilities]](../../models/components/responsibilities.md)                                 | :heavy_minus_sign:                                                                                                           | N/A                                                                                                                          |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.UpdateRepresentativeResponse](../../models/operations/updaterepresentativeresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |