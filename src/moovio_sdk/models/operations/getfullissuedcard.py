"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.models.components import fullissuedcard as components_fullissuedcard
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetFullIssuedCardGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class GetFullIssuedCardGlobals(BaseModel):
    x_moov_version: Annotated[
        Optional[str],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = "v2024.01.00"
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class GetFullIssuedCardRequestTypedDict(TypedDict):
    account_id: str
    r"""The Moov business account for which the card was issued."""
    issued_card_id: str


class GetFullIssuedCardRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The Moov business account for which the card was issued."""

    issued_card_id: Annotated[
        str,
        pydantic.Field(alias="issuedCardID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class GetFullIssuedCardResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: components_fullissuedcard.FullIssuedCardTypedDict


class GetFullIssuedCardResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_fullissuedcard.FullIssuedCard
