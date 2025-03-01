"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
from typing_extensions import TypedDict


class TaxIDEinTypedDict(TypedDict):
    number: str


class TaxIDEin(BaseModel):
    number: str


class TaxIDTypedDict(TypedDict):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: TaxIDEinTypedDict


class TaxID(BaseModel):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: TaxIDEin
