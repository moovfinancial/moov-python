"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .useraccount import UserAccount, UserAccountTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class GetUserAccountsRequestTypedDict(TypedDict):
    user_id: str
    r"""UserID of the user to load"""
    x_account_id: NotRequired[str]
    r"""ID of the account."""


class GetUserAccountsRequest(BaseModel):
    user_id: Annotated[
        str,
        pydantic.Field(alias="userID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""UserID of the user to load"""

    x_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Account-ID"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the account."""


GetUserAccountsResponseResultTypedDict = Union[List[UserAccountTypedDict], str]


GetUserAccountsResponseResult = Union[List[UserAccount], str]


class GetUserAccountsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetUserAccountsResponseResultTypedDict


class GetUserAccountsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetUserAccountsResponseResult
