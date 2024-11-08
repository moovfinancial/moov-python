"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .patchrepresentativerequest import (
    PatchRepresentativeRequest,
    PatchRepresentativeRequestTypedDict,
)
from .representative import Representative, RepresentativeTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class PatchRepresentativeRequest1TypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    representative_id: str
    r"""ID of the representative."""
    patch_representative_request: PatchRepresentativeRequestTypedDict


class PatchRepresentativeRequest1(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    representative_id: Annotated[
        str,
        pydantic.Field(alias="representativeID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the representative."""

    patch_representative_request: Annotated[
        PatchRepresentativeRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


PatchRepresentativeResponseResultTypedDict = Union[RepresentativeTypedDict, str]


PatchRepresentativeResponseResult = Union[Representative, str]


class PatchRepresentativeResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: PatchRepresentativeResponseResultTypedDict


class PatchRepresentativeResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: PatchRepresentativeResponseResult
