"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connection import Connection, ConnectionTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListConnectionsRequestTypedDict(TypedDict):
    x_account_id: NotRequired[str]
    r"""ID of the account."""


class ListConnectionsRequest(BaseModel):
    x_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Account-ID"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the account."""


ListConnectionsResponseResultTypedDict = Union[List[ConnectionTypedDict], str]


ListConnectionsResponseResult = Union[List[Connection], str]


class ListConnectionsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListConnectionsResponseResultTypedDict


class ListConnectionsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListConnectionsResponseResult
