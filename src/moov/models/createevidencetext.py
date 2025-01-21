"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .evidencetype import EvidenceType
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class CreateEvidenceTextTypedDict(TypedDict):
    text: str
    r"""The text to associate with the dispute as evidence."""
    evidence_type: EvidenceType


class CreateEvidenceText(BaseModel):
    text: str
    r"""The text to associate with the dispute as evidence."""

    evidence_type: Annotated[EvidenceType, pydantic.Field(alias="evidenceType")]
