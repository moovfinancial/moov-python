"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class FilePurpose(str, Enum):
    r"""The file's purpose."""

    BUSINESS_VERIFICATION = "business_verification"
    REPRESENTATIVE_VERIFICATION = "representative_verification"
    INDIVIDUAL_VERIFICATION = "individual_verification"
    MERCHANT_UNDERWRITING = "merchant_underwriting"
    ACCOUNT_REQUIREMENT = "account_requirement"
    IDENTITY_VERIFICATION = "identity_verification"
