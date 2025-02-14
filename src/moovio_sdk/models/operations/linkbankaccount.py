"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.models.components import (
    bankaccount as components_bankaccount,
    bankaccountwaitfor as components_bankaccountwaitfor,
    linkbankaccount as components_linkbankaccount,
)
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinkBankAccountGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class LinkBankAccountGlobals(BaseModel):
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


class LinkBankAccountRequestTypedDict(TypedDict):
    account_id: str
    link_bank_account: components_linkbankaccount.LinkBankAccountTypedDict
    x_wait_for: NotRequired[components_bankaccountwaitfor.BankAccountWaitFor]
    r"""Optional header to wait for certain events, such as the creation of a payment method, to occur before returning a response.

    When this header is set to `payment-method`, the response will include any payment methods that were created for the newly
    linked card in the `paymentMethods` field. Otherwise, the `paymentMethods` field will be omitted from the response.
    """


class LinkBankAccountRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    link_bank_account: Annotated[
        components_linkbankaccount.LinkBankAccount,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_wait_for: Annotated[
        Optional[components_bankaccountwaitfor.BankAccountWaitFor],
        pydantic.Field(alias="x-wait-for"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional header to wait for certain events, such as the creation of a payment method, to occur before returning a response.

    When this header is set to `payment-method`, the response will include any payment methods that were created for the newly
    linked card in the `paymentMethods` field. Otherwise, the `paymentMethods` field will be omitted from the response.
    """


class LinkBankAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: components_bankaccount.BankAccountTypedDict


class LinkBankAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_bankaccount.BankAccount
