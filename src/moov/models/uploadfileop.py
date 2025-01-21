"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fileuploadrequestmultipart import (
    FileUploadRequestMultiPart,
    FileUploadRequestMultiPartTypedDict,
)
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from .versions import Versions
from moov.types import BaseModel
from moov.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UploadFileSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    o_auth2_auth: NotRequired[str]


class UploadFileSecurity(BaseModel):
    basic_auth: Annotated[
        Optional[SchemeBasicAuth],
        FieldMetadata(
            security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="basic")
        ),
    ] = None

    o_auth2_auth: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True, scheme_type="oauth2", field_name="Authorization"
            )
        ),
    ] = None


class UploadFileRequestTypedDict(TypedDict):
    account_id: str
    file_upload_request_multi_part: FileUploadRequestMultiPartTypedDict
    x_moov_version: NotRequired[Versions]
    r"""Specify an API version."""


class UploadFileRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    file_upload_request_multi_part: Annotated[
        FileUploadRequestMultiPart,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]

    x_moov_version: Annotated[
        Optional[Versions],
        pydantic.Field(alias="x-moov-version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Specify an API version."""
