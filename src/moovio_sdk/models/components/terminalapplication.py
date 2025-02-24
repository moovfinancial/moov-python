"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .terminalapplicationplatform import TerminalApplicationPlatform
from .terminalapplicationstatus import TerminalApplicationStatus
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TerminalApplicationTypedDict(TypedDict):
    r"""Describes a terminal application."""

    terminal_application_id: str
    r"""ID of the terminal application."""
    status: TerminalApplicationStatus
    r"""Status of the terminal application."""
    platform: TerminalApplicationPlatform
    r"""Platform of the terminal application."""
    app_bundle_id: NotRequired[str]
    r"""The app bundle identifier of the terminal application. Will be returned if platform is ios."""
    package_name: NotRequired[str]
    r"""The app package name of the terminal application. Will be returned if platform is android."""
    sha256_digest: NotRequired[str]
    r"""The app version of the terminal application Will be returned if platform is android."""
    version_code: NotRequired[str]
    r"""The app version of the terminal application Will be returned if platform is android."""


class TerminalApplication(BaseModel):
    r"""Describes a terminal application."""

    terminal_application_id: Annotated[
        str, pydantic.Field(alias="terminalApplicationID")
    ]
    r"""ID of the terminal application."""

    status: TerminalApplicationStatus
    r"""Status of the terminal application."""

    platform: TerminalApplicationPlatform
    r"""Platform of the terminal application."""

    app_bundle_id: Annotated[Optional[str], pydantic.Field(alias="appBundleID")] = None
    r"""The app bundle identifier of the terminal application. Will be returned if platform is ios."""

    package_name: Annotated[Optional[str], pydantic.Field(alias="packageName")] = None
    r"""The app package name of the terminal application. Will be returned if platform is android."""

    sha256_digest: Annotated[Optional[str], pydantic.Field(alias="sha256Digest")] = None
    r"""The app version of the terminal application Will be returned if platform is android."""

    version_code: Annotated[Optional[str], pydantic.Field(alias="versionCode")] = None
    r"""The app version of the terminal application Will be returned if platform is android."""
