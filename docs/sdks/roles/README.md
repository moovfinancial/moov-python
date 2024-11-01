# Roles
(*roles*)

## Overview

### Available Operations

* [list_roles](#list_roles) - List roles
* [create_role](#create_role) - Create role
* [get_role](#get_role) - Get Role
* [update_role](#update_role) - Update role
* [disable_role](#disable_role) - Delete role
* [members_list](#members_list) - List members

## list_roles

Retrieve all roles for the account

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.list_roles()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListRolesResponse](../../models/listrolesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_role

Add a new role for the account

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.create_role(create_role={
    "name": "Amanda Yang",
    "subjects": [
        "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    ],
    "policies": [
        {
            "resource": moov.Resource.ROOT_BANK_ACCOUNTS,
            "action": moov.Action.WRITE,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `create_role`                                                       | [models.CreateRole](../../models/createrole.md)                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateRoleResponse](../../models/createroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_role

Retrieve a specific Role under the account

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.get_role(role_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the role to update                                            | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRoleResponse](../../models/getroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_role

Modify an existing Role for the account

### Example Usage

```python
import moov
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.update_role(role_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", update_role={
    "name": "Amanda Yang",
    "subjects": [
        "ec7e1848-dc80-4ab0-8827-dd7fc0737b43",
    ],
    "policies": [
        {
            "resource": moov.Resource.ROOT_TRANSFERS,
            "action": moov.Action.WRITE,
        },
        {
            "resource": moov.Resource.ROOT_TOS,
            "action": moov.Action.WRITE,
        },
        {
            "resource": moov.Resource.ROOT_TOS,
            "action": moov.Action.WRITE,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the role to update                                            | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `update_role`                                                       | [models.UpdateRole](../../models/updaterole.md)                     | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateRoleResponse](../../models/updateroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## disable_role

Disable a Role under the account

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.disable_role(role_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the role to update                                            | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DisableRoleResponse](../../models/disableroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## members_list

Retrieve all members connected to the account

### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.roles.members_list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_account_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MembersListResponse](../../models/memberslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |