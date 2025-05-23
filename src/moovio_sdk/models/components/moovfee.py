"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amountdecimal import AmountDecimal, AmountDecimalTypedDict
from .transferparty import TransferParty
from moovio_sdk.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class MoovFeeTypedDict(TypedDict):
    r"""Moov fee charged to an account involved in a transfer."""

    account_id: str
    r"""ID of the account that fees were charged to."""
    transfer_party: TransferParty
    r"""Indicates whether the account charged was the partner, source, or destination of the transfer."""
    total_amount: AmountDecimalTypedDict
    r"""The total amount of fees charged to the account."""
    fee_i_ds: List[str]
    r"""List of fee IDs that sum to the totalAmount."""


class MoovFee(BaseModel):
    r"""Moov fee charged to an account involved in a transfer."""

    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of the account that fees were charged to."""

    transfer_party: Annotated[TransferParty, pydantic.Field(alias="transferParty")]
    r"""Indicates whether the account charged was the partner, source, or destination of the transfer."""

    total_amount: Annotated[AmountDecimal, pydantic.Field(alias="totalAmount")]
    r"""The total amount of fees charged to the account."""

    fee_i_ds: Annotated[List[str], pydantic.Field(alias="feeIDs")]
    r"""List of fee IDs that sum to the totalAmount."""
