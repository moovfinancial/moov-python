# Scheduling

## Overview

### Available Operations

* [create](#create) - Describes the schedule to create or modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [list](#list) - Describes a list of schedules associated with an account. Append the `hydrate=accounts` query parameter to include partial account details in the response.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [update](#update) - Describes the schedule to modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get](#get) - Describes a schedule associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.
* [cancel](#cancel) - Describes the schedule to cancel.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.
* [get_occurrance](#get_occurrance) - Gets a specific occurrence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

## create

Describes the schedule to create or modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSchedule" method="post" path="/accounts/{accountID}/schedules" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.create(account_id="38fd6ae1-0e70-4162-9359-d64482d61854", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=parse_datetime("2009-11-10T23:00:00Z"),
            run_transfer=components.CreateRunTransfer(
                amount=components.Amount(
                    currency="USD",
                    value=1204,
                ),
                destination=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                description="sediment yahoo a rudely mmm massive helpful brr",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=parse_datetime("2009-11-10T23:00:00Z"),
            run_transfer=components.CreateRunTransfer(
                amount=components.Amount(
                    currency="USD",
                    value=1204,
                ),
                destination=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                description="sediment yahoo a rudely mmm massive helpful brr",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.CreateRunTransfer(
            amount=components.Amount(
                currency="USD",
                value=1204,
            ),
            sales_tax_amount=components.Amount(
                currency="USD",
                value=1204,
            ),
            destination=components.SchedulePaymentMethod(
                payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                ach_details=components.AchDetails(
                    company_entry_description="Gym dues",
                    originating_company_name="Whole Body Fit",
                ),
                card_details=components.CardDetails(
                    dynamic_descriptor="WhlBdy *Yoga 11-12",
                ),
            ),
            partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            source=components.SchedulePaymentMethod(
                payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                ach_details=components.AchDetails(
                    company_entry_description="Gym dues",
                    originating_company_name="Whole Body Fit",
                ),
                card_details=components.CardDetails(
                    dynamic_descriptor="WhlBdy *Yoga 11-12",
                ),
            ),
            description="sediment yahoo a rudely mmm massive helpful brr",
            line_items=components.CreateScheduledTransferLineItems(
                items=[],
            ),
        ),
        start=parse_datetime("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Account ID of the account that will run the transfer.                |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Simple description of what the schedule is.                          |
| `occurrences`                                                        | List[[components.Occurrence](../../models/components/occurrence.md)] | :heavy_minus_sign:                                                   | N/A                                                                  |
| `recur`                                                              | [Optional[components.Recur]](../../models/components/recur.md)       | :heavy_minus_sign:                                                   | Defines configuration for recurring transfers.                       |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.CreateScheduleResponse](../../models/operations/createscheduleresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ScheduleValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## list

Describes a list of schedules associated with an account. Append the `hydrate=accounts` query parameter to include partial account details in the response.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="listSchedules" method="get" path="/accounts/{accountID}/schedules" -->
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

    res = moov.scheduling.list(account_id="b69f6366-984e-40f9-82a0-65335a43431d", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `skip`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 60                                                                  |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `hydrate`                                                           | [Optional[operations.Hydrate]](../../models/operations/hydrate.md)  | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListSchedulesResponse](../../models/operations/listschedulesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Describes the schedule to modify.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSchedule" method="put" path="/accounts/{accountID}/schedules/{scheduleID}" -->
```python
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.update(account_id="becca38e-c01f-4cfc-8f7c-187c7cf6a7a3", schedule_id="1b29a8ad-60ee-4c90-90e7-fda62cd24154", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=parse_datetime("2009-11-10T23:00:00Z"),
            run_transfer=components.CreateRunTransfer(
                amount=components.Amount(
                    currency="USD",
                    value=1204,
                ),
                destination=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                description="er reasoning following veto oof fervently ha how till now",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=parse_datetime("2009-11-10T23:00:00Z"),
            run_transfer=components.CreateRunTransfer(
                amount=components.Amount(
                    currency="USD",
                    value=1204,
                ),
                destination=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                description="er reasoning following veto oof fervently ha how till now",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=parse_datetime("2009-11-10T23:00:00Z"),
            run_transfer=components.CreateRunTransfer(
                amount=components.Amount(
                    currency="USD",
                    value=1204,
                ),
                destination=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source=components.SchedulePaymentMethod(
                    payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    ach_details=components.AchDetails(
                        company_entry_description="Gym dues",
                        originating_company_name="Whole Body Fit",
                    ),
                    card_details=components.CardDetails(
                        dynamic_descriptor="WhlBdy *Yoga 11-12",
                    ),
                ),
                description="er reasoning following veto oof fervently ha how till now",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.CreateRunTransfer(
            amount=components.Amount(
                currency="USD",
                value=1204,
            ),
            sales_tax_amount=components.Amount(
                currency="USD",
                value=1204,
            ),
            destination=components.SchedulePaymentMethod(
                payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                ach_details=components.AchDetails(
                    company_entry_description="Gym dues",
                    originating_company_name="Whole Body Fit",
                ),
                card_details=components.CardDetails(
                    dynamic_descriptor="WhlBdy *Yoga 11-12",
                ),
            ),
            partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            source=components.SchedulePaymentMethod(
                payment_method_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                ach_details=components.AchDetails(
                    company_entry_description="Gym dues",
                    originating_company_name="Whole Body Fit",
                ),
                card_details=components.CardDetails(
                    dynamic_descriptor="WhlBdy *Yoga 11-12",
                ),
            ),
            description="er reasoning following veto oof fervently ha how till now",
            line_items=components.CreateScheduledTransferLineItems(
                items=[
                    components.CreateScheduledTransferLineItem(
                        name="<value>",
                        base_price=components.AmountDecimal(
                            currency="USD",
                            value_decimal="12.987654321",
                        ),
                        quantity=973458,
                        options=[
                            components.CreateScheduledTransferLineItemOption(
                                name="<value>",
                                quantity=221042,
                                price_modifier=components.AmountDecimal(
                                    currency="USD",
                                    value_decimal="12.987654321",
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),
        start=parse_datetime("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Account ID of the account that will run the transfer.                |
| `schedule_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Simple description of what the schedule is.                          |
| `occurrences`                                                        | List[[components.Occurrence](../../models/components/occurrence.md)] | :heavy_minus_sign:                                                   | N/A                                                                  |
| `recur`                                                              | [Optional[components.Recur]](../../models/components/recur.md)       | :heavy_minus_sign:                                                   | Defines configuration for recurring transfers.                       |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.UpdateScheduleResponse](../../models/operations/updatescheduleresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ScheduleValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## get

Describes a schedule associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSchedules" method="get" path="/accounts/{accountID}/schedules/{scheduleID}" -->
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

    res = moov.scheduling.get(account_id="31afd98b-eb55-41b3-8a4f-0ee8ea69e4e0", schedule_id="55487e07-f3b7-44e8-b6f3-64fc85701c34")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSchedulesResponse](../../models/operations/getschedulesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## cancel

Describes the schedule to cancel.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="cancelSchedule" method="delete" path="/accounts/{accountID}/schedules/{scheduleID}" -->
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

    res = moov.scheduling.cancel(account_id="e89edcfc-19ca-40eb-802b-a35100dea24d", schedule_id="5ca67de0-63f6-4cb7-b94a-6c84616ffe03")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Your Moov account ID as the partner running the transfers.          |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CancelScheduleResponse](../../models/operations/cancelscheduleresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_occurrance

Gets a specific occurrence.

To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/) 
you'll need to specify the `/accounts/{accountID}/transfers.read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getScheduledOccurrence" method="get" path="/accounts/{accountID}/schedules/{scheduleID}/occurrences/{occurrenceFilter}" -->
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

    res = moov.scheduling.get_occurrance(account_id="ea12b5d5-6249-4af2-ae48-6141a5251090", schedule_id="289e94cd-66f1-4df5-999f-46d0f40b4ce9", occurrence_filter="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| `schedule_id`                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| `occurrence_filter`                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | Allows the specification of additional filters beyond the UUID.<br/><br/>Specifying a UUID string returns the exact occurrence.<br/>Specifying a RFC 3339 timestamp returns the latest occurrence at or before that timestamp.<br/>Specifying `latest` returns the latest occurrence at or before now. |
| `retries`                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                    |

### Response

**[operations.GetScheduledOccurrenceResponse](../../models/operations/getscheduledoccurrenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |