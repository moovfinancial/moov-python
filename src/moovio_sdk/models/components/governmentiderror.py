"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GovernmentIDErrorSsnTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class GovernmentIDErrorSsn(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class GovernmentIDErrorItinTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class GovernmentIDErrorItin(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class GovernmentIDErrorTypedDict(TypedDict):
    ssn: NotRequired[GovernmentIDErrorSsnTypedDict]
    itin: NotRequired[GovernmentIDErrorItinTypedDict]


class GovernmentIDError(BaseModel):
    ssn: Optional[GovernmentIDErrorSsn] = None

    itin: Optional[GovernmentIDErrorItin] = None
