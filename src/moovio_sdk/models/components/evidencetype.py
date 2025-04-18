"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class EvidenceType(str, Enum):
    RECEIPT = "receipt"
    PROOF_OF_DELIVERY = "proof-of-delivery"
    CANCELATION_POLICY = "cancelation-policy"
    TERMS_OF_SERVICE = "terms-of-service"
    CUSTOMER_COMMUNICATION = "customer-communication"
    GENERIC_EVIDENCE = "generic-evidence"
    COVER_LETTER = "cover-letter"
    OTHER = "other"
