"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .asynccreatedtransfer import AsyncCreatedTransfer, AsyncCreatedTransferTypedDict
from .createtransfer import CreateTransfer, CreateTransferTypedDict
from .transfer import Transfer, TransferTypedDict
from .transferpostresponse import TransferPostResponse, TransferPostResponseTypedDict
from .waitfor import WaitFor
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransferRequestTypedDict(TypedDict):
    x_idempotency_key: str
    r"""Prevents duplicate transfers from being created. Note that we only accept UUID v4."""
    create_transfer: CreateTransferTypedDict
    x_wait_for: NotRequired[WaitFor]
    r"""Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an asynchronous response indicating the transfer was created (this is the default response if the header is omitted)."""


class CreateTransferRequest(BaseModel):
    x_idempotency_key: Annotated[
        str,
        pydantic.Field(alias="X-Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Prevents duplicate transfers from being created. Note that we only accept UUID v4."""

    create_transfer: Annotated[
        CreateTransfer,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_wait_for: Annotated[
        Optional[WaitFor],
        pydantic.Field(alias="X-Wait-For"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional header that indicates whether to return a synchronous response that includes full transfer and rail-specific details or an asynchronous response indicating the transfer was created (this is the default response if the header is omitted)."""


CreateTransferResponseResultTypedDict = Union[
    AsyncCreatedTransferTypedDict, TransferTypedDict, TransferPostResponseTypedDict, str
]


CreateTransferResponseResult = Union[
    AsyncCreatedTransfer, Transfer, TransferPostResponse, str
]


class CreateTransferResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: CreateTransferResponseResultTypedDict


class CreateTransferResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: CreateTransferResponseResult
