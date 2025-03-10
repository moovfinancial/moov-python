"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payoutrecipienterror import PayoutRecipientError, PayoutRecipientErrorTypedDict
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PayoutDetailsErrorTypedDict(TypedDict):
    allowed_methods: NotRequired[str]
    recipient: NotRequired[PayoutRecipientErrorTypedDict]


class PayoutDetailsError(BaseModel):
    allowed_methods: Annotated[
        Optional[str], pydantic.Field(alias="allowedMethods")
    ] = None

    recipient: Optional[PayoutRecipientError] = None
