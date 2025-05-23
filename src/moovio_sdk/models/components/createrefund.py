"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateRefundTypedDict(TypedDict):
    r"""Specifies a partial amount to refund.

    This request body is optional, an empty body will issue a refund for the full amount of the original transfer.
    """

    amount: NotRequired[int]
    r"""Amount to refund in cents. If null, the original transfer's full amount will be refunded."""


class CreateRefund(BaseModel):
    r"""Specifies a partial amount to refund.

    This request body is optional, an empty body will issue a refund for the full amount of the original transfer.
    """

    amount: Optional[int] = None
    r"""Amount to refund in cents. If null, the original transfer's full amount will be refunded."""
