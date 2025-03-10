"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class CardType(str, Enum):
    r"""The type of the card."""

    DEBIT = "debit"
    CREDIT = "credit"
    PREPAID = "prepaid"
    UNKNOWN = "unknown"
