"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UpdateColorTypedDict(TypedDict):
    accent: NotRequired[str]


class UpdateColor(BaseModel):
    accent: Optional[str] = None
