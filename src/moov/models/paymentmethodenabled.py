"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class PaymentMethodEnabledTypedDict(TypedDict):
    payment_method_id: str
    r"""ID of the payment method"""
    account_id: str
    r"""ID of the account"""
    source_id: str
    r"""ID of the bank account, card, or wallet"""


class PaymentMethodEnabled(BaseModel):
    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method"""

    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of the account"""

    source_id: Annotated[str, pydantic.Field(alias="sourceID")]
    r"""ID of the bank account, card, or wallet"""