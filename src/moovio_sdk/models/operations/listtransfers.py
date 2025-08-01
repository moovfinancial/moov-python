"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from moovio_sdk.models.components import (
    transfer as components_transfer,
    transferstatus as components_transferstatus,
)
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListTransfersGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class ListTransfersGlobals(BaseModel):
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


class ListTransfersRequestTypedDict(TypedDict):
    account_id: str
    account_i_ds: NotRequired[List[str]]
    r"""Optional, comma-separated account IDs by which the response is filtered based on whether the account ID is the source or destination."""
    status: NotRequired[components_transferstatus.TransferStatus]
    r"""Optional parameter for filtering transfers by status."""
    start_date_time: NotRequired[datetime]
    r"""Optional date-time which inclusively filters all transfers created after this date-time."""
    end_date_time: NotRequired[datetime]
    r"""Optional date-time which exclusively filters all transfers created before this date-time."""
    group_id: NotRequired[str]
    r"""Optional ID to filter for transfers in the same group."""
    schedule_id: NotRequired[str]
    r"""Optional ID to filter for transfer occurrences belonging to the same schedule."""
    payment_link_code: NotRequired[str]
    r"""Optional code to filter for transfers associated with the payment link."""
    refunded: NotRequired[bool]
    r"""Optional parameter to only return refunded transfers."""
    disputed: NotRequired[bool]
    r"""Optional parameter to only return disputed transfers."""
    foreign_id: NotRequired[str]
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""
    skip: NotRequired[int]
    count: NotRequired[int]


class ListTransfersRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    account_i_ds: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="accountIDs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional, comma-separated account IDs by which the response is filtered based on whether the account ID is the source or destination."""

    status: Annotated[
        Optional[components_transferstatus.TransferStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional parameter for filtering transfers by status."""

    start_date_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="startDateTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional date-time which inclusively filters all transfers created after this date-time."""

    end_date_time: Annotated[
        Optional[datetime],
        pydantic.Field(alias="endDateTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional date-time which exclusively filters all transfers created before this date-time."""

    group_id: Annotated[
        Optional[str],
        pydantic.Field(alias="groupID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional ID to filter for transfers in the same group."""

    schedule_id: Annotated[
        Optional[str],
        pydantic.Field(alias="scheduleID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional ID to filter for transfer occurrences belonging to the same schedule."""

    payment_link_code: Annotated[
        Optional[str],
        pydantic.Field(alias="paymentLinkCode"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional code to filter for transfers associated with the payment link."""

    refunded: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional parameter to only return refunded transfers."""

    disputed: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional parameter to only return disputed transfers."""

    foreign_id: Annotated[
        Optional[str],
        pydantic.Field(alias="foreignID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""

    skip: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None

    count: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None


class ListTransfersResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[components_transfer.TransferTypedDict]


class ListTransfersResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[components_transfer.Transfer]
