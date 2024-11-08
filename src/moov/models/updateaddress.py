"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateAddressTypedDict(TypedDict):
    r"""Provide address fields as necessary to patch the currently saved address.
    Omit any fields that should not be changed.

    """

    address_line1: NotRequired[Nullable[str]]
    address_line2: NotRequired[Nullable[str]]
    city: NotRequired[Nullable[str]]
    state_or_province: NotRequired[Nullable[str]]
    postal_code: NotRequired[Nullable[str]]
    country: NotRequired[Nullable[str]]


class UpdateAddress(BaseModel):
    r"""Provide address fields as necessary to patch the currently saved address.
    Omit any fields that should not be changed.

    """

    address_line1: Annotated[
        OptionalNullable[str], pydantic.Field(alias="addressLine1")
    ] = UNSET

    address_line2: Annotated[
        OptionalNullable[str], pydantic.Field(alias="addressLine2")
    ] = UNSET

    city: OptionalNullable[str] = UNSET

    state_or_province: Annotated[
        OptionalNullable[str], pydantic.Field(alias="stateOrProvince")
    ] = UNSET

    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET

    country: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "addressLine1",
            "addressLine2",
            "city",
            "stateOrProvince",
            "postalCode",
            "country",
        ]
        nullable_fields = [
            "addressLine1",
            "addressLine2",
            "city",
            "stateOrProvince",
            "postalCode",
            "country",
        ]
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
