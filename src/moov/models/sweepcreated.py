"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class SweepCreatedTypedDict(TypedDict):
    sweep_id: str
    r"""ID of the sweep"""
    wallet_id: str
    r"""ID of the Wallet"""


class SweepCreated(BaseModel):
    sweep_id: Annotated[str, pydantic.Field(alias="sweepID")]
    r"""ID of the sweep"""

    wallet_id: Annotated[str, pydantic.Field(alias="walletID")]
    r"""ID of the Wallet"""