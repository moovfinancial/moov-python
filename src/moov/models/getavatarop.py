"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from .versions import Versions
import httpx
from moov.types import BaseModel
from moov.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    SecurityMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetAvatarSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class GetAvatarSecurity(BaseModel):
    basic_auth: Annotated[
        Optional[SchemeBasicAuth],
        FieldMetadata(
            security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="basic")
        ),
    ] = None

    o_auth2_auth: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True, scheme_type="oauth2", field_name="Authorization"
            )
        ),
    ] = None


class GetAvatarRequestTypedDict(TypedDict):
    unique_id: str
    r"""Any unique ID associated with an account such as accountID, representativeID, routing number, or userID."""
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""


class GetAvatarRequest(BaseModel):
    unique_id: Annotated[
        str,
        pydantic.Field(alias="uniqueID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Any unique ID associated with an account such as accountID, representativeID, routing number, or userID."""

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""


GetAvatarResponseTypedDict = TypeAliasType(
    "GetAvatarResponseTypedDict", Union[httpx.Response, httpx.Response]
)


GetAvatarResponse = TypeAliasType(
    "GetAvatarResponse", Union[httpx.Response, httpx.Response]
)
