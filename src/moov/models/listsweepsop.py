"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from .sweepstatus import SweepStatus
from .versions import Versions
from moov.types import BaseModel
from moov.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    SecurityMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListSweepsSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class ListSweepsSecurity(BaseModel):
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


class ListSweepsRequestTypedDict(TypedDict):
    account_id: str
    wallet_id: str
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""
    skip: NotRequired[int]
    count: NotRequired[int]
    status: NotRequired[SweepStatus]
    r"""Optional parameter to filter by sweep status."""
    statement_descriptor: NotRequired[str]
    r"""Optional string to filter by statement descriptor."""


class ListSweepsRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    wallet_id: Annotated[
        str,
        pydantic.Field(alias="walletID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""

    skip: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None

    count: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None

    status: Annotated[
        Optional[SweepStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional parameter to filter by sweep status."""

    statement_descriptor: Annotated[
        Optional[str],
        pydantic.Field(alias="statementDescriptor"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional string to filter by statement descriptor."""
