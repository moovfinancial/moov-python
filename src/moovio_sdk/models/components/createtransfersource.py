"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createtransfersourceach import (
    CreateTransferSourceACH,
    CreateTransferSourceACHTypedDict,
)
from .createtransfersourcecard import (
    CreateTransferSourceCard,
    CreateTransferSourceCardTypedDict,
)
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransferSourceTypedDict(TypedDict):
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`."""

    transfer_id: NotRequired[str]
    r"""A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/),
    associating the new transfer with a parent transfer.
    """
    payment_method_id: NotRequired[str]
    payment_token: NotRequired[str]
    card_details: NotRequired[CreateTransferSourceCardTypedDict]
    ach_details: NotRequired[CreateTransferSourceACHTypedDict]


class CreateTransferSource(BaseModel):
    r"""Where funds for a transfer originate. For the source, you must include either a `paymentMethodID` or a `transferID`."""

    transfer_id: Annotated[Optional[str], pydantic.Field(alias="transferID")] = None
    r"""A `transferID` is used to create a [transfer group](https://docs.moov.io/guides/money-movement/transfer-groups/),
    associating the new transfer with a parent transfer.
    """

    payment_method_id: Annotated[
        Optional[str], pydantic.Field(alias="paymentMethodID")
    ] = None

    payment_token: Annotated[Optional[str], pydantic.Field(alias="paymentToken")] = None

    card_details: Annotated[
        Optional[CreateTransferSourceCard], pydantic.Field(alias="cardDetails")
    ] = None

    ach_details: Annotated[
        Optional[CreateTransferSourceACH], pydantic.Field(alias="achDetails")
    ] = None
