"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccount import BankAccount, BankAccountTypedDict
from enum import Enum
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class AchDebitFundPaymentMethodPaymentMethodType(str, Enum):
    ACH_DEBIT_FUND = "ach-debit-fund"


class AchDebitFundPaymentMethodTypedDict(TypedDict):
    payment_method_id: str
    r"""ID of the payment method."""
    bank_account: BankAccountTypedDict
    r"""Describes a bank account linked to a Moov account."""
    payment_method_type: AchDebitFundPaymentMethodPaymentMethodType


class AchDebitFundPaymentMethod(BaseModel):
    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method."""

    bank_account: Annotated[BankAccount, pydantic.Field(alias="bankAccount")]
    r"""Describes a bank account linked to a Moov account."""

    payment_method_type: Annotated[
        AchDebitFundPaymentMethodPaymentMethodType,
        pydantic.Field(alias="paymentMethodType"),
    ]
