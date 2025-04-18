"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cardacquiringrefund import CardAcquiringRefund, CardAcquiringRefundTypedDict
from moovio_sdk.types import BaseModel
from typing_extensions import TypedDict


class ReversedWithRefundTypedDict(TypedDict):
    refund: CardAcquiringRefundTypedDict
    r"""Details of a card refund."""


class ReversedWithRefund(BaseModel):
    refund: CardAcquiringRefund
    r"""Details of a card refund."""
