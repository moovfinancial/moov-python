"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentmethod import PaymentMethod, PaymentMethodTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class GetPaymentMethodRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    payment_method_id: str
    r"""ID of the payment method. Can be one of `walletID`, `cardID`, or `bankAccountID`."""


class GetPaymentMethodRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    payment_method_id: Annotated[
        str,
        pydantic.Field(alias="paymentMethodID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the payment method. Can be one of `walletID`, `cardID`, or `bankAccountID`."""


GetPaymentMethodResponseResultTypedDict = Union[PaymentMethodTypedDict, str]


GetPaymentMethodResponseResult = Union[PaymentMethod, str]


class GetPaymentMethodResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetPaymentMethodResponseResultTypedDict


class GetPaymentMethodResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetPaymentMethodResponseResult