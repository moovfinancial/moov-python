"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .evidencefile import EvidenceFile, EvidenceFileTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class UploadEvidenceFileRequestTypedDict(TypedDict):
    dispute_id: str
    r"""ID of dispute"""
    evidence_file: EvidenceFileTypedDict


class UploadEvidenceFileRequest(BaseModel):
    dispute_id: Annotated[
        str,
        pydantic.Field(alias="disputeID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of dispute"""

    evidence_file: Annotated[
        EvidenceFile,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]


UploadEvidenceFileResponseResultTypedDict = Union[str, str]


UploadEvidenceFileResponseResult = Union[str, str]


class UploadEvidenceFileResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: UploadEvidenceFileResponseResultTypedDict


class UploadEvidenceFileResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: UploadEvidenceFileResponseResult