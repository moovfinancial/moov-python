"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .scheduledachdetails import ScheduledAchDetails, ScheduledAchDetailsTypedDict
from .scheduledcarddetails import ScheduledCardDetails, ScheduledCardDetailsTypedDict
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class ScheduledPaymentMethodTypedDict(TypedDict):
    r"""Defines a payment method to use for the scheduled transfer"""

    payment_method_id: str
    r"""ID of the payment method to use."""
    ach_details: NotRequired[Nullable[ScheduledAchDetailsTypedDict]]
    card_details: NotRequired[Nullable[ScheduledCardDetailsTypedDict]]


class ScheduledPaymentMethod(BaseModel):
    r"""Defines a payment method to use for the scheduled transfer"""

    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method to use."""

    ach_details: Annotated[
        OptionalNullable[ScheduledAchDetails], pydantic.Field(alias="achDetails")
    ] = UNSET

    card_details: Annotated[
        OptionalNullable[ScheduledCardDetails], pydantic.Field(alias="cardDetails")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["achDetails", "cardDetails"]
        nullable_fields = ["achDetails", "cardDetails"]
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
