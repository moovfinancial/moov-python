"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createtransferdestinationach import (
    CreateTransferDestinationACH,
    CreateTransferDestinationACHTypedDict,
)
from .createtransferdestinationcard import (
    CreateTransferDestinationCard,
    CreateTransferDestinationCardTypedDict,
)
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransferDestinationTypedDict(TypedDict):
    r"""The final stage of a transfer and the ultimate recipient of the funds."""

    payment_method_id: str
    card_details: NotRequired[CreateTransferDestinationCardTypedDict]
    ach_details: NotRequired[CreateTransferDestinationACHTypedDict]


class CreateTransferDestination(BaseModel):
    r"""The final stage of a transfer and the ultimate recipient of the funds."""

    payment_method_id: Annotated[str, pydantic.Field(alias="paymentMethodID")]

    card_details: Annotated[
        Optional[CreateTransferDestinationCard], pydantic.Field(alias="cardDetails")
    ] = None

    ach_details: Annotated[
        Optional[CreateTransferDestinationACH], pydantic.Field(alias="achDetails")
    ] = None
