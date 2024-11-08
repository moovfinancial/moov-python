"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .qrcoderesponse import QRCodeResponse, QRCodeResponseTypedDict
import httpx
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetCheckoutQRCodeRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    checkout_code: str
    r"""Unique code of the checkout."""


class GetCheckoutQRCodeRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    checkout_code: Annotated[
        str,
        pydantic.Field(alias="checkoutCode"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique code of the checkout."""


GetCheckoutQRCodeResponseResultTypedDict = Union[
    QRCodeResponseTypedDict, httpx.Response, str
]


GetCheckoutQRCodeResponseResult = Union[QRCodeResponse, httpx.Response, str]


class GetCheckoutQRCodeResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetCheckoutQRCodeResponseResultTypedDict


class GetCheckoutQRCodeResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetCheckoutQRCodeResponseResult
