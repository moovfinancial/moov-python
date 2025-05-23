"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class WebhookWalletAvailableBalanceTypedDict(TypedDict):
    r"""The available balance of a wallet."""

    currency: str
    value: int
    value_decimal: str


class WebhookWalletAvailableBalance(BaseModel):
    r"""The available balance of a wallet."""

    currency: str

    value: int

    value_decimal: Annotated[str, pydantic.Field(alias="valueDecimal")]
