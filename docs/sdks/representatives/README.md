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

<!-- UsageSnippet language="python" operationID="createRepresentative" method="post" path="/accounts/{accountID}/representatives" -->
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

    res = moov.representatives.create(account_id="5abfe3a5-7cd3-4f92-a8bd-19b64e3ccc10", name={
        "first_name": "Jordan",
        "middle_name": "Reese",
        "last_name": "Lee",
        "suffix": "Jr",
    }, phone={
        "number": "8185551212",
        "country_code": "1",
    }, email="jordan.lee@classbooker.dev", address={
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

<!-- UsageSnippet language="python" operationID="listRepresentatives" method="get" path="/accounts/{accountID}/representatives" -->
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

    res = moov.representatives.list(account_id="aa071158-7ed6-4c18-af34-4fa37b755e53")

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

<!-- UsageSnippet language="python" operationID="deleteRepresentative" method="delete" path="/accounts/{accountID}/representatives/{representativeID}" -->
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

    res = moov.representatives.delete(account_id="23b950c7-3ccf-4edc-9566-07f765d57c73", representative_id="74d0f56b-b81b-467a-bc86-47a55fe5e503")

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

<!-- UsageSnippet language="python" operationID="getRepresentative" method="get" path="/accounts/{accountID}/representatives/{representativeID}" -->
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

    res = moov.representatives.get(account_id="071b8a57-e691-4e4b-9143-75f1a828ce9b", representative_id="00d87070-b167-48e6-be2f-198b5e1556c4")

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

<!-- UsageSnippet language="python" operationID="updateRepresentative" method="patch" path="/accounts/{accountID}/representatives/{representativeID}" -->
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

    res = moov.representatives.update(account_id="76647e2b-97ea-4551-8275-7153219f3317", representative_id="e89d3d0d-fbe3-4df6-8b18-d7cbcb761161", name={
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
    }, birth_date=None, responsibilities={
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