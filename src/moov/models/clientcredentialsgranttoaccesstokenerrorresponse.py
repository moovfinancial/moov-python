"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from moov import utils
from moov.types import BaseModel
from typing import Optional


class ClientCredentialsGrantToAccessTokenErrorResponseError(str, Enum):
    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"


class ClientCredentialsGrantToAccessTokenErrorResponseData(BaseModel):
    error: Optional[ClientCredentialsGrantToAccessTokenErrorResponseError] = None


class ClientCredentialsGrantToAccessTokenErrorResponse(Exception):
    r"""Error happened when trying to obtain an access token."""

    data: ClientCredentialsGrantToAccessTokenErrorResponseData

    def __init__(self, data: ClientCredentialsGrantToAccessTokenErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, ClientCredentialsGrantToAccessTokenErrorResponseData
        )
