"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .moneytransferpullfromcard import (
    MoneyTransferPullFromCard,
    MoneyTransferPullFromCardTypedDict,
)
from .moneytransferpushtocard import (
    MoneyTransferPushToCard,
    MoneyTransferPushToCardTypedDict,
)
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MoneyTransferTypedDict(TypedDict):
    pull_from_card: NotRequired[MoneyTransferPullFromCardTypedDict]
    push_to_card: NotRequired[MoneyTransferPushToCardTypedDict]


class MoneyTransfer(BaseModel):
    pull_from_card: Annotated[
        Optional[MoneyTransferPullFromCard], pydantic.Field(alias="pullFromCard")
    ] = None

    push_to_card: Annotated[
        Optional[MoneyTransferPushToCard], pydantic.Field(alias="pushToCard")
    ] = None
