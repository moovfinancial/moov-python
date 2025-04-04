"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountexception import BankAccountException, BankAccountExceptionTypedDict
from .bankaccountholdertype import BankAccountHolderType
from .bankaccountstatus import BankAccountStatus
from .bankaccountstatusreason import BankAccountStatusReason
from .bankaccounttype import BankAccountType
from .basicpaymentmethod import BasicPaymentMethod, BasicPaymentMethodTypedDict
from datetime import datetime
from moovio_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountTypedDict(TypedDict):
    r"""Describes a bank account linked to a Moov account."""

    bank_account_id: str
    fingerprint: str
    r"""Once the bank account is linked, we don't reveal the full bank account number.

    The fingerprint acts as a way to identify whether two linked bank accounts are the same.
    """
    status: BankAccountStatus
    holder_name: str
    holder_type: BankAccountHolderType
    r"""The type of holder on a funding source."""
    bank_name: str
    bank_account_type: BankAccountType
    r"""The bank account type."""
    routing_number: str
    last_four_account_number: str
    updated_on: datetime
    status_reason: NotRequired[BankAccountStatusReason]
    r"""The reason the bank account status changed to the current value."""
    exception_details: NotRequired[BankAccountExceptionTypedDict]
    r"""Reason for, and details related to, an `errored` or `verificationFailed` bank account status."""
    payment_methods: NotRequired[List[BasicPaymentMethodTypedDict]]
    r"""Includes any payment methods generated for a newly created bank account, removing the need to
    call the List Payment Methods endpoint following a successful Create BankAccount request.

    **NOTE: This field is only populated for Create BankAccount requests made with the `X-Wait-For` header.**
    """


class BankAccount(BaseModel):
    r"""Describes a bank account linked to a Moov account."""

    bank_account_id: Annotated[str, pydantic.Field(alias="bankAccountID")]

    fingerprint: str
    r"""Once the bank account is linked, we don't reveal the full bank account number.

    The fingerprint acts as a way to identify whether two linked bank accounts are the same.
    """

    status: BankAccountStatus

    holder_name: Annotated[str, pydantic.Field(alias="holderName")]

    holder_type: Annotated[BankAccountHolderType, pydantic.Field(alias="holderType")]
    r"""The type of holder on a funding source."""

    bank_name: Annotated[str, pydantic.Field(alias="bankName")]

    bank_account_type: Annotated[
        BankAccountType, pydantic.Field(alias="bankAccountType")
    ]
    r"""The bank account type."""

    routing_number: Annotated[str, pydantic.Field(alias="routingNumber")]

    last_four_account_number: Annotated[
        str, pydantic.Field(alias="lastFourAccountNumber")
    ]

    updated_on: Annotated[datetime, pydantic.Field(alias="updatedOn")]

    status_reason: Annotated[
        Optional[BankAccountStatusReason], pydantic.Field(alias="statusReason")
    ] = None
    r"""The reason the bank account status changed to the current value."""

    exception_details: Annotated[
        Optional[BankAccountException], pydantic.Field(alias="exceptionDetails")
    ] = None
    r"""Reason for, and details related to, an `errored` or `verificationFailed` bank account status."""

    payment_methods: Annotated[
        Optional[List[BasicPaymentMethod]], pydantic.Field(alias="paymentMethods")
    ] = None
    r"""Includes any payment methods generated for a newly created bank account, removing the need to
    call the List Payment Methods endpoint following a successful Create BankAccount request.

    **NOTE: This field is only populated for Create BankAccount requests made with the `X-Wait-For` header.**
    """
