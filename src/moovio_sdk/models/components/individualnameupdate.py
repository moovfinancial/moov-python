"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IndividualNameUpdateTypedDict(TypedDict):
    first_name: NotRequired[str]
    r"""The individual's first given name."""
    middle_name: NotRequired[str]
    r"""The individual's second given name, if any."""
    last_name: NotRequired[str]
    r"""The individual's family name."""
    suffix: NotRequired[str]
    r"""Suffix of a given name."""


class IndividualNameUpdate(BaseModel):
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    r"""The individual's first given name."""

    middle_name: Annotated[Optional[str], pydantic.Field(alias="middleName")] = None
    r"""The individual's second given name, if any."""

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    r"""The individual's family name."""

    suffix: Optional[str] = None
    r"""Suffix of a given name."""
