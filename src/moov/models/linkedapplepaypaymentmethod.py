"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applepayresponse import ApplePayResponse, ApplePayResponseTypedDict
from .paymentmethodtype import PaymentMethodType
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class LinkedApplePayPaymentMethodTypedDict(TypedDict):
    payment_method_id: str
    r"""ID of the payment method."""
    payment_method_type: PaymentMethodType
    r"""The payment method type that represents a payment rail and directionality"""
    apple_pay: ApplePayResponseTypedDict
    r"""Describes an Apple Pay token on a Moov account."""


class LinkedApplePayPaymentMethod(BaseModel):
    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method."""

    payment_method_type: Annotated[
        PaymentMethodType, pydantic.Field(alias="paymentMethodType")
    ]
    r"""The payment method type that represents a payment rail and directionality"""

    apple_pay: Annotated[ApplePayResponse, pydantic.Field(alias="applePay")]
    r"""Describes an Apple Pay token on a Moov account."""