"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cardissuingnetwork import CardIssuingNetwork
from .issuingauthorizationstatus import IssuingAuthorizationStatus
from .issuingmerchantdata import IssuingMerchantData, IssuingMerchantDataTypedDict
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IssuedCardAuthorizationTypedDict(TypedDict):
    authorization_id: str
    issued_card_id: str
    funding_wallet_id: str
    network: CardIssuingNetwork
    r"""The name of the network a card transaction is routed through."""
    authorized_amount: str
    r"""A decimal-formatted numerical string that represents up to 2 decimal place precision. In USD for example, 12.34 is $12.34 and 0.99 is $0.99."""
    status: IssuingAuthorizationStatus
    r"""Status of a card issuing authorization."""
    merchant_data: IssuingMerchantDataTypedDict
    created_on: datetime
    card_transactions: NotRequired[List[str]]
    r"""List of card transaction IDs associated with this authorization."""


class IssuedCardAuthorization(BaseModel):
    authorization_id: Annotated[str, pydantic.Field(alias="authorizationID")]

    issued_card_id: Annotated[str, pydantic.Field(alias="issuedCardID")]

    funding_wallet_id: Annotated[str, pydantic.Field(alias="fundingWalletID")]

    network: CardIssuingNetwork
    r"""The name of the network a card transaction is routed through."""

    authorized_amount: Annotated[str, pydantic.Field(alias="authorizedAmount")]
    r"""A decimal-formatted numerical string that represents up to 2 decimal place precision. In USD for example, 12.34 is $12.34 and 0.99 is $0.99."""

    status: IssuingAuthorizationStatus
    r"""Status of a card issuing authorization."""

    merchant_data: Annotated[IssuingMerchantData, pydantic.Field(alias="merchantData")]

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    card_transactions: Annotated[
        Optional[List[str]], pydantic.Field(alias="cardTransactions")
    ] = None
    r"""List of card transaction IDs associated with this authorization."""
