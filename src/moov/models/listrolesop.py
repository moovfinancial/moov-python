"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .role import Role, RoleTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListRolesRequestTypedDict(TypedDict):
    x_account_id: NotRequired[str]
    r"""ID of the account."""


class ListRolesRequest(BaseModel):
    x_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Account-ID"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the account."""


ListRolesResponseResultTypedDict = Union[List[RoleTypedDict], str]


ListRolesResponseResult = Union[List[Role], str]


class ListRolesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListRolesResponseResultTypedDict


class ListRolesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListRolesResponseResult
