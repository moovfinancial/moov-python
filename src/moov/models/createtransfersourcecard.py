"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transactionsource import TransactionSource
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransferSourceCardTypedDict(TypedDict):
    dynamic_descriptor: NotRequired[str]
    r"""An optional override of the default card statement descriptor for a transfer. Accounts must be enabled by Moov to set this field."""
    transaction_source: NotRequired[TransactionSource]
    r"""Specifies the nature and initiator of a transaction.

    Crucial for recurring and merchant-initiated transactions as per card scheme rules.
    Omit for customer-initiated e-commerce transactions.
    """


class CreateTransferSourceCard(BaseModel):
    dynamic_descriptor: Annotated[
        Optional[str], pydantic.Field(alias="dynamicDescriptor")
    ] = None
    r"""An optional override of the default card statement descriptor for a transfer. Accounts must be enabled by Moov to set this field."""

    transaction_source: Annotated[
        Optional[TransactionSource], pydantic.Field(alias="transactionSource")
    ] = None
    r"""Specifies the nature and initiator of a transaction.

    Crucial for recurring and merchant-initiated transactions as per card scheme rules.
    Omit for customer-initiated e-commerce transactions.
    """
