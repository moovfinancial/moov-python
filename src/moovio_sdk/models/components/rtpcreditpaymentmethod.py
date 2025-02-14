"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentmethodsbankaccount import (
    PaymentMethodsBankAccount,
    PaymentMethodsBankAccountTypedDict,
)
from enum import Enum
from moovio_sdk.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class RtpCreditPaymentMethodPaymentMethodType(str, Enum):
    RTP_CREDIT = "rtp-credit"


class RtpCreditPaymentMethodTypedDict(TypedDict):
    payment_method_id: str
    r"""ID of the payment method."""
    payment_method_type: RtpCreditPaymentMethodPaymentMethodType
    bank_account: PaymentMethodsBankAccountTypedDict
    r"""A bank account as contained within a payment method."""


class RtpCreditPaymentMethod(BaseModel):
    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method."""

    payment_method_type: Annotated[
        RtpCreditPaymentMethodPaymentMethodType,
        pydantic.Field(alias="paymentMethodType"),
    ]

    bank_account: Annotated[
        PaymentMethodsBankAccount, pydantic.Field(alias="bankAccount")
    ]
    r"""A bank account as contained within a payment method."""
