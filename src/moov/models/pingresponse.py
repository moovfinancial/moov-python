"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhook import Webhook, WebhookTypedDict
from moov.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class RequestBodySentTypedDict(TypedDict):
    r"""The request body sent to the target URL. It will contain an event type of `event.test` and an empty (null) data payload."""


class RequestBodySent(BaseModel):
    r"""The request body sent to the target URL. It will contain an event type of `event.test` and an empty (null) data payload."""


class PingResponseTypedDict(TypedDict):
    webhook: WebhookTypedDict
    request_body_sent: RequestBodySentTypedDict
    r"""The request body sent to the target URL. It will contain an event type of `event.test` and an empty (null) data payload."""
    response_status_code: int
    r"""The response status code after sending a ping event to the URL."""


class PingResponse(BaseModel):
    webhook: Webhook

    request_body_sent: Annotated[
        RequestBodySent, pydantic.Field(alias="requestBodySent")
    ]
    r"""The request body sent to the target URL. It will contain an event type of `event.test` and an empty (null) data payload."""

    response_status_code: Annotated[int, pydantic.Field(alias="responseStatusCode")]
    r"""The response status code after sending a ping event to the URL."""