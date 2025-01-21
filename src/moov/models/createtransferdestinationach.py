"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTransferDestinationACHTypedDict(TypedDict):
    company_entry_description: NotRequired[str]
    r"""An optional override of the default NACHA company entry description for a transfer."""
    originating_company_name: NotRequired[str]
    r"""An optional override of the default NACHA company name for a transfer."""


class CreateTransferDestinationACH(BaseModel):
    company_entry_description: Annotated[
        Optional[str], pydantic.Field(alias="companyEntryDescription")
    ] = None
    r"""An optional override of the default NACHA company entry description for a transfer."""

    originating_company_name: Annotated[
        Optional[str], pydantic.Field(alias="originatingCompanyName")
    ] = None
    r"""An optional override of the default NACHA company name for a transfer."""
