"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class CardUpdateReason(str, Enum):
    r"""The results of the card update request."""

    UNSPECIFIED = "unspecified"
    ACCOUNT_CLOSED = "account-closed"
    CONTACT_CARDHOLDER = "contact-cardholder"
    EXPIRATION_UPDATE = "expiration-update"
    NO_CHANGE = "no-change"
    NO_MATCH = "no-match"
    NUMBER_UPDATE = "number-update"