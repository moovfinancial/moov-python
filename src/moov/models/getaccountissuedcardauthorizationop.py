"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .issuedcardauthorization import (
    IssuedCardAuthorization,
    IssuedCardAuthorizationTypedDict,
)
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetAccountIssuedCardAuthorizationRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    authorization_id: str
    r"""ID of the authorization."""


class GetAccountIssuedCardAuthorizationRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    authorization_id: Annotated[
        str,
        pydantic.Field(alias="authorizationID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the authorization."""


GetAccountIssuedCardAuthorizationResponseResultTypedDict = Union[
    IssuedCardAuthorizationTypedDict, str
]


GetAccountIssuedCardAuthorizationResponseResult = Union[IssuedCardAuthorization, str]


class GetAccountIssuedCardAuthorizationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetAccountIssuedCardAuthorizationResponseResultTypedDict


class GetAccountIssuedCardAuthorizationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetAccountIssuedCardAuthorizationResponseResult
