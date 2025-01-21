"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class VolumeByCustomerTypeTypedDict(TypedDict):
    business_to_business_percentage: int
    consumer_to_business_percentage: int


class VolumeByCustomerType(BaseModel):
    business_to_business_percentage: Annotated[
        int, pydantic.Field(alias="businessToBusinessPercentage")
    ]

    consumer_to_business_percentage: Annotated[
        int, pydantic.Field(alias="consumerToBusinessPercentage")
    ]
