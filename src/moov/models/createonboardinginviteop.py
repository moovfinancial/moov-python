"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .onboardinginvite import OnboardingInvite, OnboardingInviteTypedDict
from moov.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class CreateOnboardingInviteResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: OnboardingInviteTypedDict


class CreateOnboardingInviteResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: OnboardingInvite
