"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .qrcode import QRCode, QRCodeTypedDict
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


class GetPaymentLinkQRCodeSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class GetPaymentLinkQRCodeSecurity(BaseModel):
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


class GetPaymentLinkQRCodeRequestTypedDict(TypedDict):
    account_id: str
    payment_link_code: str
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""


class GetPaymentLinkQRCodeRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    payment_link_code: Annotated[
        str,
        pydantic.Field(alias="paymentLinkCode"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""


GetPaymentLinkQRCodeResponseTypedDict = TypeAliasType(
    "GetPaymentLinkQRCodeResponseTypedDict", Union[QRCodeTypedDict, httpx.Response]
)


GetPaymentLinkQRCodeResponse = TypeAliasType(
    "GetPaymentLinkQRCodeResponse", Union[QRCode, httpx.Response]
)
