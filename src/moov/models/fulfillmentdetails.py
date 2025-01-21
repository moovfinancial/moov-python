"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .returnpolicytype import ReturnPolicyType
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class FulfillmentDetailsTypedDict(TypedDict):
    has_physical_goods: bool
    is_shipping_product: bool
    shipment_duration_days: int
    return_policy: ReturnPolicyType


class FulfillmentDetails(BaseModel):
    has_physical_goods: Annotated[bool, pydantic.Field(alias="hasPhysicalGoods")]

    is_shipping_product: Annotated[bool, pydantic.Field(alias="isShippingProduct")]

    shipment_duration_days: Annotated[int, pydantic.Field(alias="shipmentDurationDays")]

    return_policy: Annotated[ReturnPolicyType, pydantic.Field(alias="returnPolicy")]
