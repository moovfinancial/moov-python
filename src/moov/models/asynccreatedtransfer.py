"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class AsyncCreatedTransferTypedDict(TypedDict):
    transfer_id: str
    r"""Identifier for the transfer."""
    created_on: datetime


class AsyncCreatedTransfer(BaseModel):
    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]
    r"""Identifier for the transfer."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]