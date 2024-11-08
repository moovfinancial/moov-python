"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetAvatarRequestTypedDict(TypedDict):
    unique_id: str
    r"""Any unique ID associated with an account such as accountID, representativeID, routing number, or userID."""


class GetAvatarRequest(BaseModel):
    unique_id: Annotated[
        str,
        pydantic.Field(alias="uniqueID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Any unique ID associated with an account such as accountID, representativeID, routing number, or userID."""


GetAvatarResponseResultTypedDict = Union[httpx.Response, str]


GetAvatarResponseResult = Union[httpx.Response, str]


class GetAvatarResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetAvatarResponseResultTypedDict


class GetAvatarResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetAvatarResponseResult
