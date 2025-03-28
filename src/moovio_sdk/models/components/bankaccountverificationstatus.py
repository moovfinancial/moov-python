"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class BankAccountVerificationStatus(str, Enum):
    NEW = "new"
    SENT_CREDIT = "sent-credit"
    MAX_ATTEMPTS_EXCEEDED = "max-attempts-exceeded"
    FAILED = "failed"
    EXPIRED = "expired"
    SUCCESSFUL = "successful"
