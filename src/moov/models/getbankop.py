"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountresponse import BankAccountResponse, BankAccountResponseTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetBankRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    bank_account_id: str
    r"""ID of the bank account"""


class GetBankRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    bank_account_id: Annotated[
        str,
        pydantic.Field(alias="bankAccountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the bank account"""


GetBankResponseResultTypedDict = Union[BankAccountResponseTypedDict, str]


GetBankResponseResult = Union[BankAccountResponse, str]


class GetBankResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetBankResponseResultTypedDict


class GetBankResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetBankResponseResult