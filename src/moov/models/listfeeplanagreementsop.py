"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agreement import Agreement, AgreementTypedDict
from .agreementstatus import AgreementStatus
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListFeePlanAgreementsRequestTypedDict(TypedDict):
    account_id: str
    r"""ID of the account."""
    agreement_id: NotRequired[str]
    r"""A comma-separated list of agreement IDs to filter the results by."""
    status: NotRequired[AgreementStatus]
    r"""A comma-separated list of statuses to filter the results by."""


class ListFeePlanAgreementsRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the account."""

    agreement_id: Annotated[
        Optional[str],
        pydantic.Field(alias="agreementID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A comma-separated list of agreement IDs to filter the results by."""

    status: Annotated[
        Optional[AgreementStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A comma-separated list of statuses to filter the results by."""


ListFeePlanAgreementsResponseResultTypedDict = Union[List[AgreementTypedDict], str]


ListFeePlanAgreementsResponseResult = Union[List[Agreement], str]


class ListFeePlanAgreementsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListFeePlanAgreementsResponseResultTypedDict


class ListFeePlanAgreementsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListFeePlanAgreementsResponseResult