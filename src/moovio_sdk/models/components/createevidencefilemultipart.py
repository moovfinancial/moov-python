"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .evidencetype import EvidenceType
import io
from moovio_sdk.types import BaseModel
from moovio_sdk.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class CreateEvidenceFileMultiPartTypedDict(TypedDict):
    file: FileTypedDict
    r"""The file to upload as evidence. Valid types are [jpeg, tiff, pdf] with a limit of 4MB per file.

    The `Content-Type` header for this form part must be one of the following:
    - `image/jpeg`
    - `image/tiff`
    - `application/pdf`
    """
    evidence_type: EvidenceType


class CreateEvidenceFileMultiPart(BaseModel):
    file: Annotated[File, FieldMetadata(multipart=MultipartFormMetadata(file=True))]
    r"""The file to upload as evidence. Valid types are [jpeg, tiff, pdf] with a limit of 4MB per file.

    The `Content-Type` header for this form part must be one of the following:
    - `image/jpeg`
    - `image/tiff`
    - `application/pdf`
    """

    evidence_type: Annotated[
        EvidenceType,
        pydantic.Field(alias="evidenceType"),
        FieldMetadata(multipart=True),
    ]
