"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DeviceInfoTypedDict(TypedDict):
    r"""Current device information"""

    fingerprint: NotRequired[str]
    r"""Device hash generated by a frontend library."""


class DeviceInfo(BaseModel):
    r"""Current device information"""

    fingerprint: Optional[str] = None
    r"""Device hash generated by a frontend library."""