"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .achlocation import AchLocation, AchLocationTypedDict
from moov.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, TypedDict


class LogoTypedDict(TypedDict):
    name: str
    url: str


class Logo(BaseModel):
    name: str

    url: str


class AchParticipantTypedDict(TypedDict):
    ach_location: AchLocationTypedDict
    customer_name: str
    new_routing_number: str
    office_code: str
    phone_number: str
    record_type_code: str
    revised: str
    routing_number: str
    servicing_frb_number: str
    status_code: str
    view_code: str
    clean_name: str
    logo: Nullable[LogoTypedDict]


class AchParticipant(BaseModel):
    ach_location: Annotated[AchLocation, pydantic.Field(alias="achLocation")]

    customer_name: Annotated[str, pydantic.Field(alias="customerName")]

    new_routing_number: Annotated[str, pydantic.Field(alias="newRoutingNumber")]

    office_code: Annotated[str, pydantic.Field(alias="officeCode")]

    phone_number: Annotated[str, pydantic.Field(alias="phoneNumber")]

    record_type_code: Annotated[str, pydantic.Field(alias="recordTypeCode")]

    revised: str

    routing_number: Annotated[str, pydantic.Field(alias="routingNumber")]

    servicing_frb_number: Annotated[str, pydantic.Field(alias="servicingFRBNumber")]

    status_code: Annotated[str, pydantic.Field(alias="statusCode")]

    view_code: Annotated[str, pydantic.Field(alias="viewCode")]

    clean_name: Annotated[str, pydantic.Field(alias="cleanName")]

    logo: Nullable[Logo]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["logo"]
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
