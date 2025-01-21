"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addresserror import AddressError, AddressErrorTypedDict
from .phonenumbererror import PhoneNumberError, PhoneNumberErrorTypedDict
from moov.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomerSupportErrorTypedDict(TypedDict):
    phone: NotRequired[PhoneNumberErrorTypedDict]
    email: NotRequired[str]
    address: NotRequired[AddressErrorTypedDict]
    website: NotRequired[str]


class CustomerSupportError(BaseModel):
    phone: Optional[PhoneNumberError] = None

    email: Optional[str] = None

    address: Optional[AddressError] = None

    website: Optional[str] = None
