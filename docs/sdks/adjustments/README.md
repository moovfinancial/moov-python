# Adjustments
(*adjustments*)

## Overview

### Available Operations

* [list_adjustments](#list_adjustments) - List adjustments associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/wallets.read` scope.
* [get_adjustment](#get_adjustment) - Retrieve a specific adjustment associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/wallets.read` scope.

## list_adjustments

List adjustments associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.adjustments.list_adjustments(security=moov.ListAdjustmentsSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="27396e19-5d2d-4fba-876d-423579b4f37e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.ListAdjustmentsSecurity](../../models/listadjustmentssecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `account_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `x_moov_version`                                                          | [Optional[models.Versions]](../../models/versions.md)                     | :heavy_minus_sign:                                                        | Specify an API version.                                                   |
| `wallet_id`                                                               | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A wallet ID to filter adjustments by.                                     |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[List[models.Adjustment]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_adjustment

Retrieve a specific adjustment associated with a Moov account.

To access this endpoint using a [token](https://docs.moov.io/api/authentication/access-tokens/) you'll need 
to specify the `/accounts/{accountID}/wallets.read` scope.

### Example Usage

```python
import moov
from moov import Moov

with Moov() as moov:

    res = moov.adjustments.get_adjustment(security=moov.GetAdjustmentSecurity(
        basic_auth=moov.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="7c43cb4c-5944-40f9-9bef-7925774b06b4", adjustment_id="244e9b18-1d97-4344-8a69-abf3c48078bc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.GetAdjustmentSecurity](../../models/getadjustmentsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `account_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `adjustment_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `x_moov_version`                                                      | [Optional[models.Versions]](../../models/versions.md)                 | :heavy_minus_sign:                                                    | Specify an API version.                                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Adjustment](../../models/adjustment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |