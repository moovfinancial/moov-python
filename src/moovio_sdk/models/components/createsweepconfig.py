"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sweepconfigstatus import SweepConfigStatus
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateSweepConfigTypedDict(TypedDict):
    wallet_id: str
    status: SweepConfigStatus
    push_payment_method_id: str
    r"""ID of the payment method."""
    pull_payment_method_id: str
    r"""ID of the payment method."""
    statement_descriptor: NotRequired[str]
    r"""The text that appears on the banking statement. The default descriptor is a 10 character ID if an override is not set in the sweep configs statementDescriptor."""
    minimum_balance: NotRequired[str]


class CreateSweepConfig(BaseModel):
    wallet_id: Annotated[str, pydantic.Field(alias="walletID")]

    status: SweepConfigStatus

    push_payment_method_id: Annotated[str, pydantic.Field(alias="pushPaymentMethodID")]
    r"""ID of the payment method."""

    pull_payment_method_id: Annotated[str, pydantic.Field(alias="pullPaymentMethodID")]
    r"""ID of the payment method."""

    statement_descriptor: Annotated[
        Optional[str], pydantic.Field(alias="statementDescriptor")
    ] = None
    r"""The text that appears on the banking statement. The default descriptor is a 10 character ID if an override is not set in the sweep configs statementDescriptor."""

    minimum_balance: Annotated[
        Optional[str], pydantic.Field(alias="minimumBalance")
    ] = None
