"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class OccurrenceErrorTypedDict(TypedDict):
    r"""Contains details on why the occurrence errored"""

    message: NotRequired[str]


class OccurrenceError(BaseModel):
    r"""Contains details on why the occurrence errored"""

    message: Optional[str] = None