"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class ACHPaymentSettingsTypedDict(TypedDict):
    company_name: str
    r"""The description that shows up on ACH transactions. This will default to the account's display name on account creation."""


class ACHPaymentSettings(BaseModel):
    company_name: Annotated[str, pydantic.Field(alias="companyName")]
    r"""The description that shows up on ACH transactions. This will default to the account's display name on account creation."""
