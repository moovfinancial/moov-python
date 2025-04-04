"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from moovio_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomerSupportTypedDict(TypedDict):
    r"""User-provided information that can be displayed on credit card transactions for customers to use when
    contacting a customer support team. This data is only allowed on a business account.
    """

    phone: NotRequired[PhoneNumberTypedDict]
    email: NotRequired[str]
    address: NotRequired[AddressTypedDict]
    website: NotRequired[str]


class CustomerSupport(BaseModel):
    r"""User-provided information that can be displayed on credit card transactions for customers to use when
    contacting a customer support team. This data is only allowed on a business account.
    """

    phone: Optional[PhoneNumber] = None

    email: Optional[str] = None

    address: Optional[Address] = None

    website: Optional[str] = None
