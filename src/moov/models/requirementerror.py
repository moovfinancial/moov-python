"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .requirementerrorcode import RequirementErrorCode
from .requirementid import RequirementID
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RequirementErrorTypedDict(TypedDict):
    r"""Describes an error fulfilling a Requirement"""

    requirement: NotRequired[RequirementID]
    r"""The unique ID of what the requirement is asking to be filled out."""
    error_code: NotRequired[RequirementErrorCode]


class RequirementError(BaseModel):
    r"""Describes an error fulfilling a Requirement"""

    requirement: Optional[RequirementID] = None
    r"""The unique ID of what the requirement is asking to be filled out."""

    error_code: Annotated[
        Optional[RequirementErrorCode], pydantic.Field(alias="errorCode")
    ] = None