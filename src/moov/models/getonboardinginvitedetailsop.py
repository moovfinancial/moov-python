"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .onboardinginvite import OnboardingInvite, OnboardingInviteTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetOnboardingInviteDetailsRequestTypedDict(TypedDict):
    code: str
    r"""The unique code that identifies the onboarding invite."""


class GetOnboardingInviteDetailsRequest(BaseModel):
    code: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique code that identifies the onboarding invite."""


class GetOnboardingInviteDetailsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: OnboardingInviteTypedDict


class GetOnboardingInviteDetailsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: OnboardingInvite
