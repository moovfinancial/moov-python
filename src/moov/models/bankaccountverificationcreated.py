"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountverificationmethod import BankAccountVerificationMethod
from .bankaccountverificationstatus import BankAccountVerificationStatus
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class BankAccountVerificationCreatedTypedDict(TypedDict):
    verification_method: BankAccountVerificationMethod
    status: BankAccountVerificationStatus


class BankAccountVerificationCreated(BaseModel):
    verification_method: Annotated[
        BankAccountVerificationMethod, pydantic.Field(alias="verificationMethod")
    ]

    status: BankAccountVerificationStatus
