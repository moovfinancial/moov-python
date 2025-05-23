"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PayoutRecipientErrorTypedDict(TypedDict):
    email: NotRequired[str]


class PayoutRecipientError(BaseModel):
    email: Optional[str] = None
