"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billablefee import BillableFee, BillableFeeTypedDict
from .cardacquringmodel import CardAcquringModel
from .feeplanagreementstatus import FeePlanAgreementStatus
from datetime import datetime
from moovio_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PartnerPricingAgreementTypedDict(TypedDict):
    aggreement_id: str
    plan_id: str
    name: str
    r"""The name of the agreement."""
    accepted_on: datetime
    status: FeePlanAgreementStatus
    card_acquring_model: CardAcquringModel
    r"""Specifies the card processing pricing model"""
    billable_fees: List[BillableFeeTypedDict]
    revenue_share: int
    r"""The integer percentage value of the revenue split for partner."""
    account_id: NotRequired[str]
    description: NotRequired[str]
    r"""The description of the agreement."""


class PartnerPricingAgreement(BaseModel):
    aggreement_id: Annotated[str, pydantic.Field(alias="aggreementID")]

    plan_id: Annotated[str, pydantic.Field(alias="planID")]

    name: str
    r"""The name of the agreement."""

    accepted_on: Annotated[datetime, pydantic.Field(alias="acceptedOn")]

    status: FeePlanAgreementStatus

    card_acquring_model: Annotated[
        CardAcquringModel, pydantic.Field(alias="cardAcquringModel")
    ]
    r"""Specifies the card processing pricing model"""

    billable_fees: Annotated[List[BillableFee], pydantic.Field(alias="billableFees")]

    revenue_share: Annotated[int, pydantic.Field(alias="revenueShare")]
    r"""The integer percentage value of the revenue split for partner."""

    account_id: Annotated[Optional[str], pydantic.Field(alias="accountID")] = None

    description: Optional[str] = None
    r"""The description of the agreement."""
