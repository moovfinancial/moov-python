"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from .updateapplepaymerchantdomains import (
    UpdateApplePayMerchantDomains,
    UpdateApplePayMerchantDomainsTypedDict,
)
from .versions import Versions
from moov.types import BaseModel
from moov.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateApplePayMerchantDomainsSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class UpdateApplePayMerchantDomainsSecurity(BaseModel):
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


class UpdateApplePayMerchantDomainsRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the Moov account representing the merchant."""
    update_apple_pay_merchant_domains: UpdateApplePayMerchantDomainsTypedDict
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""


class UpdateApplePayMerchantDomainsRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the Moov account representing the merchant."""

    update_apple_pay_merchant_domains: Annotated[
        UpdateApplePayMerchantDomains,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""
