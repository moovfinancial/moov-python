"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .card import Card, CardTypedDict
from .cardupdaterequest import CardUpdateRequest, CardUpdateRequestTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class UpdateCardRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the Moov account representing the cardholder."""
    card_id: str
    r"""ID of the card."""
    card_update_request: CardUpdateRequestTypedDict


class UpdateCardRequest(BaseModel):
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

    card_update_request: Annotated[
        CardUpdateRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


UpdateCardResponseResultTypedDict = Union[CardTypedDict, str]


UpdateCardResponseResult = Union[Card, str]


class UpdateCardResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: UpdateCardResponseResultTypedDict


class UpdateCardResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: UpdateCardResponseResult
