"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
from typing import Dict, List, Union
from typing_extensions import TypedDict


SendVerificationCodeViaEmailResponseResultTypedDict = Union[str, str]


SendVerificationCodeViaEmailResponseResult = Union[str, str]


class SendVerificationCodeViaEmailResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: SendVerificationCodeViaEmailResponseResultTypedDict


class SendVerificationCodeViaEmailResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: SendVerificationCodeViaEmailResponseResult