"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .evidencetype import EvidenceType
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class DisputeEvidenceMetadataTypedDict(TypedDict):
    evidence_id: str
    dispute_id: str
    mime_type: str
    filename: str
    size: int
    evidence_type: EvidenceType
    text: str
    r"""The text submited as evidence."""
    created_on: datetime
    updated_on: datetime


class DisputeEvidenceMetadata(BaseModel):
    evidence_id: Annotated[str, pydantic.Field(alias="evidenceID")]

    dispute_id: Annotated[str, pydantic.Field(alias="disputeID")]

    mime_type: Annotated[str, pydantic.Field(alias="mimeType")]

    filename: str

    size: int

    evidence_type: Annotated[EvidenceType, pydantic.Field(alias="evidenceType")]

    text: str
    r"""The text submited as evidence."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    updated_on: Annotated[datetime, pydantic.Field(alias="updatedOn")]
