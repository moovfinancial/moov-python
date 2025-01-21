"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billablefee import BillableFee, BillableFeeTypedDict
from .cardacquringmodel import CardAcquringModel
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FeePlanTypedDict(TypedDict):
    plan_id: str
    name: str
    r"""The name of the fee plan."""
    card_acquring_model: CardAcquringModel
    r"""Specifies the card processing pricing model"""
    billable_fees: List[BillableFeeTypedDict]
    r"""Additional usage-based fees for this plan."""
    created_at: datetime
    description: NotRequired[str]
    r"""A description of the fee plan."""


class FeePlan(BaseModel):
    plan_id: Annotated[str, pydantic.Field(alias="planID")]

    name: str
    r"""The name of the fee plan."""

    card_acquring_model: Annotated[
        CardAcquringModel, pydantic.Field(alias="cardAcquringModel")
    ]
    r"""Specifies the card processing pricing model"""

    billable_fees: Annotated[List[BillableFee], pydantic.Field(alias="billableFees")]
    r"""Additional usage-based fees for this plan."""

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    description: Optional[str] = None
    r"""A description of the fee plan."""
