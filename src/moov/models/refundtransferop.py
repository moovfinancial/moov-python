"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createrefund import CreateRefund, CreateRefundTypedDict
from .getrefund import GetRefund, GetRefundTypedDict
from .refundpostresponse import RefundPostResponse, RefundPostResponseTypedDict
from .waitfor import WaitFor
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class RefundTransferRequestTypedDict(TypedDict):
    transfer_id: str
    r"""Identifier for the transfer."""
    x_idempotency_key: str
    r"""Prevents duplicate refunds from being created. Note that we only accept UUID v4."""
    x_wait_for: NotRequired[WaitFor]
    r"""Optional header that indicates whether to return a synchronous response that includes the full refund and card transaction details or an asynchronous response indicating the refund was created (this is the default response if the header is omitted)."""
    create_refund: NotRequired[CreateRefundTypedDict]


class RefundTransferRequest(BaseModel):
    transfer_id: Annotated[
        str,
        pydantic.Field(alias="transferID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Identifier for the transfer."""

    x_idempotency_key: Annotated[
        str,
        pydantic.Field(alias="X-Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Prevents duplicate refunds from being created. Note that we only accept UUID v4."""

    x_wait_for: Annotated[
        Optional[WaitFor],
        pydantic.Field(alias="X-Wait-For"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional header that indicates whether to return a synchronous response that includes the full refund and card transaction details or an asynchronous response indicating the refund was created (this is the default response if the header is omitted)."""

    create_refund: Annotated[
        Optional[CreateRefund],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


RefundTransferResponseResultTypedDict = Union[
    GetRefundTypedDict, RefundPostResponseTypedDict, str
]


RefundTransferResponseResult = Union[GetRefund, RefundPostResponse, str]


class RefundTransferResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: RefundTransferResponseResultTypedDict


class RefundTransferResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: RefundTransferResponseResult