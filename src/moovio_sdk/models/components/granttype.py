"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class GrantType(str, Enum):
    r"""The type of grant being requested.

    - `client_credentials`: A grant type used by clients to obtain an access token
    - `refresh_token`: A grant type used by clients to obtain a new access token using a refresh token
    """

    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"
