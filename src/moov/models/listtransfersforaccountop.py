"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transfer1 import Transfer3, Transfer3TypedDict
from .transferstatus import TransferStatus
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListTransfersForAccountRequestTypedDict(TypedDict):
    account_id: str
    r"""Identifier for an account."""
    status: NotRequired[TransferStatus]
    r"""Optional parameter for filtering transfers by status."""
    start_date_time: NotRequired[str]
    r"""Optional date-time which inclusively filters all transfers created after this date-time."""
    end_date_time: NotRequired[str]
    r"""Optional date-time which exclusively filters all transfers created before this date-time."""
    group_id: NotRequired[str]
    r"""Optional ID to filter for transfers in the same group."""
    count: NotRequired[int]
    r"""Optional parameter to limit the number of results in the query."""
    skip: NotRequired[int]
    r"""The number of items to offset before starting to collect the result set."""
    refunded: NotRequired[bool]
    r"""Optional parameter to only return refunded transfers."""
    disputed: NotRequired[bool]
    r"""Optional parameter to only return disputed transfers."""


class ListTransfersForAccountRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Identifier for an account."""

    status: Annotated[
        Optional[TransferStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional parameter for filtering transfers by status."""

    start_date_time: Annotated[
        Optional[str],
        pydantic.Field(alias="startDateTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional date-time which inclusively filters all transfers created after this date-time."""

    end_date_time: Annotated[
        Optional[str],
        pydantic.Field(alias="endDateTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional date-time which exclusively filters all transfers created before this date-time."""

    group_id: Annotated[
        Optional[str],
        pydantic.Field(alias="groupID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional ID to filter for transfers in the same group."""

    count: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 200
    r"""Optional parameter to limit the number of results in the query."""

    skip: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of items to offset before starting to collect the result set."""

    refunded: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional parameter to only return refunded transfers."""

    disputed: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional parameter to only return disputed transfers."""


ListTransfersForAccountResponseResultTypedDict = Union[List[Transfer3TypedDict], str]


ListTransfersForAccountResponseResult = Union[List[Transfer3], str]


class ListTransfersForAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListTransfersForAccountResponseResultTypedDict


class ListTransfersForAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListTransfersForAccountResponseResult