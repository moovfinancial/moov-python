"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing_extensions import deprecated


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class VerificationStatusDetails(str, Enum):
    r"""This field is deprecated and will be removed in a future release."""

    FAILED_AUTO_VERIFY = "failedAutoVerify"
    DOC_DOB_MISMATCH = "docDobMismatch"
    DOC_NAME_MISMATCH = "docNameMismatch"
    DOC_ADDRESS_MISMATCH = "docAddressMismatch"
    DOC_NUMBER_MISMATCH = "docNumberMismatch"
    DOC_INCOMPLETE = "docIncomplete"
    DOC_FAILED_RISK = "docFailedRisk"
    POTENTIAL_ACCOUNT_SANCTIONS_MATCH = "potentialAccountSanctionsMatch"
    POTENTIAL_REPRESENTATIVE_SANCTIONS_MATCH = "potentialRepresentativeSanctionsMatch"
    FAILED_OTHER = "failedOther"