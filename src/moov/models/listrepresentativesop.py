"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .representative import Representative, RepresentativeTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class ListRepresentativesRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""


class ListRepresentativesRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""


ListRepresentativesResponseResultTypedDict = Union[List[RepresentativeTypedDict], str]


ListRepresentativesResponseResult = Union[List[Representative], str]


class ListRepresentativesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListRepresentativesResponseResultTypedDict


class ListRepresentativesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListRepresentativesResponseResult
