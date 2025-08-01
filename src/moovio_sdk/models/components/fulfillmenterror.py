"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FulfillmentErrorTypedDict(TypedDict):
    method: NotRequired[str]
    timeframe: NotRequired[str]


class FulfillmentError(BaseModel):
    method: Optional[str] = None

    timeframe: Optional[str] = None
