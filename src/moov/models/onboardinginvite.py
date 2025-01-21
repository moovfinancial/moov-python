"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationscope import ApplicationScope
from .capabilityid import CapabilityID
from .createaccount import CreateAccount, CreateAccountTypedDict
from .onboardingpartneraccount import (
    OnboardingPartnerAccount,
    OnboardingPartnerAccountTypedDict,
)
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OnboardingInviteTypedDict(TypedDict):
    code: str
    r"""A unique code that identifies an onboarding invite."""
    link: str
    r"""A unique URL, including the invite code, that the recipient can follow to redeem the invitation."""
    scopes: List[ApplicationScope]
    r"""List of [scopes](https://docs.moov.io/api/authentication/scopes/) you request to use on this
    account. These values are used to determine what can be done with the account onboarded.
    """
    capabilities: List[CapabilityID]
    r"""List of [capabilities](https://docs.moov.io/guides/accounts/capabilities/) you intend to request for this
    account. These values are used to determine what information to collect from the user during onboarding.
    """
    fee_plan_codes: List[str]
    r"""List of fee plan codes to assign the account created by the invitee."""
    created_on: datetime
    return_url: NotRequired[str]
    r"""The scopes requested by the inviter."""
    terms_of_service_url: NotRequired[str]
    r"""The terms of service URL set by the inviter."""
    prefill: NotRequired[CreateAccountTypedDict]
    partner: NotRequired[OnboardingPartnerAccountTypedDict]
    r"""The account that created the onboarding invite."""
    revoked_on: NotRequired[datetime]
    redeemed_on: NotRequired[datetime]


class OnboardingInvite(BaseModel):
    code: str
    r"""A unique code that identifies an onboarding invite."""

    link: str
    r"""A unique URL, including the invite code, that the recipient can follow to redeem the invitation."""

    scopes: List[ApplicationScope]
    r"""List of [scopes](https://docs.moov.io/api/authentication/scopes/) you request to use on this
    account. These values are used to determine what can be done with the account onboarded.
    """

    capabilities: List[CapabilityID]
    r"""List of [capabilities](https://docs.moov.io/guides/accounts/capabilities/) you intend to request for this
    account. These values are used to determine what information to collect from the user during onboarding.
    """

    fee_plan_codes: Annotated[List[str], pydantic.Field(alias="feePlanCodes")]
    r"""List of fee plan codes to assign the account created by the invitee."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    return_url: Annotated[Optional[str], pydantic.Field(alias="returnURL")] = None
    r"""The scopes requested by the inviter."""

    terms_of_service_url: Annotated[
        Optional[str], pydantic.Field(alias="TermsOfServiceURL")
    ] = None
    r"""The terms of service URL set by the inviter."""

    prefill: Optional[CreateAccount] = None

    partner: Optional[OnboardingPartnerAccount] = None
    r"""The account that created the onboarding invite."""

    revoked_on: Annotated[Optional[datetime], pydantic.Field(alias="revokedOn")] = None

    redeemed_on: Annotated[Optional[datetime], pydantic.Field(alias="redeemedOn")] = (
        None
    )
