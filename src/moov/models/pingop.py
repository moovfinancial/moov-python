"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class PingResponse1TypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: str


class PingResponse1(BaseModel):
    headers: Dict[str, List[str]]

    result: str