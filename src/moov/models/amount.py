"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing_extensions import TypedDict


class AmountTypedDict(TypedDict):
    currency: str
    r"""A 3-letter ISO 4217 currency code."""
    value: int
    r"""Quantity in the smallest unit of the specified currency.

    In USD this is cents, for example, $12.04 is 1204 and $0.99 is 99.
    """


class Amount(BaseModel):
    currency: str
    r"""A 3-letter ISO 4217 currency code."""

    value: int
    r"""Quantity in the smallest unit of the specified currency.

    In USD this is cents, for example, $12.04 is 1204 and $0.99 is 99.
    """
