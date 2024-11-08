"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .account import Account, AccountTypedDict
from .accountwaitfor import AccountWaitFor
from .createaccountrequest import CreateAccountRequest, CreateAccountRequestTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateAccountRequest1TypedDict(TypedDict):
    create_account_request: CreateAccountRequestTypedDict
    x_wait_for: NotRequired[AccountWaitFor]
    r"""Optional header that indicates whether to wait for the connection to be created before returning from the account creation.

    """


class CreateAccountRequest1(BaseModel):
    create_account_request: Annotated[
        CreateAccountRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_wait_for: Annotated[
        Optional[AccountWaitFor],
        pydantic.Field(alias="X-Wait-For"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional header that indicates whether to wait for the connection to be created before returning from the account creation.

    """


CreateAccountResponseResultTypedDict = Union[AccountTypedDict, str]


CreateAccountResponseResult = Union[Account, str]


class CreateAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: CreateAccountResponseResultTypedDict


class CreateAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: CreateAccountResponseResult
