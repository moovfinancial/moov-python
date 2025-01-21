"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountcapability import AccountCapability, AccountCapabilityTypedDict
from .accounttype import AccountType
from .customersupport import CustomerSupport, CustomerSupportTypedDict
from .mode import Mode
from .profile import Profile, ProfileTypedDict
from .settings import Settings, SettingsTypedDict
from .termsofservice import TermsOfService, TermsOfServiceTypedDict
from .verification import Verification, VerificationTypedDict
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountTypedDict(TypedDict):
    account_id: str
    r"""Unique identifier for this account."""
    mode: Mode
    r"""The operating mode for an account."""
    account_type: AccountType
    r"""The type of entity represented by this account."""
    display_name: str
    profile: ProfileTypedDict
    r"""Describes a Moov account profile. A profile will have a business or an individual, depending on the account's type."""
    verification: VerificationTypedDict
    r"""Describes identity verification status and relevant identity verification documents."""
    created_on: datetime
    updated_on: datetime
    metadata: NotRequired[Dict[str, str]]
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""
    terms_of_service: NotRequired[TermsOfServiceTypedDict]
    r"""Describes the acceptance of the Terms of Service."""
    capabilities: NotRequired[List[AccountCapabilityTypedDict]]
    foreign_id: NotRequired[str]
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""
    customer_support: NotRequired[CustomerSupportTypedDict]
    r"""User-provided information that can be displayed on credit card transactions for customers to use when
    contacting a customer support team. This data is only allowed on a business account.
    """
    settings: NotRequired[SettingsTypedDict]
    r"""User provided settings to manage an account."""
    disconnected_on: NotRequired[datetime]


class Account(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""Unique identifier for this account."""

    mode: Mode
    r"""The operating mode for an account."""

    account_type: Annotated[AccountType, pydantic.Field(alias="accountType")]
    r"""The type of entity represented by this account."""

    display_name: Annotated[str, pydantic.Field(alias="displayName")]

    profile: Profile
    r"""Describes a Moov account profile. A profile will have a business or an individual, depending on the account's type."""

    verification: Verification
    r"""Describes identity verification status and relevant identity verification documents."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    updated_on: Annotated[datetime, pydantic.Field(alias="updatedOn")]

    metadata: Optional[Dict[str, str]] = None
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""

    terms_of_service: Annotated[
        Optional[TermsOfService], pydantic.Field(alias="termsOfService")
    ] = None
    r"""Describes the acceptance of the Terms of Service."""

    capabilities: Optional[List[AccountCapability]] = None

    foreign_id: Annotated[Optional[str], pydantic.Field(alias="foreignID")] = None
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""

    customer_support: Annotated[
        Optional[CustomerSupport], pydantic.Field(alias="customerSupport")
    ] = None
    r"""User-provided information that can be displayed on credit card transactions for customers to use when
    contacting a customer support team. This data is only allowed on a business account.
    """

    settings: Optional[Settings] = None
    r"""User provided settings to manage an account."""

    disconnected_on: Annotated[
        Optional[datetime], pydantic.Field(alias="disconnectedOn")
    ] = None
