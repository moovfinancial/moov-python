"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cancellation import Cancellation, CancellationTypedDict
from moovio_sdk.types import BaseModel
from typing_extensions import TypedDict


class ReversedWithCancellationTypedDict(TypedDict):
    cancellation: CancellationTypedDict


class ReversedWithCancellation(BaseModel):
    cancellation: Cancellation
