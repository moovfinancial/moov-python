"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from .versions import Versions
from moov.types import BaseModel
from moov.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    SecurityMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetScheduledOccurrenceSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class GetScheduledOccurrenceSecurity(BaseModel):
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


class GetScheduledOccurrenceRequestTypedDict(TypedDict):
    account_id: str
    schedule_id: str
    occurrence_filter: str
    r"""Allows the specification of additional filters beyond the UUID.

    Specifying a UUID string returns the exact occurrence.
    Specifying a RFC 3339 timestamp returns the latest occurrence at or before that timestamp.
    Specifying `latest` returns the latest occurrence at or before now.
    """
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""


class GetScheduledOccurrenceRequest(BaseModel):
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

    occurrence_filter: Annotated[
        str,
        pydantic.Field(alias="occurrenceFilter"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Allows the specification of additional filters beyond the UUID.

    Specifying a UUID string returns the exact occurrence.
    Specifying a RFC 3339 timestamp returns the latest occurrence at or before that timestamp.
    Specifying `latest` returns the latest occurrence at or before now.
    """

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""
