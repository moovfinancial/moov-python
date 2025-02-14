"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.models.components import capabilityid as components_capabilityid
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DisableCapabilityGlobalsTypedDict(TypedDict):
    x_moov_version: NotRequired[str]
    r"""Specify an API version.

    API versioning follows the format `vYYYY.QQ.BB`, where
    - `YYYY` is the year
    - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
    - `BB` is the build number, starting at `.01`, for subsequent builds in the same quarter.
    - For example, `v2024.01.00` is the initial release of the first quarter of 2024.

    The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.
    """


class DisableCapabilityGlobals(BaseModel):
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


class DisableCapabilityRequestTypedDict(TypedDict):
    account_id: str
    capability_id: components_capabilityid.CapabilityID
    r"""Moov account capabilities.

    The `production-app` capability might appear in your list. This is a read-only capability that Moov requests and uses for account verification purposes. The capability remains active with your account and requires no additional action.
    """


class DisableCapabilityRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    capability_id: Annotated[
        components_capabilityid.CapabilityID,
        pydantic.Field(alias="capabilityID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Moov account capabilities.

    The `production-app` capability might appear in your list. This is a read-only capability that Moov requests and uses for account verification purposes. The capability remains active with your account and requires no additional action.
    """


class DisableCapabilityResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class DisableCapabilityResponse(BaseModel):
    headers: Dict[str, List[str]]
