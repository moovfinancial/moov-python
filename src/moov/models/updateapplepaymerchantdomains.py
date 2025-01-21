"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateApplePayMerchantDomainsTypedDict(TypedDict):
    add_domains: NotRequired[List[str]]
    r"""A unique list of fully-qualified, top-level or sub-domain names to add."""
    remove_domains: NotRequired[List[str]]
    r"""A unique list of fully-qualified, top-level or sub-domain names to remove."""


class UpdateApplePayMerchantDomains(BaseModel):
    add_domains: Annotated[Optional[List[str]], pydantic.Field(alias="addDomains")] = (
        None
    )
    r"""A unique list of fully-qualified, top-level or sub-domain names to add."""

    remove_domains: Annotated[
        Optional[List[str]], pydantic.Field(alias="removeDomains")
    ] = None
    r"""A unique list of fully-qualified, top-level or sub-domain names to remove."""
