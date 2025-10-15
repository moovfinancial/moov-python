# Products
(*products*)

## Overview

### Available Operations

* [list](#list) - List active (non-disabled) products for an account.
* [create](#create) - Creates a new product for the specified account.
* [get](#get) - Retrieve a product by ID.
* [update](#update) - Update a product and its options.
* [disable](#disable) - Disable a product by ID.

The product will no longer be available, but will remain in the system for historical and reporting purposes.

## list

List active (non-disabled) products for an account.

### Example Usage

<!-- UsageSnippet language="python" operationID="listProducts" method="get" path="/accounts/{accountID}/products" -->
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

    res = moov.products.list(account_id="cd696219-4308-446c-b0d8-1759254995c2", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `skip`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 60                                                                  |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListProductsResponse](../../models/operations/listproductsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new product for the specified account.

### Example Usage

<!-- UsageSnippet language="python" operationID="createProduct" method="post" path="/accounts/{accountID}/products" -->
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

    res = moov.products.create(account_id="27cd3181-7c1c-4d81-b020-e7d55c33941f", title="World's best lemonade", base_price={
        "currency": "USD",
        "value_decimal": "4.99",
    }, description="Really, the best.", images=[
        {
            "image_id": "fed91252-6f48-4b70-885e-520bf53a52ff",
        },
        {
            "image_id": "eb466644-0a58-4b87-af1e-94d03e223ad2",
        },
    ], option_groups=[
        {
            "name": "Flavor add-ins",
            "description": "Choose up to 3 flavor add-ins to enhance your lemonade.",
            "min_select": 0,
            "max_select": 3,
            "options": [
                {
                    "name": "Strawberry puree",
                    "description": "Fresh and fruity.",
                    "price_modifier": "0.99",
                    "images": [
                        {
                            "image_id": "d359808d-9896-4414-8d17-dac43f35842d",
                        },
                    ],
                },
                {
                    "name": "Passionfruit syrup",
                    "price_modifier": "0.49",
                },
                {
                    "name": "Cherry syrup",
                    "price_modifier": "0.49",
                },
            ],
        },
        {
            "name": "Sweetener",
            "description": "Choose a sweetener for your lemonade.",
            "min_select": 1,
            "max_select": 1,
            "options": [
                {
                    "name": "Cane Sugar",
                },
                {
                    "name": "Honey",
                    "price_modifier": "0.99",
                },
                {
                    "name": "Stevia",
                    "description": "Natural, zero-calorie sweetener.",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                       | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | N/A                                                                                                                                                |
| `title`                                                                                                                                            | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | N/A                                                                                                                                                |
| `base_price`                                                                                                                                       | [components.AmountDecimal](../../models/components/amountdecimal.md)                                                                               | :heavy_check_mark:                                                                                                                                 | A product's starting price, before applying modifiers.                                                                                             |
| `description`                                                                                                                                      | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | A detailed description of the product.<br/><br/>- Must be valid UTF-8 text<br/>- Supports Markdown for formatting<br/>- HTML is not permitted and will be rejected |
| `images`                                                                                                                                           | List[[components.AssignProductImage](../../models/components/assignproductimage.md)]                                                               | :heavy_minus_sign:                                                                                                                                 | Assign previously uploaded images to a product or option.                                                                                          |
| `option_groups`                                                                                                                                    | List[[components.CreateProductOptionGroup](../../models/components/createproductoptiongroup.md)]                                                   | :heavy_minus_sign:                                                                                                                                 | Optional configuration options for a product, such as size or color.                                                                               |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[operations.CreateProductResponse](../../models/operations/createproductresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400, 409                             | application/json                     |
| errors.ProductRequestValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## get

Retrieve a product by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProduct" method="get" path="/accounts/{accountID}/products/{productID}" -->
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

    res = moov.products.get(account_id="a749d848-5ebc-42a4-9ae6-555804317835", product_id="dd0b4873-5cf5-4aa8-aa86-e31d86f7e38a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetProductResponse](../../models/operations/getproductresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a product and its options.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateProduct" method="put" path="/accounts/{accountID}/products/{productID}" -->
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

    res = moov.products.update(account_id="7a7b55ed-d90d-4e83-a8f6-f146eaebd0cc", product_id="fa407877-3b46-4484-814e-65b147d76a9e", title="<value>", base_price={
        "currency": "USD",
        "value_decimal": "12.987654321",
    }, option_groups=[
        {
            "name": "<value>",
            "min_select": 328576,
            "max_select": 430951,
            "options": [],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                       | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | N/A                                                                                                                                                |
| `product_id`                                                                                                                                       | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | N/A                                                                                                                                                |
| `title`                                                                                                                                            | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | N/A                                                                                                                                                |
| `base_price`                                                                                                                                       | [components.AmountDecimal](../../models/components/amountdecimal.md)                                                                               | :heavy_check_mark:                                                                                                                                 | A product's starting price, before applying modifiers.                                                                                             |
| `description`                                                                                                                                      | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | A detailed description of the product.<br/><br/>- Must be valid UTF-8 text<br/>- Supports Markdown for formatting<br/>- HTML is not permitted and will be rejected |
| `images`                                                                                                                                           | List[[components.AssignProductImage](../../models/components/assignproductimage.md)]                                                               | :heavy_minus_sign:                                                                                                                                 | Assign previously uploaded images to a product or option.                                                                                          |
| `option_groups`                                                                                                                                    | List[[components.CreateProductOptionGroup](../../models/components/createproductoptiongroup.md)]                                                   | :heavy_minus_sign:                                                                                                                                 | Optional configuration options for a product, such as size or color.                                                                               |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[operations.UpdateProductResponse](../../models/operations/updateproductresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GenericError                  | 400, 409                             | application/json                     |
| errors.ProductRequestValidationError | 422                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## disable

Disable a product by ID.

The product will no longer be available, but will remain in the system for historical and reporting purposes.

### Example Usage

<!-- UsageSnippet language="python" operationID="disableProduct" method="delete" path="/accounts/{accountID}/products/{productID}" -->
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

    res = moov.products.disable(account_id="9fbe72c0-abba-4bb7-b1d0-d15ee702fe62", product_id="1e11a7dc-4e86-41ed-b256-55c22f3bfd38")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DisableProductResponse](../../models/operations/disableproductresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |