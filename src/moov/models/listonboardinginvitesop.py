"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .onboardinginvite import OnboardingInvite, OnboardingInviteTypedDict
from moov.types import BaseModel
from typing import Dict, List, Union
from typing_extensions import TypedDict


ListOnboardingInvitesResponseResultTypedDict = Union[
    List[OnboardingInviteTypedDict], str
]


ListOnboardingInvitesResponseResult = Union[List[OnboardingInvite], str]


class ListOnboardingInvitesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ListOnboardingInvitesResponseResultTypedDict


class ListOnboardingInvitesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ListOnboardingInvitesResponseResult
