"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class End2EndEncryptionErrorTypedDict(TypedDict):
    token: NotRequired[str]


class End2EndEncryptionError(BaseModel):
    token: Optional[str] = None
