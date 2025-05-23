"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class AccountType(str, Enum):
    r"""The type of entity represented by this account."""

    INDIVIDUAL = "individual"
    BUSINESS = "business"
    GUEST = "guest"
