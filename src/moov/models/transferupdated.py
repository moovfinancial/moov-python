"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transferpaymentmethod import TransferPaymentMethod, TransferPaymentMethodTypedDict
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class TransferUpdatedTypedDict(TypedDict):
    account_id: str
    r"""ID of the facilitator account"""
    transfer_id: str
    r"""ID of the transfer"""
    status: str
    r"""Status of the transfer"""
    source: TransferPaymentMethodTypedDict
    destination: TransferPaymentMethodTypedDict


class TransferUpdated(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of the facilitator account"""

    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]
    r"""ID of the transfer"""

    status: str
    r"""Status of the transfer"""

    source: TransferPaymentMethod

    destination: TransferPaymentMethod