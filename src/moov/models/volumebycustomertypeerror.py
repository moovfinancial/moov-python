"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VolumeByCustomerTypeErrorTypedDict(TypedDict):
    business_to_business_percentage: NotRequired[str]
    consumer_to_business_percentage: NotRequired[str]


class VolumeByCustomerTypeError(BaseModel):
    business_to_business_percentage: Annotated[
        Optional[str], pydantic.Field(alias="businessToBusinessPercentage")
    ] = None

    consumer_to_business_percentage: Annotated[
        Optional[str], pydantic.Field(alias="consumerToBusinessPercentage")
    ] = None
