"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billablefee import BillableFee, BillableFeeTypedDict
from .cardacquiringmodel import CardAcquiringModel
from datetime import datetime
from moovio_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PartnerPricingTypedDict(TypedDict):
    plan_id: str
    name: str
    r"""The name of the fee plan."""
    revenue_share: int
    r"""The integer percentage value of the revenue split for partner."""
    card_acquiring_model: CardAcquiringModel
    r"""Specifies the card processing pricing model"""
    billable_fees: List[BillableFeeTypedDict]
    created_at: datetime
    description: NotRequired[str]
    r"""A description of the fee plan."""


class PartnerPricing(BaseModel):
    plan_id: Annotated[str, pydantic.Field(alias="planID")]

    name: str
    r"""The name of the fee plan."""

    revenue_share: Annotated[int, pydantic.Field(alias="revenueShare")]
    r"""The integer percentage value of the revenue split for partner."""

    card_acquiring_model: Annotated[
        CardAcquiringModel, pydantic.Field(alias="cardAcquiringModel")
    ]
    r"""Specifies the card processing pricing model"""

    billable_fees: Annotated[List[BillableFee], pydantic.Field(alias="billableFees")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    description: Optional[str] = None
    r"""A description of the fee plan."""
