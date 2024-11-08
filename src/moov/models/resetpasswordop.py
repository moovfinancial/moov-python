"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Dict, List, Union
from typing_extensions import TypedDict


ResetPasswordResponseResultTypedDict = Union[str, str]


ResetPasswordResponseResult = Union[str, str]


class ResetPasswordResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ResetPasswordResponseResultTypedDict


class ResetPasswordResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ResetPasswordResponseResult
