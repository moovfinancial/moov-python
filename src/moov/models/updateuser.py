"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateUserTypedDict(TypedDict):
    r"""Properties to update a User"""

    given_name: NotRequired[str]
    r"""Name this person was given. This is usually the same as first name."""
    family_name: NotRequired[str]
    r"""Family name of this person. This is usually the same as last name."""


class UpdateUser(BaseModel):
    r"""Properties to update a User"""

    given_name: Annotated[Optional[str], pydantic.Field(alias="givenName")] = None
    r"""Name this person was given. This is usually the same as first name."""

    family_name: Annotated[Optional[str], pydantic.Field(alias="familyName")] = None
    r"""Family name of this person. This is usually the same as last name."""