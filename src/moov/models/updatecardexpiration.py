"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UpdateCardExpirationTypedDict(TypedDict):
    month: NotRequired[str]
    year: NotRequired[str]


class UpdateCardExpiration(BaseModel):
    month: Optional[str] = None

    year: Optional[str] = None
