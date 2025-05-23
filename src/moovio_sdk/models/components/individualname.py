"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IndividualNameTypedDict(TypedDict):
    first_name: str
    r"""The individual's first given name."""
    last_name: str
    r"""The individual's family name."""
    middle_name: NotRequired[str]
    r"""The individual's second given name, if any."""
    suffix: NotRequired[str]
    r"""Suffix of a given name."""


class IndividualName(BaseModel):
    first_name: Annotated[str, pydantic.Field(alias="firstName")]
    r"""The individual's first given name."""

    last_name: Annotated[str, pydantic.Field(alias="lastName")]
    r"""The individual's family name."""

    middle_name: Annotated[Optional[str], pydantic.Field(alias="middleName")] = None
    r"""The individual's second given name, if any."""

    suffix: Optional[str] = None
    r"""Suffix of a given name."""
