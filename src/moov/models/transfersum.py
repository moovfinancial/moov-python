"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from moov.types import BaseModel
from typing_extensions import TypedDict


class TransferSumTypedDict(TypedDict):
    r"""Sum of all transfers between two timestamps"""

    start: datetime
    stop: datetime
    amount: int


class TransferSum(BaseModel):
    r"""Sum of all transfers between two timestamps"""

    start: datetime

    stop: datetime

    amount: int