"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UserAccountTypedDict(TypedDict):
    r"""Information about an account the user has access to."""

    account_id: NotRequired[str]
    r"""ID of account."""
    display_name: NotRequired[str]
    r"""Descriptive name allowing spaces."""


class UserAccount(BaseModel):
    r"""Information about an account the user has access to."""

    account_id: Annotated[Optional[str], pydantic.Field(alias="accountID")] = None
    r"""ID of account."""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Descriptive name allowing spaces."""
