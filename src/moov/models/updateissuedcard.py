"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createauthorizeduser import CreateAuthorizedUser, CreateAuthorizedUserTypedDict
from .updateissuedcardstate import UpdateIssuedCardState
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateIssuedCardTypedDict(TypedDict):
    state: NotRequired[UpdateIssuedCardState]
    r"""Updates the state of a Moov issued card. Currently only supports the closed state."""
    memo: NotRequired[str]
    r"""Optional descriptive name."""
    authorized_user: NotRequired[CreateAuthorizedUserTypedDict]
    r"""Fields for identifying an authorized individual."""


class UpdateIssuedCard(BaseModel):
    state: Optional[UpdateIssuedCardState] = None
    r"""Updates the state of a Moov issued card. Currently only supports the closed state."""

    memo: Optional[str] = None
    r"""Optional descriptive name."""

    authorized_user: Annotated[
        Optional[CreateAuthorizedUser], pydantic.Field(alias="authorizedUser")
    ] = None
    r"""Fields for identifying an authorized individual."""
