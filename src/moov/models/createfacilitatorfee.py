"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateFacilitatorFeeTypedDict(TypedDict):
    r"""Total or markup fee."""

    total: NotRequired[Nullable[int]]
    r"""Total facilitator fee in cents. Only either `total` or `totalDecimal` can be set."""
    total_decimal: NotRequired[Nullable[str]]
    r"""Same as `total`, but a decimal-formatted numerical string that represents up to 9 decimal place precision. Only either `total` or `totalDecimal` can be set. Set this field if you expect the fee to be in fractions of a cent."""
    markup: NotRequired[Nullable[int]]
    r"""Markup facilitator fee in cents. Only either `markup` or `markupDecimal` can be set."""
    markup_decimal: NotRequired[Nullable[str]]
    r"""Same as `markup`, but a decimal-formatted numerical string that represents up to 9 decimal place precision. Only either `markup` or `markupDecimal` can be set. Set this field if you expect the fee to be in fractions of a cent."""


class CreateFacilitatorFee(BaseModel):
    r"""Total or markup fee."""

    total: OptionalNullable[int] = UNSET
    r"""Total facilitator fee in cents. Only either `total` or `totalDecimal` can be set."""

    total_decimal: Annotated[
        OptionalNullable[str], pydantic.Field(alias="totalDecimal")
    ] = UNSET
    r"""Same as `total`, but a decimal-formatted numerical string that represents up to 9 decimal place precision. Only either `total` or `totalDecimal` can be set. Set this field if you expect the fee to be in fractions of a cent."""

    markup: OptionalNullable[int] = UNSET
    r"""Markup facilitator fee in cents. Only either `markup` or `markupDecimal` can be set."""

    markup_decimal: Annotated[
        OptionalNullable[str], pydantic.Field(alias="markupDecimal")
    ] = UNSET
    r"""Same as `markup`, but a decimal-formatted numerical string that represents up to 9 decimal place precision. Only either `markup` or `markupDecimal` can be set. Set this field if you expect the fee to be in fractions of a cent."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["total", "totalDecimal", "markup", "markupDecimal"]
        nullable_fields = ["total", "totalDecimal", "markup", "markupDecimal"]
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