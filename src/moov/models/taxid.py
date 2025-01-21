"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing_extensions import TypedDict


class EinTypedDict(TypedDict):
    number: str


class Ein(BaseModel):
    number: str


class TaxIDTypedDict(TypedDict):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: EinTypedDict


class TaxID(BaseModel):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: Ein
