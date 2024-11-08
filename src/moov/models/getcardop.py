"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .card import Card, CardTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetCardRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the Moov account representing the cardholder."""
    card_id: str
    r"""ID of the card."""


class GetCardRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the Moov account representing the cardholder."""

    card_id: Annotated[
        str,
        pydantic.Field(alias="cardID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the card."""


GetCardResponseResultTypedDict = Union[CardTypedDict, str]


GetCardResponseResult = Union[Card, str]


class GetCardResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetCardResponseResultTypedDict


class GetCardResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetCardResponseResult
