"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .recur_input import RecurInput, RecurInputTypedDict
from .upsertoccurrence import UpsertOccurrence, UpsertOccurrenceTypedDict
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class UpsertScheduleTypedDict(TypedDict):
    r"""Describes the schedule to create or modify"""

    description: NotRequired[str]
    r"""Simple description of what the schedule is."""
    recur: NotRequired[Nullable[RecurInputTypedDict]]
    r"""Defines configuration for recurring transfers"""
    occurrences: NotRequired[List[UpsertOccurrenceTypedDict]]
    r"""Occurrences to either create or modify

    """


class UpsertSchedule(BaseModel):
    r"""Describes the schedule to create or modify"""

    description: Optional[str] = None
    r"""Simple description of what the schedule is."""

    recur: OptionalNullable[RecurInput] = UNSET
    r"""Defines configuration for recurring transfers"""

    occurrences: Optional[List[UpsertOccurrence]] = None
    r"""Occurrences to either create or modify

    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "recur", "occurrences"]
        nullable_fields = ["recur"]
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
