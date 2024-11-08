"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .disputeevidence import DisputeEvidence, DisputeEvidenceTypedDict
from .evidencetext import EvidenceText, EvidenceTextTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypedDict


class UploadEvidenceTextRequestTypedDict(TypedDict):
    dispute_id: str
    r"""ID of dispute"""
    evidence_text: EvidenceTextTypedDict


class UploadEvidenceTextRequest(BaseModel):
    dispute_id: Annotated[
        str,
        pydantic.Field(alias="disputeID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of dispute"""

    evidence_text: Annotated[
        EvidenceText,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


UploadEvidenceTextResponseResultTypedDict = Union[List[DisputeEvidenceTypedDict], str]


UploadEvidenceTextResponseResult = Union[List[DisputeEvidence], str]


class UploadEvidenceTextResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: UploadEvidenceTextResponseResultTypedDict


class UploadEvidenceTextResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: UploadEvidenceTextResponseResult
