"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class RefundCreatedTypedDict(TypedDict):
    account_id: str
    r"""ID of the merchant's Account associated with the refund transfer"""
    transfer_id: str
    r"""ID of the original transfer"""
    refund_id: str
    r"""ID of the refund transfer"""


class RefundCreated(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of the merchant's Account associated with the refund transfer"""

    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]
    r"""ID of the original transfer"""

    refund_id: Annotated[str, pydantic.Field(alias="refundID")]
    r"""ID of the refund transfer"""