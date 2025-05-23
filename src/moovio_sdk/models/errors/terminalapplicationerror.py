"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk import utils
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class TerminalApplicationErrorData(BaseModel):
    platform: Optional[str] = None

    app_bundle_id: Annotated[Optional[str], pydantic.Field(alias="appBundleID")] = None

    package_name: Annotated[Optional[str], pydantic.Field(alias="packageName")] = None

    sha256_digest: Annotated[Optional[str], pydantic.Field(alias="sha256Digest")] = None

    version_code: Annotated[Optional[str], pydantic.Field(alias="versionCode")] = None


class TerminalApplicationError(Exception):
    data: TerminalApplicationErrorData

    def __init__(self, data: TerminalApplicationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, TerminalApplicationErrorData)
