"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov import utils
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class CreateSweepConfigErrorData(BaseModel):
    wallet_id: Annotated[Optional[str], pydantic.Field(alias="walletID")] = None

    status: Optional[str] = None

    push_payment_method_id: Annotated[
        Optional[str], pydantic.Field(alias="pushPaymentMethodID")
    ] = None

    pull_payment_method_id: Annotated[
        Optional[str], pydantic.Field(alias="pullPaymentMethodID")
    ] = None

    statement_descriptor: Annotated[
        Optional[str], pydantic.Field(alias="statementDescriptor")
    ] = None

    minimum_balance: Annotated[
        Optional[str], pydantic.Field(alias="minimumBalance")
    ] = None


class CreateSweepConfigError(Exception):
    data: CreateSweepConfigErrorData

    def __init__(self, data: CreateSweepConfigErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, CreateSweepConfigErrorData)
