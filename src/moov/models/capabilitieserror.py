"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class CapabilitiesErrorTypedDict(TypedDict):
    capabilities: NotRequired[Dict[str, str]]


class CapabilitiesError(BaseModel):
    capabilities: Optional[Dict[str, str]] = None
