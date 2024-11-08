"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .createachdetailsbase import CreateACHDetailsBase, CreateACHDetailsBaseTypedDict
from .createachdetailssource import (
    CreateAchDetailsSource,
    CreateAchDetailsSourceTypedDict,
)
from .createcarddetailsdestination import (
    CreateCardDetailsDestination,
    CreateCardDetailsDestinationTypedDict,
)
from .createcarddetailssource import (
    CreateCardDetailsSource,
    CreateCardDetailsSourceTypedDict,
)
from .createfacilitatorfee import CreateFacilitatorFee, CreateFacilitatorFeeTypedDict
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SourceTypedDict(TypedDict):
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`. A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/), associating the new transfer with a parent transfer."""

    transfer_id: str
    r"""UUID v4"""
    payment_method_id: str
    r"""UUID v4"""
    card_details: NotRequired[Nullable[CreateCardDetailsSourceTypedDict]]
    ach_details: NotRequired[Nullable[CreateAchDetailsSourceTypedDict]]


class Source(BaseModel):
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`. A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/), associating the new transfer with a parent transfer."""

    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]
    r"""UUID v4"""

    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""UUID v4"""

    card_details: Annotated[
        OptionalNullable[CreateCardDetailsSource], pydantic.Field(alias="cardDetails")
    ] = UNSET

    ach_details: Annotated[
        OptionalNullable[CreateAchDetailsSource], pydantic.Field(alias="achDetails")
    ] = UNSET

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


class DestinationTypedDict(TypedDict):
    r"""The final stage of a transfer and the ultimate recipient of the funds."""

    payment_method_id: str
    r"""UUID v4"""
    card_details: NotRequired[Nullable[CreateCardDetailsDestinationTypedDict]]
    ach_details: NotRequired[Nullable[CreateACHDetailsBaseTypedDict]]
    r"""If transfer involves ACH, override default card acceptance properties."""


class Destination(BaseModel):
    r"""The final stage of a transfer and the ultimate recipient of the funds."""

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


class CreateTransferTypedDict(TypedDict):
    source: SourceTypedDict
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`. A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/), associating the new transfer with a parent transfer."""
    destination: DestinationTypedDict
    r"""The final stage of a transfer and the ultimate recipient of the funds."""
    amount: AmountTypedDict
    r"""An integer value representing money in a specific currency."""
    facilitator_fee: NotRequired[CreateFacilitatorFeeTypedDict]
    r"""Total or markup fee."""
    description: NotRequired[str]
    r"""An optional description of the transfer for your own internal use."""
    metadata: NotRequired[Dict[str, str]]
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""


class CreateTransfer(BaseModel):
    source: Source
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`. A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/), associating the new transfer with a parent transfer."""

    destination: Destination
    r"""The final stage of a transfer and the ultimate recipient of the funds."""

    amount: Amount
    r"""An integer value representing money in a specific currency."""

    facilitator_fee: Annotated[
        Optional[CreateFacilitatorFee], pydantic.Field(alias="facilitatorFee")
    ] = None
    r"""Total or markup fee."""

    description: Optional[str] = None
    r"""An optional description of the transfer for your own internal use."""

    metadata: Optional[Dict[str, str]] = None
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""
