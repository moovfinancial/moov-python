"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing_extensions import TypedDict


class BirthDateTypedDict(TypedDict):
    day: int
    month: int
    year: int


class BirthDate(BaseModel):
    day: int

    month: int

    year: int
