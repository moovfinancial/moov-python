# Scheduling
(*scheduling*)

## Overview

### Available Operations

* [create_schedule](#create_schedule) - Describes the schedule to create or modify.
* [list_schedules](#list_schedules) - Describes a list of schedules associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.
* [update_schedule](#update_schedule) - Describes the schedule to modify.
* [get_schedules](#get_schedules) - Describes a schedule associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.
* [cancel_schedule](#cancel_schedule) - Describes the schedule to cancel.
* [get_scheduled_occurrence](#get_scheduled_occurrence) - Defines an occurrence for when to run a transfer.

## create_schedule

Describes the schedule to create or modify.

### Example Usage

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.scheduling.create_schedule(security=operations.CreateScheduleSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="85154287-4ee0-4c8f-89d9-6c4a524b28f0", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
                amount={
                    "currency": "USD",
                    "value": 1204,
                },
                destination={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                description="ajar ornate bah calculus circumference fiercely ornate",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
                amount={
                    "currency": "USD",
                    "value": 1204,
                },
                destination={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                description="scented whether once why unexpectedly",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
                amount={
                    "currency": "USD",
                    "value": 1204,
                },
                destination={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                description="formation dreamily exasperation but yuck psst nautical",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.RunTransfer(
            amount={
                "currency": "USD",
                "value": 1204,
            },
            destination={
                "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                "ach_details": {
                    "company_entry_description": "Gym dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            source={
                "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                "ach_details": {
                    "company_entry_description": "Gym dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            description="adjourn briskly amidst modulo gosh foolishly",
        ),
        start=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.CreateScheduleSecurity](../../models/operations/createschedulesecurity.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `x_moov_version`                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                   | :heavy_minus_sign:                                                                     | Specify an API version.                                                                |
| `description`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Simple description of what the schedule is.                                            |
| `occurrences`                                                                          | List[[components.Occurrence](../../models/components/occurrence.md)]                   | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `recur`                                                                                | [Optional[components.Recur]](../../models/components/recur.md)                         | :heavy_minus_sign:                                                                     | Defines configuration for recurring transfers.                                         |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[components.ScheduleResponse](../../models/components/scheduleresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ScheduleValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## list_schedules

Describes a list of schedules associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.scheduling.list_schedules(security=operations.ListSchedulesSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="f5b39da1-b677-43d6-b114-65cbbea83ad5", skip=60, count=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [operations.ListSchedulesSecurity](../../models/operations/listschedulessecurity.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |                                                                                      |
| `account_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |                                                                                      |
| `x_moov_version`                                                                     | [Optional[components.Versions]](../../models/components/versions.md)                 | :heavy_minus_sign:                                                                   | Specify an API version.                                                              |                                                                                      |
| `skip`                                                                               | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  | 60                                                                                   |
| `count`                                                                              | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  | 20                                                                                   |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |                                                                                      |

### Response

**[List[components.ScheduleResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_schedule

Describes the schedule to modify.

### Example Usage

```python
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.scheduling.update_schedule(security=operations.UpdateScheduleSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="9122f67d-60fd-4e10-9f18-023929ab3209", schedule_id="a4599c7c-e943-47b9-8e40-0834618798a5", occurrences=[
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
                amount={
                    "currency": "USD",
                    "value": 1204,
                },
                destination={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                description="playfully better now relative athwart lest anesthetize",
            ),
        ),
        components.Occurrence(
            occurrence_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            run_on=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
            run_transfer=components.RunTransfer(
                amount={
                    "currency": "USD",
                    "value": 1204,
                },
                destination={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                source={
                    "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                    "ach_details": {
                        "company_entry_description": "Gym dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                description="whereas reboot probate prejudge which mobility carefully",
            ),
        ),
    ], recur=components.Recur(
        recurrence_rule="<value>",
        run_transfer=components.RunTransfer(
            amount={
                "currency": "USD",
                "value": 1204,
            },
            destination={
                "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                "ach_details": {
                    "company_entry_description": "Gym dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            partner_account_id="c520f1b9-0ba7-42f5-b977-248cdbe41c69",
            source={
                "payment_method_id": "c520f1b9-0ba7-42f5-b977-248cdbe41c69",
                "ach_details": {
                    "company_entry_description": "Gym dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            description="fooey heavily immediately abaft justly phooey when separately",
        ),
        start=dateutil.parser.isoparse("2009-11-10T23:00:00Z"),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.UpdateScheduleSecurity](../../models/operations/updateschedulesecurity.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `schedule_id`                                                                          | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `x_moov_version`                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                   | :heavy_minus_sign:                                                                     | Specify an API version.                                                                |
| `description`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Simple description of what the schedule is.                                            |
| `occurrences`                                                                          | List[[components.Occurrence](../../models/components/occurrence.md)]                   | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `recur`                                                                                | [Optional[components.Recur]](../../models/components/recur.md)                         | :heavy_minus_sign:                                                                     | Defines configuration for recurring transfers.                                         |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[components.ScheduleResponse](../../models/components/scheduleresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GenericError            | 400, 409                       | application/json               |
| errors.ScheduleValidationError | 422                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## get_schedules

Describes a schedule associated with an account. Requires at least 1 occurrence or recurTransfer to be specified.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.scheduling.get_schedules(security=operations.GetSchedulesSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="aa7a59b8-5d59-4efd-99e7-b644e71e5f8c", schedule_id="605976e8-f3ff-4e64-9b41-7255577d6f44")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.GetSchedulesSecurity](../../models/operations/getschedulessecurity.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `account_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `schedule_id`                                                                      | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `x_moov_version`                                                                   | [Optional[components.Versions]](../../models/components/versions.md)               | :heavy_minus_sign:                                                                 | Specify an API version.                                                            |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[components.ScheduleResponse](../../models/components/scheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## cancel_schedule

Describes the schedule to cancel.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    moov.scheduling.cancel_schedule(security=operations.CancelScheduleSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="a1303a1c-8708-447e-a64b-5dba8417b641", schedule_id="ab5ca483-e27d-48f0-b596-09eed517874f")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.CancelScheduleSecurity](../../models/operations/cancelschedulesecurity.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `schedule_id`                                                                          | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `x_moov_version`                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                   | :heavy_minus_sign:                                                                     | Specify an API version.                                                                |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.GenericError | 400, 409            | application/json    |
| errors.APIError     | 4XX, 5XX            | \*/\*               |

## get_scheduled_occurrence

Defines an occurrence for when to run a transfer.

### Example Usage

```python
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.scheduling.get_scheduled_occurrence(security=operations.GetScheduledOccurrenceSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_id="7175f455-a6d6-4b87-8e24-cbd12c7dabe7", schedule_id="a4ffa63d-9228-4488-8f27-d2ff59d7760c", occurrence_filter="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                             | [operations.GetScheduledOccurrenceSecurity](../../models/operations/getscheduledoccurrencesecurity.md)                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| `account_id`                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| `schedule_id`                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| `occurrence_filter`                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | Allows the specification of additional filters beyond the UUID.<br/><br/>Specifying a UUID string returns the exact occurrence.<br/>Specifying a RFC 3339 timestamp returns the latest occurrence at or before that timestamp.<br/>Specifying `latest` returns the latest occurrence at or before now. |
| `x_moov_version`                                                                                                                                                                                                                                                                       | [Optional[components.Versions]](../../models/components/versions.md)                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | Specify an API version.                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                    |

### Response

**[components.ScheduleResponse](../../models/components/scheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |