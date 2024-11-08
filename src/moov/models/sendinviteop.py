"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .invite import Invite, InviteTypedDict
from .sendinvite import SendInvite, SendInviteTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class SendInviteRequestTypedDict(TypedDict):
    send_invite: SendInviteTypedDict
    x_account_id: NotRequired[str]
    r"""ID of the account."""


class SendInviteRequest(BaseModel):
    send_invite: Annotated[
        SendInvite,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Account-ID"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the account."""


SendInviteResponseResultTypedDict = Union[InviteTypedDict, str]


SendInviteResponseResult = Union[Invite, str]


class SendInviteResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: SendInviteResponseResultTypedDict


class SendInviteResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: SendInviteResponseResult
