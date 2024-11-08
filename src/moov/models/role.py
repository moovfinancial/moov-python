"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .rolepolicy import RolePolicy, RolePolicyTypedDict
from datetime import datetime
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class RoleTypedDict(TypedDict):
    r"""Describes an role."""

    role_id: str
    r"""UUID v4"""
    account_id: str
    r"""ID of account."""
    created_on: datetime
    created_by: str
    r"""UUID v4"""
    last_updated_on: datetime
    last_updated_by: str
    r"""UUID v4"""
    name: str
    r"""Descriptive name allowing spaces."""
    subjects: List[str]
    policies: List[RolePolicyTypedDict]
    deleted_on: NotRequired[Nullable[datetime]]
    deleted_by: NotRequired[Nullable[str]]
    r"""UUID v4"""


class Role(BaseModel):
    r"""Describes an role."""

    role_id: Annotated[str, pydantic.Field(alias="roleID")]
    r"""UUID v4"""

    account_id: Annotated[str, pydantic.Field(alias="accountID")]
    r"""ID of account."""

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    created_by: Annotated[str, pydantic.Field(alias="createdBy")]
    r"""UUID v4"""

    last_updated_on: Annotated[datetime, pydantic.Field(alias="lastUpdatedOn")]

    last_updated_by: Annotated[str, pydantic.Field(alias="lastUpdatedBy")]
    r"""UUID v4"""

    name: str
    r"""Descriptive name allowing spaces."""

    subjects: List[str]

    policies: List[RolePolicy]

    deleted_on: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="deletedOn")
    ] = UNSET

    deleted_by: Annotated[OptionalNullable[str], pydantic.Field(alias="deletedBy")] = (
        UNSET
    )
    r"""UUID v4"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["deletedOn", "deletedBy"]
        nullable_fields = ["deletedOn", "deletedBy"]
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
