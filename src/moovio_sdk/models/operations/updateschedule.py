"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.models.components import (
    scheduleresponse as components_scheduleresponse,
    upsertschedule as components_upsertschedule,
)
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateScheduleGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class UpdateScheduleGlobals(BaseModel):
    x_moov_version: Annotated[
        Optional[str],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = "v2024.01.00"
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class UpdateScheduleRequestTypedDict(TypedDict):
    account_id: str
    schedule_id: str
    upsert_schedule: components_upsertschedule.UpsertScheduleTypedDict


class UpdateScheduleRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    schedule_id: Annotated[
        str,
        pydantic.Field(alias="scheduleID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    upsert_schedule: Annotated[
        components_upsertschedule.UpsertSchedule,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateScheduleResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: components_scheduleresponse.ScheduleResponseTypedDict


class UpdateScheduleResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_scheduleresponse.ScheduleResponse
