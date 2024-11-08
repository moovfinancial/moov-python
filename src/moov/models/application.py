"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationaccountmode import ApplicationAccountMode
from .applicationscope import ApplicationScope
from datetime import datetime
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ApplicationTypedDict(TypedDict):
    r"""Properties of an Application"""

    application_id: NotRequired[str]
    r"""UUID v4"""
    account_id: NotRequired[str]
    r"""UUID v4"""
    account_mode: NotRequired[ApplicationAccountMode]
    r"""The mode of the application's associated account:
    * `0`: unspecified
    * `1`: sandbox
    * `2`: production

    """
    created_on: NotRequired[datetime]
    created_by: NotRequired[str]
    r"""UUID v4"""
    disabled_on: NotRequired[Nullable[datetime]]
    disabled_by: NotRequired[Nullable[str]]
    r"""UUID v4"""
    allowed_scopes: NotRequired[List[ApplicationScope]]
    r"""List of allowed scopes that can be requested on another account per their agreement with Moov."""
    name: NotRequired[str]
    r"""Descriptive name allowing spaces."""
    description: NotRequired[str]
    r"""A description for the item."""


class Application(BaseModel):
    r"""Properties of an Application"""

    application_id: Annotated[Optional[str], pydantic.Field(alias="applicationID")] = (
        None
    )
    r"""UUID v4"""

    account_id: Annotated[Optional[str], pydantic.Field(alias="accountID")] = None
    r"""UUID v4"""

    account_mode: Annotated[
        Optional[ApplicationAccountMode], pydantic.Field(alias="accountMode")
    ] = None
    r"""The mode of the application's associated account:
    * `0`: unspecified
    * `1`: sandbox
    * `2`: production

    """

    created_on: Annotated[Optional[datetime], pydantic.Field(alias="createdOn")] = None

    created_by: Annotated[Optional[str], pydantic.Field(alias="createdBy")] = None
    r"""UUID v4"""

    disabled_on: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="disabledOn")
    ] = UNSET

    disabled_by: Annotated[
        OptionalNullable[str], pydantic.Field(alias="disabledBy")
    ] = UNSET
    r"""UUID v4"""

    allowed_scopes: Annotated[
        Optional[List[ApplicationScope]], pydantic.Field(alias="allowedScopes")
    ] = None
    r"""List of allowed scopes that can be requested on another account per their agreement with Moov."""

    name: Optional[str] = None
    r"""Descriptive name allowing spaces."""

    description: Optional[str] = None
    r"""A description for the item."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "applicationID",
            "accountID",
            "accountMode",
            "createdOn",
            "createdBy",
            "disabledOn",
            "disabledBy",
            "allowedScopes",
            "name",
            "description",
        ]
        nullable_fields = ["disabledOn", "disabledBy"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
