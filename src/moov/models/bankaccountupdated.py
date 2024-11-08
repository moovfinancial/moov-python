"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountstatusreason import BankAccountStatusReason
from .exceptiondetails import ExceptionDetails, ExceptionDetailsTypedDict
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountUpdatedTypedDict(TypedDict):
    bank_account_id: str
    r"""ID of the bank account"""
    account_id: str
    r"""ID of the account where the bank account was updated"""
    status: str
    r"""Status of the bank account"""
    status_reason: BankAccountStatusReason
    r"""The reason the bank account status changed to the current value."""
    exception_details: NotRequired[Nullable[ExceptionDetailsTypedDict]]
    r"""Reason for, and details related to, an `errored` or `verificationFailed` bank account status."""


class BankAccountUpdated(BaseModel):
    bank_account_id: Annotated[str, pydantic.Field(alias="bankAccountID")]
    r"""ID of the bank account"""

    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of the account where the bank account was updated"""

    status: str
    r"""Status of the bank account"""

    status_reason: Annotated[
        BankAccountStatusReason, pydantic.Field(alias="statusReason")
    ]
    r"""The reason the bank account status changed to the current value."""

    exception_details: Annotated[
        OptionalNullable[ExceptionDetails], pydantic.Field(alias="exceptionDetails")
    ] = UNSET
    r"""Reason for, and details related to, an `errored` or `verificationFailed` bank account status."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["exceptionDetails"]
        nullable_fields = ["exceptionDetails"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
