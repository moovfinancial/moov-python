"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RepresentativeResponsibilitiesTypedDict(TypedDict):
    r"""Describes the job responsibilities of a business representative."""

    is_controller: NotRequired[bool]
    r"""Indicates whether this individual has significant management responsibilities within the business."""
    is_owner: NotRequired[bool]
    r"""If `true`, this field indicates that the individual has a business ownership stake of at least 25% in the
    business. If the representative does not own at least 25% of the business, this field should be `false`.
    """
    ownership_percentage: NotRequired[int]
    r"""The percentage of ownership this individual has in the business (required if `isOwner` is `true`)."""
    job_title: NotRequired[str]


class RepresentativeResponsibilities(BaseModel):
    r"""Describes the job responsibilities of a business representative."""

    is_controller: Annotated[Optional[bool], pydantic.Field(alias="isController")] = (
        None
    )
    r"""Indicates whether this individual has significant management responsibilities within the business."""

    is_owner: Annotated[Optional[bool], pydantic.Field(alias="isOwner")] = None
    r"""If `true`, this field indicates that the individual has a business ownership stake of at least 25% in the
    business. If the representative does not own at least 25% of the business, this field should be `false`.
    """

    ownership_percentage: Annotated[
        Optional[int], pydantic.Field(alias="ownershipPercentage")
    ] = None
    r"""The percentage of ownership this individual has in the business (required if `isOwner` is `true`)."""

    job_title: Annotated[Optional[str], pydantic.Field(alias="jobTitle")] = None
