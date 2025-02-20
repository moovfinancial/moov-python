"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GeneratedByTransferIDTypedDict(TypedDict):
    transfer_id: NotRequired[str]


class GeneratedByTransferID(BaseModel):
    transfer_id: Annotated[Optional[str], pydantic.Field(alias="transferID")] = None
