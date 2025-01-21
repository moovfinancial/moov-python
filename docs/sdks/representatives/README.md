# Representatives
(*representatives*)

## Overview

### Available Operations

* [create_representative](#create_representative) - Moov accounts associated with businesses require information regarding individuals who represent the business. 
You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [list_representatives](#list_representatives) - A Moov account may have multiple representatives depending on the associated business’s ownership and management structure. 
You can use this method to list all the representatives for a given Moov account. 
Note that Moov accounts associated with an individual do not have representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [delete_representative](#delete_representative) - Deletes a business representative associated with a Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [get_representative](#get_representative) - Retrieve a specific representative associated with a given Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).
* [update_representative](#update_representative) - If a representative’s information has changed you can patch the information associated with a specific representative ID. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

When **can** profile data be updated:

- For unverified representatives, all profile data can be edited.
- During the verification process, missing or incomplete profile data can be edited.
- Verified representatives can only add missing profile data.

When **can’t** profile data be updated:

- Verified representatives cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

## create_representative

Moov accounts associated with businesses require information regarding individuals who represent the business. 
You can provide this information by creating a representative. Each account is allowed a maximum of 7 representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.representatives.create_representative(security=moov.CreateRepresentativeSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="602bcb92-e33e-47e9-874b-f8c8cdea8a6e", name={
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

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.CreateRepresentativeSecurity](../../models/createrepresentativesecurity.md)               | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `account_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | ID of the account.                                                                                |                                                                                                   |
| `name`                                                                                            | [models.IndividualName](../../models/individualname.md)                                           | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `x_moov_version`                                                                                  | [Optional[models.Versions]](../../models/versions.md)                                             | :heavy_minus_sign:                                                                                | Specify an API version.                                                                           |                                                                                                   |
| `phone`                                                                                           | [Optional[models.PhoneNumber]](../../models/phonenumber.md)                                       | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `email`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               | jordan.lee@classbooker.dev                                                                        |
| `address`                                                                                         | [Optional[models.Address]](../../models/address.md)                                               | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `birth_date`                                                                                      | [Optional[models.BirthDate]](../../models/birthdate.md)                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `government_id`                                                                                   | [Optional[models.GovernmentID]](../../models/governmentid.md)                                     | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `responsibilities`                                                                                | [Optional[models.RepresentativeResponsibilities]](../../models/representativeresponsibilities.md) | :heavy_minus_sign:                                                                                | Describes the job responsibilities of a business representative.                                  |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.Representative](../../models/representative.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.GenericError                  | 400, 409                             | application/json                     |
| models.RepresentativeValidationError | 422                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## list_representatives

A Moov account may have multiple representatives depending on the associated business’s ownership and management structure. 
You can use this method to list all the representatives for a given Moov account. 
Note that Moov accounts associated with an individual do not have representatives. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.representatives.list_representatives(security=moov.ListRepresentativesSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="33c72fc5-9781-4400-9547-0fa6966c8791")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.ListRepresentativesSecurity](../../models/listrepresentativessecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `account_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | ID of the account.                                                                |
| `x_moov_version`                                                                  | [Optional[models.Versions]](../../models/versions.md)                             | :heavy_minus_sign:                                                                | Specify an API version.                                                           |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[List[models.Representative]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_representative

Deletes a business representative associated with a Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    moov.representatives.delete_representative(security=moov.DeleteRepresentativeSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="8c15ae30-39cc-45a6-a9b1-f96dfd44efa8", representative_id="302eff0a-1b46-4437-bfa0-532d4401ffcd")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.DeleteRepresentativeSecurity](../../models/deleterepresentativesecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `account_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the account.                                                                  |
| `representative_id`                                                                 | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the representative.                                                           |
| `x_moov_version`                                                                    | [Optional[models.Versions]](../../models/versions.md)                               | :heavy_minus_sign:                                                                  | Specify an API version.                                                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_representative

Retrieve a specific representative associated with a given Moov account. Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.representatives.get_representative(security=moov.GetRepresentativeSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="64980616-9a3a-476e-b482-151eb6571b76", representative_id="7b611595-93d0-48cc-9da4-3aac709d069a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetRepresentativeSecurity](../../models/getrepresentativesecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `account_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | ID of the account.                                                            |
| `representative_id`                                                           | *str*                                                                         | :heavy_check_mark:                                                            | ID of the representative.                                                     |
| `x_moov_version`                                                              | [Optional[models.Versions]](../../models/versions.md)                         | :heavy_minus_sign:                                                            | Specify an API version.                                                       |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.Representative](../../models/representative.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_representative

If a representative’s information has changed you can patch the information associated with a specific representative ID. 
Read our [business representatives guide](https://docs.moov.io/guides/accounts/requirements/business-representatives/) to learn more.

To use this endpoint from the browser, you’ll need to specify the `/accounts/{accountID}/representatives.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

When **can** profile data be updated:

- For unverified representatives, all profile data can be edited.
- During the verification process, missing or incomplete profile data can be edited.
- Verified representatives can only add missing profile data.

When **can’t** profile data be updated:

- Verified representatives cannot change any existing profile data.

If you need to update information in a locked state, please contact Moov support.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.representatives.update_representative(security=moov.UpdateRepresentativeSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="377d9553-179a-45f6-8ed4-c92810fbb4d0", representative_id="54619159-548e-45ed-b917-271fb71fc438", name={
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

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.UpdateRepresentativeSecurity](../../models/updaterepresentativesecurity.md)                           | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `account_id`                                                                                                  | *str*                                                                                                         | :heavy_check_mark:                                                                                            | ID of the account.                                                                                            |
| `representative_id`                                                                                           | *str*                                                                                                         | :heavy_check_mark:                                                                                            | ID of the representative.                                                                                     |
| `x_moov_version`                                                                                              | [Optional[models.Versions]](../../models/versions.md)                                                         | :heavy_minus_sign:                                                                                            | Specify an API version.                                                                                       |
| `name`                                                                                                        | [Optional[models.IndividualNameUpdate]](../../models/individualnameupdate.md)                                 | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `phone`                                                                                                       | [OptionalNullable[models.Phone]](../../models/phone.md)                                                       | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `email`                                                                                                       | [OptionalNullable[models.Email]](../../models/email.md)                                                       | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `address`                                                                                                     | [OptionalNullable[models.UpdateRepresentativeAddress]](../../models/updaterepresentativeaddress.md)           | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `birth_date`                                                                                                  | [OptionalNullable[models.UpdateRepresentativeBirthDate]](../../models/updaterepresentativebirthdate.md)       | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `government_id`                                                                                               | [OptionalNullable[models.UpdateRepresentativeGovernmentID]](../../models/updaterepresentativegovernmentid.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `responsibilities`                                                                                            | [OptionalNullable[models.Responsibilities]](../../models/responsibilities.md)                                 | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.Representative](../../models/representative.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.GenericError | 400, 409            | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |