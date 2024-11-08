"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class CardUpdateType(str, Enum):
    r"""Result of the card update"""

    ACCOUNT_CLOSED = "account-closed"
    CONTACT_CARDHOLDER = "contact-cardholder"
    EXPIRATION_UPDATE = "expiration-update"
    NUMBER_UPDATE = "number-update"
