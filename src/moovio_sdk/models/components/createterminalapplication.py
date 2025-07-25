"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .terminalapplicationplatform import TerminalApplicationPlatform
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTerminalApplicationTypedDict(TypedDict):
    r"""Describes a create terminal application request."""

    platform: TerminalApplicationPlatform
    r"""Platform of the terminal application."""
    app_bundle_id: NotRequired[str]
    r"""The app bundle identifier of the terminal application. Required if platform is `ios`."""
    package_name: NotRequired[str]
    r"""The app package name of the terminal application. Required if platform is `android`."""
    sha256_digest: NotRequired[str]
    r"""The SHA-256 digest of the signing key for the application. Required if platform is `android`."""
    version_code: NotRequired[str]
    r"""The version code of the Android application. Required if platform is `android`."""


class CreateTerminalApplication(BaseModel):
    r"""Describes a create terminal application request."""

    platform: TerminalApplicationPlatform
    r"""Platform of the terminal application."""

    app_bundle_id: Annotated[Optional[str], pydantic.Field(alias="appBundleID")] = None
    r"""The app bundle identifier of the terminal application. Required if platform is `ios`."""

    package_name: Annotated[Optional[str], pydantic.Field(alias="packageName")] = None
    r"""The app package name of the terminal application. Required if platform is `android`."""

    sha256_digest: Annotated[Optional[str], pydantic.Field(alias="sha256Digest")] = None
    r"""The SHA-256 digest of the signing key for the application. Required if platform is `android`."""

    version_code: Annotated[Optional[str], pydantic.Field(alias="versionCode")] = None
    r"""The version code of the Android application. Required if platform is `android`."""
