"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updatewebhook import UpdateWebhook, UpdateWebhookTypedDict
from .webhook import Webhook, WebhookTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class UpdateWebhookRequestTypedDict(TypedDict):
    webhook_id: str
    r"""ID of the webhook"""
    update_webhook: UpdateWebhookTypedDict


class UpdateWebhookRequest(BaseModel):
    webhook_id: Annotated[
        str,
        pydantic.Field(alias="webhookID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the webhook"""

    update_webhook: Annotated[
        UpdateWebhook,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateWebhookResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: WebhookTypedDict


class UpdateWebhookResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: Webhook
