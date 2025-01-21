"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov import utils
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class LinkApplePayErrorData(BaseModel):
    error: Optional[str] = None
    r"""Describes an error that wasn't attributable to a single request field."""

    payment_data: Annotated[Optional[str], pydantic.Field(alias="paymentData")] = None
    r"""Describes an error within the `token.paymentData` request field."""

    payment_method: Annotated[Optional[str], pydantic.Field(alias="paymentMethod")] = (
        None
    )
    r"""Describes an error within the `token.paymentMethod` request field."""

    transaction_identifier: Annotated[
        Optional[str], pydantic.Field(alias="transactionIdentifier")
    ] = None
    r"""Describes an error within the `token.transactionIdentifier` request field."""


class LinkApplePayError(Exception):
    data: LinkApplePayErrorData

    def __init__(self, data: LinkApplePayErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, LinkApplePayErrorData)
