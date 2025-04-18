"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AddressUpdateTypedDict(TypedDict):
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    city: NotRequired[str]
    state_or_province: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]


class AddressUpdate(BaseModel):
    address_line1: Annotated[Optional[str], pydantic.Field(alias="addressLine1")] = None

    address_line2: Annotated[Optional[str], pydantic.Field(alias="addressLine2")] = None

    city: Optional[str] = None

    state_or_province: Annotated[
        Optional[str], pydantic.Field(alias="stateOrProvince")
    ] = None

    postal_code: Annotated[Optional[str], pydantic.Field(alias="postalCode")] = None

    country: Optional[str] = None
