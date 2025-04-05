# PaymentLinks
(*payment_links*)

## Overview

### Available Operations

* [create](#create) - Create a payment link that allows an end user to make a payment on Moov's hosted payment link page.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](#list) - List all the payment links created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [get](#get) - Retrieve a payment link by code.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](#update) - Update a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [disable](#disable) - Disable a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_qr_code](#get_qr_code) - Retrieve the payment link encoded in a QR code. 

Use the `Accept` header to specify the format of the response. Supported formats are `application/json` and `image/png`.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

## create

Create a payment link that allows an end user to make a payment on Moov's hosted payment link page.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.payment_links.create(account_id="621cf021-cd9c-4f54-a033-15211a509a30", partner_account_id="d290f1ee-6c54-4b01-90e6-d701748f0851", merchant_payment_method_id="4c4e7f8e-81f4-4f3d-8f6f-6f6e7f8e4c4e", amount={
        "currency": "USD",
        "value": 1204,
    }, display={
        "title": "Example Payment Link",
        "description": "This is an example payment link.",
        "call_to_action": components.CallToAction.PAY,
    }, customer={
        "require_phone": True,
    }, payment={
        "allowed_methods": [
            components.CollectionPaymentMethodType.CARD_PAYMENT,
            components.CollectionPaymentMethodType.ACH_DEBIT_COLLECT,
        ],
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym dues",
            "originating_company_name": "Whole Body Fit",
        },
    }, payout={
        "allowed_methods": [
            components.DisbursementPaymentMethodType.ACH_CREDIT_SAME_DAY,
        ],
        "recipient": {
            "email": "jordan.lee@classbooker.dev",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `partner_account_id`                                                                                              | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The partner's Moov account ID.                                                                                    |
| `merchant_payment_method_id`                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The merchant's preferred payment method ID. Must be a wallet payment method.                                      |
| `amount`                                                                                                          | [components.Amount](../../models/components/amount.md)                                                            | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `display`                                                                                                         | [components.PaymentLinkDisplayOptions](../../models/components/paymentlinkdisplayoptions.md)                      | :heavy_check_mark:                                                                                                | Customizable display options for a payment link.                                                                  |
| `max_uses`                                                                                                        | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | An optional limit on the number of times this payment link can be used. <br/><br/>**For payouts, `maxUses` is always 1.** |
| `expires_on`                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_minus_sign:                                                                                                | An optional expiration date for this payment link.                                                                |
| `customer`                                                                                                        | [Optional[components.PaymentLinkCustomerOptions]](../../models/components/paymentlinkcustomeroptions.md)          | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `payment`                                                                                                         | [Optional[components.PaymentLinkPaymentDetails]](../../models/components/paymentlinkpaymentdetails.md)            | :heavy_minus_sign:                                                                                                | Options for payment links used to collect payment.                                                                |
| `payout`                                                                                                          | [Optional[components.PaymentLinkPayoutDetails]](../../models/components/paymentlinkpayoutdetails.md)              | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[operations.CreatePaymentLinkResponse](../../models/operations/createpaymentlinkresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GenericError           | 400, 409                      | application/json              |
| errors.CreatePaymentLinkError | 422                           | application/json              |
| errors.APIError               | 4XX, 5XX                      | \*/\*                         |

## list

List all the payment links created under a Moov account.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.payment_links.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListPaymentLinksResponse](../../models/operations/listpaymentlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a payment link by code.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

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

    res = moov.payment_links.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", payment_link_code="uc7ZYKrMhi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `payment_link_code`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetPaymentLinkResponse](../../models/operations/getpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.payment_links.update(account_id="d95fa7f0-e743-42ce-b47c-b60cc78135dd", payment_link_code="uc7ZYKrMhi", amount={
        "currency": "USD",
        "value": 1204,
    }, customer={
        "require_address": True,
        "require_phone": True,
    }, payment={
        "card_details": {
            "dynamic_descriptor": "WhlBdy *Yoga 11-12",
        },
        "ach_details": {
            "company_entry_description": "Gym dues",
            "originating_company_name": "Whole Body Fit",
        },
    }, payout={
        "recipient": {
            "email": "jordan.lee@classbooker.dev",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                       | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `payment_link_code`                                                                                                | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                | uc7ZYKrMhi                                                                                                         |
| `amount`                                                                                                           | [Optional[components.AmountUpdate]](../../models/components/amountupdate.md)                                       | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `expires_on`                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                               | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `display`                                                                                                          | [Optional[components.PaymentLinkDisplayOptionsUpdate]](../../models/components/paymentlinkdisplayoptionsupdate.md) | :heavy_minus_sign:                                                                                                 | Customizable display options for a payment link.                                                                   |                                                                                                                    |
| `customer`                                                                                                         | [Optional[components.PaymentLinkCustomerOptions]](../../models/components/paymentlinkcustomeroptions.md)           | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `payment`                                                                                                          | [Optional[components.PaymentLinkPaymentDetailsUpdate]](../../models/components/paymentlinkpaymentdetailsupdate.md) | :heavy_minus_sign:                                                                                                 | Options for payment links used to collect payment.                                                                 |                                                                                                                    |
| `payout`                                                                                                           | [Optional[components.PaymentLinkPayoutDetailsUpdate]](../../models/components/paymentlinkpayoutdetailsupdate.md)   | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |                                                                                                                    |

### Response

**[operations.UpdatePaymentLinkResponse](../../models/operations/updatepaymentlinkresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GenericError           | 400, 409                      | application/json              |
| errors.UpdatePaymentLinkError | 422                           | application/json              |
| errors.APIError               | 4XX, 5XX                      | \*/\*                         |

## disable

Disable a payment link.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.payment_links.disable(account_id="cd7cd1ce-90cc-444b-ac3e-badb79be277f", payment_link_code="uc7ZYKrMhi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `payment_link_code`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.DisablePaymentLinkResponse](../../models/operations/disablepaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_qr_code

Retrieve the payment link encoded in a QR code. 

Use the `Accept` header to specify the format of the response. Supported formats are `application/json` and `image/png`.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

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

    res = moov.payment_links.get_qr_code(account_id="2014a1ff-9924-40b3-ac01-f4ed64dac1b8", payment_link_code="uc7ZYKrMhi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `payment_link_code`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | uc7ZYKrMhi                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetPaymentLinkQRCodeResponse](../../models/operations/getpaymentlinkqrcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |