"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .name import Name, NameTypedDict
from .representative import Representative, RepresentativeTypedDict
from enum import Enum
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProfileIndividualPhoneTypedDict(TypedDict):
    number: NotRequired[str]
    country_code: NotRequired[str]


class ProfileIndividualPhone(BaseModel):
    number: Optional[str] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None


class ProfileIndividualAddressTypedDict(TypedDict):
    address_line1: str
    city: str
    state_or_province: str
    postal_code: str
    country: str
    address_line2: NotRequired[str]


class ProfileIndividualAddress(BaseModel):
    address_line1: Annotated[str, pydantic.Field(alias="addressLine1")]

    city: str

    state_or_province: Annotated[str, pydantic.Field(alias="stateOrProvince")]

    postal_code: Annotated[str, pydantic.Field(alias="postalCode")]

    country: str

    address_line2: Annotated[Optional[str], pydantic.Field(alias="addressLine2")] = None


class IndividualTypedDict(TypedDict):
    r"""Describes an individual."""

    name: NotRequired[NameTypedDict]
    r"""An individual's name."""
    phone: NotRequired[Nullable[ProfileIndividualPhoneTypedDict]]
    email: NotRequired[str]
    r"""Email address."""
    address: NotRequired[Nullable[ProfileIndividualAddressTypedDict]]
    birth_date_provided: NotRequired[bool]
    r"""Indicates whether this individual's birth date has been provided."""
    government_id_provided: NotRequired[bool]
    r"""Indicates whether a government ID (SSN, ITIN, etc.) has been provided for this individual."""


class Individual(BaseModel):
    r"""Describes an individual."""

    name: Optional[Name] = None
    r"""An individual's name."""

    phone: OptionalNullable[ProfileIndividualPhone] = UNSET

    email: Optional[str] = None
    r"""Email address."""

    address: OptionalNullable[ProfileIndividualAddress] = UNSET

    birth_date_provided: Annotated[
        Optional[bool], pydantic.Field(alias="birthDateProvided")
    ] = False
    r"""Indicates whether this individual's birth date has been provided."""

    government_id_provided: Annotated[
        Optional[bool], pydantic.Field(alias="governmentIDProvided")
    ] = False
    r"""Indicates whether a government ID (SSN, ITIN, etc.) has been provided for this individual."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "phone",
            "email",
            "address",
            "birthDateProvided",
            "governmentIDProvided",
        ]
        nullable_fields = ["phone", "address"]
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


class BusinessType(str, Enum):
    r"""The type of entity represented by this business."""

    SOLE_PROPRIETORSHIP = "soleProprietorship"
    UNINCORPORATED_ASSOCIATION = "unincorporatedAssociation"
    TRUST = "trust"
    PUBLIC_CORPORATION = "publicCorporation"
    PRIVATE_CORPORATION = "privateCorporation"
    LLC = "llc"
    PARTNERSHIP = "partnership"
    UNINCORPORATED_NON_PROFIT = "unincorporatedNonProfit"
    INCORPORATED_NON_PROFIT = "incorporatedNonProfit"
    GOVERNMENT_ENTITY = "governmentEntity"


class ProfileAddressTypedDict(TypedDict):
    address_line1: str
    city: str
    state_or_province: str
    postal_code: str
    country: str
    address_line2: NotRequired[str]


class ProfileAddress(BaseModel):
    address_line1: Annotated[str, pydantic.Field(alias="addressLine1")]

    city: str

    state_or_province: Annotated[str, pydantic.Field(alias="stateOrProvince")]

    postal_code: Annotated[str, pydantic.Field(alias="postalCode")]

    country: str

    address_line2: Annotated[Optional[str], pydantic.Field(alias="addressLine2")] = None


class ProfilePhoneTypedDict(TypedDict):
    number: NotRequired[str]
    country_code: NotRequired[str]


class ProfilePhone(BaseModel):
    number: Optional[str] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None


class IndustryCodesTypedDict(TypedDict):
    r"""Describes industry specific identifiers."""

    naics: NotRequired[str]
    sic: NotRequired[str]
    mcc: NotRequired[str]


class IndustryCodes(BaseModel):
    r"""Describes industry specific identifiers."""

    naics: Optional[str] = None

    sic: Optional[str] = None

    mcc: Optional[str] = None


class PrimaryRegulator(str, Enum):
    r"""If the business is a financial institution, this field describes its primary regulator."""

    OCC = "OCC"
    FDIC = "FDIC"
    NCUA = "NCUA"
    FRB = "FRB"


class BusinessTypedDict(TypedDict):
    r"""Describes a business."""

    owners_provided: bool
    legal_business_name: NotRequired[str]
    doing_business_as: NotRequired[str]
    business_type: NotRequired[Nullable[BusinessType]]
    address: NotRequired[Nullable[ProfileAddressTypedDict]]
    phone: NotRequired[Nullable[ProfilePhoneTypedDict]]
    email: NotRequired[str]
    r"""Email address."""
    website: NotRequired[str]
    description: NotRequired[str]
    tax_id_provided: NotRequired[bool]
    r"""Indicates whether a tax ID has been provided for this business."""
    representatives: NotRequired[List[RepresentativeTypedDict]]
    industry_codes: NotRequired[Nullable[IndustryCodesTypedDict]]
    primary_regulator: NotRequired[Nullable[PrimaryRegulator]]


class Business(BaseModel):
    r"""Describes a business."""

    owners_provided: Annotated[bool, pydantic.Field(alias="ownersProvided")]

    legal_business_name: Annotated[
        Optional[str], pydantic.Field(alias="legalBusinessName")
    ] = None

    doing_business_as: Annotated[
        Optional[str], pydantic.Field(alias="doingBusinessAs")
    ] = None

    business_type: Annotated[
        OptionalNullable[BusinessType], pydantic.Field(alias="businessType")
    ] = UNSET

    address: OptionalNullable[ProfileAddress] = UNSET

    phone: OptionalNullable[ProfilePhone] = UNSET

    email: Optional[str] = None
    r"""Email address."""

    website: Optional[str] = None

    description: Optional[str] = None

    tax_id_provided: Annotated[
        Optional[bool], pydantic.Field(alias="taxIDProvided")
    ] = False
    r"""Indicates whether a tax ID has been provided for this business."""

    representatives: Optional[List[Representative]] = None

    industry_codes: Annotated[
        OptionalNullable[IndustryCodes], pydantic.Field(alias="industryCodes")
    ] = UNSET

    primary_regulator: Annotated[
        OptionalNullable[PrimaryRegulator], pydantic.Field(alias="primaryRegulator")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "legalBusinessName",
            "doingBusinessAs",
            "businessType",
            "address",
            "phone",
            "email",
            "website",
            "description",
            "taxIDProvided",
            "representatives",
            "industryCodes",
            "primaryRegulator",
        ]
        nullable_fields = [
            "businessType",
            "address",
            "phone",
            "industryCodes",
            "primaryRegulator",
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


class ProfileTypedDict(TypedDict):
    r"""Describes a Moov account profile."""

    individual: NotRequired[Nullable[IndividualTypedDict]]
    business: NotRequired[Nullable[BusinessTypedDict]]


class Profile(BaseModel):
    r"""Describes a Moov account profile."""

    individual: OptionalNullable[Individual] = UNSET

    business: OptionalNullable[Business] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["individual", "business"]
        nullable_fields = ["individual", "business"]
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
