"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UserInviteTypedDict(TypedDict):
    r"""Information about an invitation sent to the user"""

    invite_id: NotRequired[str]
    r"""UUID v4"""
    account_id: NotRequired[str]
    r"""ID of account."""
    display_name: NotRequired[str]
    r"""Descriptive name allowing spaces."""
    email: NotRequired[str]
    r"""Email address."""
    expires_on: NotRequired[datetime]


class UserInvite(BaseModel):
    r"""Information about an invitation sent to the user"""

    invite_id: Annotated[Optional[str], pydantic.Field(alias="inviteID")] = None
    r"""UUID v4"""

    account_id: Annotated[Optional[str], pydantic.Field(alias="accountID")] = None
    r"""ID of account."""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Descriptive name allowing spaces."""

    email: Optional[str] = None
    r"""Email address."""

    expires_on: Annotated[Optional[datetime], pydantic.Field(alias="expiresOn")] = None