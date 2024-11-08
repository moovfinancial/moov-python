"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .createachdetailsbase import CreateACHDetailsBase, CreateACHDetailsBaseTypedDict
from .createcarddetailsdestination import (
    CreateCardDetailsDestination,
    CreateCardDetailsDestinationTypedDict,
)
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class CheckoutTransferOptionsDestinationTypedDict(TypedDict):
    payment_method_id: str
    r"""UUID v4"""
    card_details: NotRequired[Nullable[CreateCardDetailsDestinationTypedDict]]
    ach_details: NotRequired[Nullable[CreateACHDetailsBaseTypedDict]]
    r"""If transfer involves ACH, override default card acceptance properties."""


class CheckoutTransferOptionsDestination(BaseModel):
    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""UUID v4"""

    card_details: Annotated[
        OptionalNullable[CreateCardDetailsDestination],
        pydantic.Field(alias="cardDetails"),
    ] = UNSET

    ach_details: Annotated[
        OptionalNullable[CreateACHDetailsBase], pydantic.Field(alias="achDetails")
    ] = UNSET
    r"""If transfer involves ACH, override default card acceptance properties."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cardDetails", "achDetails"]
        nullable_fields = ["cardDetails", "achDetails"]
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


class CheckoutTransferOptionsTypedDict(TypedDict):
    destination: CheckoutTransferOptionsDestinationTypedDict
    amount: AmountTypedDict
    r"""An integer value representing money in a specific currency."""


class CheckoutTransferOptions(BaseModel):
    destination: CheckoutTransferOptionsDestination

    amount: Amount
    r"""An integer value representing money in a specific currency."""
