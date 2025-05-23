"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cancellationstatus import CancellationStatus
from moovio_sdk.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class WebhookDataCancellationUpdatedTypedDict(TypedDict):
    cancellation_id: str
    transfer_id: str
    status: CancellationStatus


class WebhookDataCancellationUpdated(BaseModel):
    cancellation_id: Annotated[str, pydantic.Field(alias="cancellationID")]

    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]

    status: CancellationStatus
