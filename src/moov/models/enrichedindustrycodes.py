"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EnrichedIndustryCodesTypedDict(TypedDict):
    r"""Describes industry specific identifiers"""

    naics: NotRequired[str]
    sic: NotRequired[str]


class EnrichedIndustryCodes(BaseModel):
    r"""Describes industry specific identifiers"""

    naics: Optional[str] = None

    sic: Optional[str] = None