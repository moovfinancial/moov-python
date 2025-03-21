"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SsnTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class Ssn(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class ItinTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class Itin(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class GovernmentIDTypedDict(TypedDict):
    ssn: NotRequired[SsnTypedDict]
    itin: NotRequired[ItinTypedDict]


class GovernmentID(BaseModel):
    ssn: Optional[Ssn] = None

    itin: Optional[Itin] = None
