"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FulfillmentDetailsErrorTypedDict(TypedDict):
    shipment_duration_days: NotRequired[str]
    return_policy: NotRequired[str]


class FulfillmentDetailsError(BaseModel):
    shipment_duration_days: Annotated[
        Optional[str], pydantic.Field(alias="shipmentDurationDays")
    ] = None

    return_policy: Annotated[Optional[str], pydantic.Field(alias="returnPolicy")] = None
