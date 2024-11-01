# Schedules
(*schedules*)

## Overview

Set up future transfers through scheduling.


### Available Operations

* [list_schedules](#list_schedules) - List schedules
* [create_schedule](#create_schedule) - Create schedule
* [get_schedules](#get_schedules) - Get schedule
* [update_schedule](#update_schedule) - Update schedule
* [cancel_schedule](#cancel_schedule) - Cancel schedule
* [get_scheduled_occurrence](#get_scheduled_occurrence) - Get occurrence

## list_schedules

List all schedules associated with accountID.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.list_schedules(account_id="f5b39da1-b677-43d6-b114-65cbbea83ad5")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSchedulesResponse](../../models/listschedulesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_schedule

Create a schedule on the specified account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.create_schedule(account_id="3cc39187-0d6f-4895-ab44-449e9d7e16fa", upsert_schedule={
    "recur": {
        "recurrence_rule": "FREQ=DAILY;COUNT=5",
        "run_transfer": {
            "amount": {
                "currency": "USD",
                "value": 1204,
            },
            "partner_account_id": "b827a5a9-0fa8-4459-b997-8745af19a961",
            "source": {
                "payment_method_id": "d1ebc2a0-b0d2-43cd-86d6-c953ad65ab9d",
                "ach_details": {
                    "company_entry_description": "Gym Dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            "destination": {
                "payment_method_id": "797d9a61-4c83-4b43-a4cf-def9c5d86929",
                "ach_details": {
                    "company_entry_description": "Gym Dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
        },
    },
    "occurrences": [
        {
            "run_transfer": {
                "amount": {
                    "currency": "USD",
                    "value": 1204,
                },
                "partner_account_id": "56012f72-28b2-4e94-9ac3-d5020f81fd00",
                "source": {
                    "payment_method_id": "57e18dfc-b7b8-462e-a966-a069c926138f",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                "destination": {
                    "payment_method_id": "71269395-39bb-451a-aad8-773104851542",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
            },
            "run_on": dateutil.parser.isoparse("2023-05-11T01:51:19.130Z"),
        },
        {
            "run_transfer": {
                "amount": {
                    "currency": "USD",
                    "value": 1204,
                },
                "partner_account_id": "4ee0c8f9-d96c-44a5-924b-28f02e5d05ca",
                "source": {
                    "payment_method_id": "33b07d59-e588-41aa-837c-85ccf1fc3bac",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                "destination": {
                    "payment_method_id": "60611c15-e34d-4481-9a02-c16a0225efe4",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
            },
            "run_on": dateutil.parser.isoparse("2022-11-02T15:28:12.172Z"),
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
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |
| `upsert_schedule`                                                   | [models.UpsertSchedule](../../models/upsertschedule.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateScheduleResponse](../../models/createscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## get_schedules

Get a schedule associated with accountID.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.get_schedules(account_id="aa7a59b8-5d59-4efd-99e7-b644e71e5f8c", schedule_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the schedule                                                  | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSchedulesResponse](../../models/getschedulesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_schedule

Update a schedule on the specified account.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
import dateutil.parser
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.update_schedule(account_id="462e3d5c-86c5-4f88-a79d-fb7161f73e54", schedule_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", upsert_schedule={
    "recur": {
        "recurrence_rule": "FREQ=DAILY;COUNT=5",
        "run_transfer": {
            "amount": {
                "currency": "USD",
                "value": 1204,
            },
            "partner_account_id": "691e09e4-9dea-49a9-a11e-2071752824ab",
            "source": {
                "payment_method_id": "6456038c-c7d6-489e-b3f2-009a3cd28d77",
                "ach_details": {
                    "company_entry_description": "Gym Dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
            "destination": {
                "payment_method_id": "169a5915-76a8-4214-a42a-153048d8e914",
                "ach_details": {
                    "company_entry_description": "Gym Dues",
                    "originating_company_name": "Whole Body Fit",
                },
                "card_details": {
                    "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                },
            },
        },
    },
    "occurrences": [
        {
            "run_transfer": {
                "amount": {
                    "currency": "USD",
                    "value": 1204,
                },
                "partner_account_id": "a70fd61a-d17b-45d3-8bad-9d559a08205f",
                "source": {
                    "payment_method_id": "ba030011-8126-4e45-a189-1abc554c0aa3",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                "destination": {
                    "payment_method_id": "4b9122f6-7d60-4fde-810f-18023929ab32",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
            },
            "run_on": dateutil.parser.isoparse("2023-10-12T23:27:40.449Z"),
        },
        {
            "run_transfer": {
                "amount": {
                    "currency": "USD",
                    "value": 1204,
                },
                "partner_account_id": "4a4599c7-ce94-437b-99e4-00834618798a",
                "source": {
                    "payment_method_id": "23d82d1a-696a-4ad4-9610-da4033b75dd5",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
                "destination": {
                    "payment_method_id": "b9944e28-5d4f-48b8-be2c-72f742c50066",
                    "ach_details": {
                        "company_entry_description": "Gym Dues",
                        "originating_company_name": "Whole Body Fit",
                    },
                    "card_details": {
                        "dynamic_descriptor": "WhlBdy *Yoga 11-12",
                    },
                },
            },
            "run_on": dateutil.parser.isoparse("2022-12-06T15:30:07.941Z"),
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
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the schedule                                                  | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `upsert_schedule`                                                   | [models.UpsertSchedule](../../models/upsertschedule.md)             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateScheduleResponse](../../models/updatescheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error1    | 400              | application/json |
| models.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_schedule

Disables a schedule and cancels all occurrences.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.cancel_schedule(account_id="a1303a1c-8708-447e-a64b-5dba8417b641", schedule_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the account.                                                  |                                                                     |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the schedule                                                  | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CancelScheduleResponse](../../models/cancelscheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_scheduled_occurrence

Gets a specific occurrence.

To use this endpoint from the browser, you'll need to specify the `/accounts/{your-account-id}/transfers.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


### Example Usage

```python
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.schedules.get_scheduled_occurrence(account_id="7175f455-a6d6-4b87-8e24-cbd12c7dabe7", schedule_id="ec7e1848-dc80-4ab0-8827-dd7fc0737b43", occurrence_filter="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                         | ID of the account.                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                            |
| `schedule_id`                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                         | ID of the schedule                                                                                                                                                                                                                                                                         | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                                                                                                                                                                                                                                       |
| `occurrence_filter`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                         | Allows the specification of additional filters beyond the UUID. <br/>- Specifying a UUID string returns the exact occurrence<br/>- Specifying a RFC 3339 timestamp returns the latest occurrence at or before that timestamp<br/>- Specifying 'latest' returns the latest occurrence at or before now<br/> |                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                            |

### Response

**[models.GetScheduledOccurrenceResponse](../../models/getscheduledoccurrenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |