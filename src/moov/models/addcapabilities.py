"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .capabilityid import CapabilityID
from moov.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AddCapabilitiesTypedDict(TypedDict):
    capabilities: List[CapabilityID]


class AddCapabilities(BaseModel):
    capabilities: List[CapabilityID]
