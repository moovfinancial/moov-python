"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updatecolors import UpdateColors, UpdateColorsTypedDict
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UpdateBrandTypedDict(TypedDict):
    colors: NotRequired[UpdateColorsTypedDict]


class UpdateBrand(BaseModel):
    colors: Optional[UpdateColors] = None
