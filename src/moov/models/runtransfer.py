"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .scheduledpaymentmethod import (
    ScheduledPaymentMethod,
    ScheduledPaymentMethodTypedDict,
)
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RunTransferTypedDict(TypedDict):
    r"""Defines the attributes of a transfer"""

    amount: AmountTypedDict
    r"""An integer value representing money in a specific currency."""
    partner_account_id: str
    r"""AccountID of the Moov partner in the transfer."""
    source: ScheduledPaymentMethodTypedDict
    r"""Defines a payment method to use for the scheduled transfer"""
    destination: ScheduledPaymentMethodTypedDict
    r"""Defines a payment method to use for the scheduled transfer"""
    description: NotRequired[str]
    r"""Simple description to place on the transfer"""


class RunTransfer(BaseModel):
    r"""Defines the attributes of a transfer"""

    amount: Amount
    r"""An integer value representing money in a specific currency."""

    partner_account_id: Annotated[str, pydantic.Field(alias="partnerAccountID")]
    r"""AccountID of the Moov partner in the transfer."""

    source: ScheduledPaymentMethod
    r"""Defines a payment method to use for the scheduled transfer"""

    destination: ScheduledPaymentMethod
    r"""Defines a payment method to use for the scheduled transfer"""

    description: Optional[str] = None
    r"""Simple description to place on the transfer"""