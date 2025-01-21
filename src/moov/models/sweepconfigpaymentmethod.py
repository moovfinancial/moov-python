"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SweepConfigPaymentMethodTypedDict(TypedDict):
    r"""The payment method used to push or pull funds to a bank account.
    The push payment method can only be ach-credit-standard or ach-credit-same-day. The pull payment method can only be ach-debit-fund.
    """

    payment_method_id: str
    r"""ID of the payment method."""
    disabled_on: NotRequired[datetime]


class SweepConfigPaymentMethod(BaseModel):
    r"""The payment method used to push or pull funds to a bank account.
    The push payment method can only be ach-credit-standard or ach-credit-same-day. The pull payment method can only be ach-debit-fund.
    """

    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]
    r"""ID of the payment method."""

    disabled_on: Annotated[Optional[datetime], pydantic.Field(alias="disabledOn")] = (
        None
    )
