"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createaccountsettings import CreateAccountSettings, CreateAccountSettingsTypedDict
from .createprofileerror import CreateProfileError, CreateProfileErrorTypedDict
from .customersupporterror import CustomerSupportError, CustomerSupportErrorTypedDict
from .termsofserviceerror import TermsOfServiceError, TermsOfServiceErrorTypedDict
from moovio_sdk.types import BaseModel
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateAccountErrorTypedDict(TypedDict):
    account_type: NotRequired[str]
    profile: NotRequired[CreateProfileErrorTypedDict]
    metadata: NotRequired[str]
    terms_of_service: NotRequired[TermsOfServiceErrorTypedDict]
    foreign_id: NotRequired[str]
    customer_support: NotRequired[CustomerSupportErrorTypedDict]
    settings: NotRequired[CreateAccountSettingsTypedDict]
    capabilities: NotRequired[Dict[str, str]]


class CreateAccountError(BaseModel):
    account_type: Annotated[Optional[str], pydantic.Field(alias="accountType")] = None

    profile: Optional[CreateProfileError] = None

    metadata: Optional[str] = None

    terms_of_service: Annotated[
        Optional[TermsOfServiceError], pydantic.Field(alias="termsOfService")
    ] = None

    foreign_id: Annotated[Optional[str], pydantic.Field(alias="foreignID")] = None

    customer_support: Annotated[
        Optional[CustomerSupportError], pydantic.Field(alias="customerSupport")
    ] = None

    settings: Optional[CreateAccountSettings] = None

    capabilities: Optional[Dict[str, str]] = None
