"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from moovio_sdk.models.components import (
    end2endencryptionerror as components_end2endencryptionerror,
)
from moovio_sdk.models.errors import MoovError
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class LinkCardErrorData(BaseModel):
    error: Optional[str] = None

    e2ee: Optional[components_end2endencryptionerror.End2EndEncryptionError] = None

    card_number: Annotated[Optional[str], pydantic.Field(alias="cardNumber")] = None

    card_cvv: Annotated[Optional[str], pydantic.Field(alias="cardCvv")] = None

    expiration: Optional[str] = None

    holder_name: Annotated[Optional[str], pydantic.Field(alias="holderName")] = None

    billing_address: Annotated[
        Optional[str], pydantic.Field(alias="billingAddress")
    ] = None

    card_on_file: Annotated[Optional[str], pydantic.Field(alias="cardOnFile")] = None

    merchant_account_id: Annotated[
        Optional[str], pydantic.Field(alias="merchantAccountID")
    ] = None

    verify_name: Annotated[Optional[str], pydantic.Field(alias="verifyName")] = None


class LinkCardError(MoovError):
    data: LinkCardErrorData

    def __init__(
        self,
        data: LinkCardErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data
