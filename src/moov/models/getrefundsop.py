"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getrefund import GetRefund, GetRefundTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class GetRefundsRequestTypedDict(TypedDict):
    transfer_id: str
    r"""Identifier for the transfer."""
    account_id: NotRequired[str]
    r"""Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account."""


class GetRefundsRequest(BaseModel):
    transfer_id: Annotated[
        str,
        pydantic.Field(alias="transferID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Identifier for the transfer."""

    account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="accountID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Identifier for a connected account. Must be provided when using a token and the value of `{accountID}` in the scopes is a connected account."""


GetRefundsResponseResultTypedDict = Union[List[GetRefundTypedDict], str]


GetRefundsResponseResult = Union[List[GetRefund], str]


class GetRefundsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetRefundsResponseResultTypedDict


class GetRefundsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetRefundsResponseResult
