"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .refundcarddetails import RefundCardDetails, RefundCardDetailsTypedDict
from .refundstatus import RefundStatus
from datetime import datetime
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import ConfigDict, model_serializer
from typing import Any, Dict, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class SynchronousRefundResponseTypedDict(TypedDict):
    r"""Details of a card refund."""

    refund_id: str
    r"""UUID v4"""
    created_on: datetime
    updated_on: datetime
    status: RefundStatus
    amount: AmountTypedDict
    r"""An integer value representing money in a specific currency."""
    card_details: NotRequired[Nullable[RefundCardDetailsTypedDict]]


class SynchronousRefundResponse(BaseModel):
    r"""Details of a card refund."""

    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    refund_id: Annotated[str, pydantic.Field(alias="refundID")]
    r"""UUID v4"""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    updated_on: Annotated[datetime, pydantic.Field(alias="updatedOn")]

    status: RefundStatus

    amount: Amount
    r"""An integer value representing money in a specific currency."""

    card_details: Annotated[
        OptionalNullable[RefundCardDetails], pydantic.Field(alias="cardDetails")
    ] = UNSET

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cardDetails"]
        nullable_fields = ["cardDetails"]
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

        for k, v in serialized.items():
            m[k] = v

        return m


class AsynchronousRefundResponseTypedDict(TypedDict):
    refund_id: str
    r"""UUID v4"""
    created_on: datetime
    amount: AmountTypedDict
    r"""An integer value representing money in a specific currency."""


class AsynchronousRefundResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    refund_id: Annotated[str, pydantic.Field(alias="refundID")]
    r"""UUID v4"""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    amount: Amount
    r"""An integer value representing money in a specific currency."""

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]


RefundPostResponseTypedDict = Union[
    AsynchronousRefundResponseTypedDict, SynchronousRefundResponseTypedDict
]


RefundPostResponse = Union[AsynchronousRefundResponse, SynchronousRefundResponse]
