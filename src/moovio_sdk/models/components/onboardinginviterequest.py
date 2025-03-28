"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationscope import ApplicationScope
from .capabilityid import CapabilityID
from .createaccount import CreateAccount, CreateAccountTypedDict
from moovio_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OnboardingInviteRequestTypedDict(TypedDict):
    r"""Request to create an onboarding invite."""

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
    return_url: NotRequired[str]
    r"""Optional URL to redirect the user to after they complete the onboarding process."""
    terms_of_service_url: NotRequired[str]
    r"""Optional URL to your organization's terms of service."""
    prefill: NotRequired[CreateAccountTypedDict]


class OnboardingInviteRequest(BaseModel):
    r"""Request to create an onboarding invite."""

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

    return_url: Annotated[Optional[str], pydantic.Field(alias="returnURL")] = None
    r"""Optional URL to redirect the user to after they complete the onboarding process."""

    terms_of_service_url: Annotated[
        Optional[str], pydantic.Field(alias="termsOfServiceURL")
    ] = None
    r"""Optional URL to your organization's terms of service."""

    prefill: Optional[CreateAccount] = None
