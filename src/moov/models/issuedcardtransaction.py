"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .issuingmerchantdata import IssuingMerchantData, IssuingMerchantDataTypedDict
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IssuedCardTransactionTypedDict(TypedDict):
    card_transaction_id: str
    issued_card_id: str
    funding_wallet_id: str
    amount: str
    r"""A decimal-formatted numerical string that represents up to 2 decimal place precision. In USD for example, 12.34 is $12.34 and 0.99 is $0.99."""
    authorized_on: datetime
    merchant_data: IssuingMerchantDataTypedDict
    created_on: datetime
    authorization_id: NotRequired[str]


class IssuedCardTransaction(BaseModel):
    card_transaction_id: Annotated[str, pydantic.Field(alias="cardTransactionID")]

    issued_card_id: Annotated[str, pydantic.Field(alias="issuedCardID")]

    funding_wallet_id: Annotated[str, pydantic.Field(alias="fundingWalletID")]

    amount: str
    r"""A decimal-formatted numerical string that represents up to 2 decimal place precision. In USD for example, 12.34 is $12.34 and 0.99 is $0.99."""

    authorized_on: Annotated[datetime, pydantic.Field(alias="authorizedOn")]

    merchant_data: Annotated[IssuingMerchantData, pydantic.Field(alias="merchantData")]

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    authorization_id: Annotated[
        Optional[str], pydantic.Field(alias="authorizationID")
    ] = None
