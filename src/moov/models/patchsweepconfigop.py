"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .patchsweepconfig import PatchSweepConfig, PatchSweepConfigTypedDict
from .sweepconfig import SweepConfig, SweepConfigTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class PatchSweepConfigRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    sweep_config_id: str
    r"""ID of the sweep config"""
    patch_sweep_config: PatchSweepConfigTypedDict


class PatchSweepConfigRequest(BaseModel):
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

    patch_sweep_config: Annotated[
        PatchSweepConfig,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


PatchSweepConfigResponseResultTypedDict = Union[SweepConfigTypedDict, str]


PatchSweepConfigResponseResult = Union[SweepConfig, str]


class PatchSweepConfigResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: PatchSweepConfigResponseResultTypedDict


class PatchSweepConfigResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: PatchSweepConfigResponseResult