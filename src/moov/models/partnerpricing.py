"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fee import Fee, FeeTypedDict
from datetime import datetime
from enum import Enum
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class PartnerPricingCardAcquiringModel(str, Enum):
    r"""Specifies the card processing pricing model"""

    COST_PLUS = "cost-plus"
    FLAT_RATE = "flat-rate"


class PartnerPricingTypedDict(TypedDict):
    plan_id: str
    r"""UUID v4"""
    name: str
    r"""The name of the plan."""
    revenue_share: int
    r"""The integer percentage value of the revenue split for partner."""
    card_acquiring_model: PartnerPricingCardAcquiringModel
    created_at: datetime
    billable_fees: List[FeeTypedDict]
    r"""Additional usage-based fees for this plan."""
    description: NotRequired[Nullable[str]]
    r"""The description on the plan."""


class PartnerPricing(BaseModel):
    plan_id: Annotated[str, pydantic.Field(alias="planID")]
    r"""UUID v4"""

    name: str
    r"""The name of the plan."""

    revenue_share: Annotated[int, pydantic.Field(alias="revenueShare")]
    r"""The integer percentage value of the revenue split for partner."""

    card_acquiring_model: Annotated[
        PartnerPricingCardAcquiringModel, pydantic.Field(alias="cardAcquiringModel")
    ]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    billable_fees: Annotated[List[Fee], pydantic.Field(alias="billableFees")]
    r"""Additional usage-based fees for this plan."""

    description: OptionalNullable[str] = UNSET
    r"""The description on the plan."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description"]
        nullable_fields = ["description"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m