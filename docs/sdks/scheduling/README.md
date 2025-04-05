# Scheduling
(*scheduling*)

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

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.create(account_id="9ab418fe-7b54-4964-a372-69b08e55ee8a", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
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
                description="delightfully fumigate convection though zowie up bulky electronics",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
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
                description="tackle unabashedly mentor early miserly stealthily without",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.RunTransfer(
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
            description="via deeply writ amid pupil yawningly wasabi when excepting councilman",
        ),
        start=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.list(account_id="c8a232aa-0b11-4b8a-b005-71e9e705d0e6", skip=60, count=20)

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

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.update(account_id="916f66c9-4a48-4a10-94fb-c5837b3ed84e", schedule_id="ce88be33-c224-42c1-ae8b-3533cc7b3742", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
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
                description="technician eulogise whereas till mild than during",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
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
                description="gosh frantically belabor past",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
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
                description="perfumed fisherman with",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.RunTransfer(
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
            description="hydrolyze lazily whenever how what",
        ),
        start=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.get(account_id="b888f774-3e7c-4135-a18c-6b985523c4bc", schedule_id="e50f7622-81da-484b-9c66-1c8a99c6b71b")

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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.cancel(account_id="0f713502-9233-41c6-9ebd-c570b7edb496", schedule_id="d50fbe4e-3e32-4613-8574-4d82f3fd6b3c")

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

```python
from moovio_sdk import Moov
from moovio_sdk.models import components


with Moov(
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.scheduling.get_occurrance(account_id="cdeb0c02-04f9-4e60-9768-3c10a2b2201d", schedule_id="47a51a3b-df1e-40c5-8048-918f18949779", occurrence_filter="<value>")

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