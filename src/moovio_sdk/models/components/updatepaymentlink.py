"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amountupdate import AmountUpdate, AmountUpdateTypedDict
from .paymentlinkcustomeroptions import (
    PaymentLinkCustomerOptions,
    PaymentLinkCustomerOptionsTypedDict,
)
from .paymentlinkdisplayoptionsupdate import (
    PaymentLinkDisplayOptionsUpdate,
    PaymentLinkDisplayOptionsUpdateTypedDict,
)
from .paymentlinkpaymentdetailsupdate import (
    PaymentLinkPaymentDetailsUpdate,
    PaymentLinkPaymentDetailsUpdateTypedDict,
)
from .paymentlinkpayoutdetailsupdate import (
    PaymentLinkPayoutDetailsUpdate,
    PaymentLinkPayoutDetailsUpdateTypedDict,
)
from datetime import datetime
from moovio_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdatePaymentLinkTypedDict(TypedDict):
    amount: NotRequired[AmountUpdateTypedDict]
    expires_on: NotRequired[Nullable[datetime]]
    display: NotRequired[PaymentLinkDisplayOptionsUpdateTypedDict]
    r"""Customizable display options for a payment link."""
    customer: NotRequired[PaymentLinkCustomerOptionsTypedDict]
    payment: NotRequired[PaymentLinkPaymentDetailsUpdateTypedDict]
    r"""Options for payment links used to collect payment."""
    payout: NotRequired[PaymentLinkPayoutDetailsUpdateTypedDict]


class UpdatePaymentLink(BaseModel):
    amount: Optional[AmountUpdate] = None

    expires_on: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="expiresOn")
    ] = UNSET

    display: Optional[PaymentLinkDisplayOptionsUpdate] = None
    r"""Customizable display options for a payment link."""

    customer: Optional[PaymentLinkCustomerOptions] = None

    payment: Optional[PaymentLinkPaymentDetailsUpdate] = None
    r"""Options for payment links used to collect payment."""

    payout: Optional[PaymentLinkPayoutDetailsUpdate] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "amount",
            "expiresOn",
            "display",
            "customer",
            "payment",
            "payout",
        ]
        nullable_fields = ["expiresOn"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
