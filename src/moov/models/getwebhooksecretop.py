"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhooksecretkey import WebhookSecretKey, WebhookSecretKeyTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetWebhookSecretRequestTypedDict(TypedDict):
    webhook_id: str
    r"""ID of the webhook"""


class GetWebhookSecretRequest(BaseModel):
    webhook_id: Annotated[
        str,
        pydantic.Field(alias="webhookID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the webhook"""


class GetWebhookSecretResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: WebhookSecretKeyTypedDict


class GetWebhookSecretResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: WebhookSecretKey