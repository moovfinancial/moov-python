"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sweepconfig import SweepConfig, SweepConfigTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetSweepConfigRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    sweep_config_id: str
    r"""ID of the sweep config"""


class GetSweepConfigRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    sweep_config_id: Annotated[
        str,
        pydantic.Field(alias="sweepConfigID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the sweep config"""


GetSweepConfigResponseResultTypedDict = Union[SweepConfigTypedDict, str]


GetSweepConfigResponseResult = Union[SweepConfig, str]


class GetSweepConfigResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetSweepConfigResponseResultTypedDict


class GetSweepConfigResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetSweepConfigResponseResult
