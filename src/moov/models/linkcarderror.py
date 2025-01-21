"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cardaddresserror import CardAddressError
from .cardexpirationerror import CardExpirationError
from .end2endencryptionerror import End2EndEncryptionError
from moov import utils
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class LinkCardErrorData(BaseModel):
    error: Optional[str] = None

    e2ee: Optional[End2EndEncryptionError] = None

    card_number: Annotated[Optional[str], pydantic.Field(alias="cardNumber")] = None

    card_cvv: Annotated[Optional[str], pydantic.Field(alias="cardCvv")] = None

    expiration: Optional[CardExpirationError] = None

    holder_name: Annotated[Optional[str], pydantic.Field(alias="holderName")] = None

    billing_address: Annotated[
        Optional[CardAddressError], pydantic.Field(alias="billingAddress")
    ] = None

    card_on_file: Annotated[Optional[str], pydantic.Field(alias="cardOnFile")] = None

    merchant_account_id: Annotated[
        Optional[str], pydantic.Field(alias="merchantAccountID")
    ] = None

    verify_name: Annotated[Optional[str], pydantic.Field(alias="verifyName")] = None


class LinkCardError(Exception):
    data: LinkCardErrorData

    def __init__(self, data: LinkCardErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, LinkCardErrorData)
