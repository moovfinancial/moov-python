"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.models.components import (
    account as components_account,
    accounttype as components_accounttype,
    capabilityid as components_capabilityid,
    capabilitystatus as components_capabilitystatus,
)
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAccountsGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class ListAccountsGlobals(BaseModel):
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


class ListAccountsRequestTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Filter connected accounts by name.

    If provided, this query will attempt to find matches against the following Account and Profile fields:
    <ul>
    <li>Account `displayName`</li>
    <li>Individual Profile `firstName`, `middleName`, and `lastName`</li>
    <li>Business Profile `legalBusinessName`</li>
    </ul>
    """
    email: NotRequired[str]
    r"""Filter connected accounts by email address.

    Provide the full email address to filter by email.
    """
    type: NotRequired[components_accounttype.AccountType]
    r"""Filter connected accounts by AccountType.

    If the `type` parameter is used in combination with `name`, only the corresponding type's name fields will
    be searched. For example, if `type=business` and `name=moov`, the search will attempt to find matches against
    the display name and Business Profile name fields (`legalBusinessName`, and `doingBusinessAs`).
    """
    foreign_id: NotRequired[str]
    r"""Serves as an optional alias from a foreign/external system which can be used to reference this resource."""
    include_disconnected: NotRequired[bool]
    r"""Filter disconnected accounts.

    If true, the response will include disconnected accounts.
    """
    capability: NotRequired[components_capabilityid.CapabilityID]
    r"""Filter connected accounts by the capability."""
    capability_status: NotRequired[components_capabilitystatus.CapabilityStatus]
    r"""Filter connected accounts by the capability."""
    skip: NotRequired[int]
    count: NotRequired[int]


class ListAccountsRequest(BaseModel):
    name: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter connected accounts by name.

    If provided, this query will attempt to find matches against the following Account and Profile fields:
    <ul>
    <li>Account `displayName`</li>
    <li>Individual Profile `firstName`, `middleName`, and `lastName`</li>
    <li>Business Profile `legalBusinessName`</li>
    </ul>
    """

    email: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter connected accounts by email address.

    Provide the full email address to filter by email.
    """

    type: Annotated[
        Optional[components_accounttype.AccountType],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter connected accounts by AccountType.

    If the `type` parameter is used in combination with `name`, only the corresponding type's name fields will
    be searched. For example, if `type=business` and `name=moov`, the search will attempt to find matches against
    the display name and Business Profile name fields (`legalBusinessName`, and `doingBusinessAs`).
    """

    foreign_id: Annotated[
        Optional[str],
        pydantic.Field(alias="foreignID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Serves as an optional alias from a foreign/external system which can be used to reference this resource."""

    include_disconnected: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeDisconnected"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter disconnected accounts.

    If true, the response will include disconnected accounts.
    """

    capability: Annotated[
        Optional[components_capabilityid.CapabilityID],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter connected accounts by the capability."""

    capability_status: Annotated[
        Optional[components_capabilitystatus.CapabilityStatus],
        pydantic.Field(alias="capabilityStatus"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Filter connected accounts by the capability."""

    skip: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None

    count: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None


class ListAccountsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[components_account.AccountTypedDict]


class ListAccountsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[components_account.Account]
