"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updateissuedcard import UpdateIssuedCard, UpdateIssuedCardTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class UpdateIssuedCardRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    issued_card_id: str
    r"""ID of the issued card."""
    update_issued_card: UpdateIssuedCardTypedDict


class UpdateIssuedCardRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    issued_card_id: Annotated[
        str,
        pydantic.Field(alias="issuedCardID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the issued card."""

    update_issued_card: Annotated[
        UpdateIssuedCard,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateIssuedCardResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: str


class UpdateIssuedCardResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: str