"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DisableRoleRequestTypedDict(TypedDict):
    role_id: str
    r"""ID of the role to update"""
    x_account_id: NotRequired[str]
    r"""ID of the account."""


class DisableRoleRequest(BaseModel):
    role_id: Annotated[
        str,
        pydantic.Field(alias="roleID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the role to update"""

    x_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Account-ID"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the account."""


class DisableRoleResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: str


class DisableRoleResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: str
