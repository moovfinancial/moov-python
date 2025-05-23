"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amountdecimal import AmountDecimal, AmountDecimalTypedDict
from .wallettransactiontype import WalletTransactionType
from moovio_sdk.types import BaseModel
from typing_extensions import TypedDict


class SweepSubtotalTypedDict(TypedDict):
    type: WalletTransactionType
    r"""The type of wallet transaction the subtotal is for."""
    count: int
    r"""The number of transactions of this type accrued in the sweep."""
    amount: AmountDecimalTypedDict
    r"""The value of transactions of this type accrued in the sweep."""


class SweepSubtotal(BaseModel):
    type: WalletTransactionType
    r"""The type of wallet transaction the subtotal is for."""

    count: int
    r"""The number of transactions of this type accrued in the sweep."""

    amount: AmountDecimal
    r"""The value of transactions of this type accrued in the sweep."""
