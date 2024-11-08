"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ein import Ein, EinTypedDict
from .name import Name, NameTypedDict
from enum import Enum
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateProfilePhoneTypedDict(TypedDict):
    number: NotRequired[str]
    country_code: NotRequired[str]


class CreateProfilePhone(BaseModel):
    number: Optional[str] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None


class CreateProfileAddressTypedDict(TypedDict):
    address_line1: str
    city: str
    state_or_province: str
    postal_code: str
    country: str
    address_line2: NotRequired[str]


class CreateProfileAddress(BaseModel):
    address_line1: Annotated[str, pydantic.Field(alias="addressLine1")]

    city: str

    state_or_province: Annotated[str, pydantic.Field(alias="stateOrProvince")]

    postal_code: Annotated[str, pydantic.Field(alias="postalCode")]

    country: str

    address_line2: Annotated[Optional[str], pydantic.Field(alias="addressLine2")] = None


class CreateProfileBirthDateTypedDict(TypedDict):
    r"""An individual's birthdate."""

    day: int
    month: int
    year: int


class CreateProfileBirthDate(BaseModel):
    r"""An individual's birthdate."""

    day: int

    month: int

    year: int


class CreateProfileSsnTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class CreateProfileSsn(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class CreateProfileItinTypedDict(TypedDict):
    full: NotRequired[str]
    last_four: NotRequired[str]


class CreateProfileItin(BaseModel):
    full: Optional[str] = None

    last_four: Annotated[Optional[str], pydantic.Field(alias="lastFour")] = None


class CreateProfileGovernmentIDTypedDict(TypedDict):
    ssn: NotRequired[Nullable[CreateProfileSsnTypedDict]]
    itin: NotRequired[Nullable[CreateProfileItinTypedDict]]


class CreateProfileGovernmentID(BaseModel):
    ssn: OptionalNullable[CreateProfileSsn] = UNSET

    itin: OptionalNullable[CreateProfileItin] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ssn", "itin"]
        nullable_fields = ["ssn", "itin"]
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


class CreateProfileIndividualTypedDict(TypedDict):
    r"""Describes the fields available when creating an individual."""

    name: NameTypedDict
    r"""An individual's name."""
    phone: NotRequired[Nullable[CreateProfilePhoneTypedDict]]
    email: NotRequired[str]
    r"""Email address."""
    address: NotRequired[Nullable[CreateProfileAddressTypedDict]]
    birth_date: NotRequired[Nullable[CreateProfileBirthDateTypedDict]]
    government_id: NotRequired[Nullable[CreateProfileGovernmentIDTypedDict]]


class CreateProfileIndividual(BaseModel):
    r"""Describes the fields available when creating an individual."""

    name: Name
    r"""An individual's name."""

    phone: OptionalNullable[CreateProfilePhone] = UNSET

    email: Optional[str] = None
    r"""Email address."""

    address: OptionalNullable[CreateProfileAddress] = UNSET

    birth_date: Annotated[
        OptionalNullable[CreateProfileBirthDate], pydantic.Field(alias="birthDate")
    ] = UNSET

    government_id: Annotated[
        OptionalNullable[CreateProfileGovernmentID],
        pydantic.Field(alias="governmentID"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["phone", "email", "address", "birthDate", "governmentID"]
        nullable_fields = ["phone", "address", "birthDate", "governmentID"]
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


class CreateProfileBusinessType(str, Enum):
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


class CreateProfileBusinessAddressTypedDict(TypedDict):
    address_line1: str
    city: str
    state_or_province: str
    postal_code: str
    country: str
    address_line2: NotRequired[str]


class CreateProfileBusinessAddress(BaseModel):
    address_line1: Annotated[str, pydantic.Field(alias="addressLine1")]

    city: str

    state_or_province: Annotated[str, pydantic.Field(alias="stateOrProvince")]

    postal_code: Annotated[str, pydantic.Field(alias="postalCode")]

    country: str

    address_line2: Annotated[Optional[str], pydantic.Field(alias="addressLine2")] = None


class CreateProfileBusinessPhoneTypedDict(TypedDict):
    number: NotRequired[str]
    country_code: NotRequired[str]


class CreateProfileBusinessPhone(BaseModel):
    number: Optional[str] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None


class TaxIDTypedDict(TypedDict):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: NotRequired[EinTypedDict]


class TaxID(BaseModel):
    r"""An EIN (employer identification number) for the business. For sole proprietors, an SSN can be used as the EIN."""

    ein: Optional[Ein] = None


class CreateProfileIndustryCodesTypedDict(TypedDict):
    r"""Describes industry specific identifiers."""

    naics: NotRequired[str]
    sic: NotRequired[str]
    mcc: NotRequired[str]


class CreateProfileIndustryCodes(BaseModel):
    r"""Describes industry specific identifiers."""

    naics: Optional[str] = None

    sic: Optional[str] = None

    mcc: Optional[str] = None


class CreateProfilePrimaryRegulator(str, Enum):
    r"""If the business is a financial institution, this field describes its primary regulator."""

    OCC = "OCC"
    FDIC = "FDIC"
    NCUA = "NCUA"
    FRB = "FRB"


class CreateProfileBusinessTypedDict(TypedDict):
    r"""Describes the fields available when creating a business."""

    legal_business_name: str
    doing_business_as: NotRequired[str]
    business_type: NotRequired[Nullable[CreateProfileBusinessType]]
    address: NotRequired[Nullable[CreateProfileBusinessAddressTypedDict]]
    phone: NotRequired[Nullable[CreateProfileBusinessPhoneTypedDict]]
    email: NotRequired[str]
    r"""Email address."""
    website: NotRequired[str]
    description: NotRequired[str]
    tax_id: NotRequired[Nullable[TaxIDTypedDict]]
    industry_codes: NotRequired[Nullable[CreateProfileIndustryCodesTypedDict]]
    primary_regulator: NotRequired[Nullable[CreateProfilePrimaryRegulator]]


class CreateProfileBusiness(BaseModel):
    r"""Describes the fields available when creating a business."""

    legal_business_name: Annotated[str, pydantic.Field(alias="legalBusinessName")]

    doing_business_as: Annotated[
        Optional[str], pydantic.Field(alias="doingBusinessAs")
    ] = None

    business_type: Annotated[
        OptionalNullable[CreateProfileBusinessType],
        pydantic.Field(alias="businessType"),
    ] = UNSET

    address: OptionalNullable[CreateProfileBusinessAddress] = UNSET

    phone: OptionalNullable[CreateProfileBusinessPhone] = UNSET

    email: Optional[str] = None
    r"""Email address."""

    website: Optional[str] = None

    description: Optional[str] = None

    tax_id: Annotated[OptionalNullable[TaxID], pydantic.Field(alias="taxID")] = UNSET

    industry_codes: Annotated[
        OptionalNullable[CreateProfileIndustryCodes],
        pydantic.Field(alias="industryCodes"),
    ] = UNSET

    primary_regulator: Annotated[
        OptionalNullable[CreateProfilePrimaryRegulator],
        pydantic.Field(alias="primaryRegulator"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "doingBusinessAs",
            "businessType",
            "address",
            "phone",
            "email",
            "website",
            "description",
            "taxID",
            "industryCodes",
            "primaryRegulator",
        ]
        nullable_fields = [
            "businessType",
            "address",
            "phone",
            "taxID",
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


class CreateProfileTypedDict(TypedDict):
    r"""Describes the fields available when creating a profile.
    If `accountType` is set to `individual`, the `individual` object should be completed. All others should populate `business`.

    """

    individual: NotRequired[Nullable[CreateProfileIndividualTypedDict]]
    business: NotRequired[Nullable[CreateProfileBusinessTypedDict]]


class CreateProfile(BaseModel):
    r"""Describes the fields available when creating a profile.
    If `accountType` is set to `individual`, the `individual` object should be completed. All others should populate `business`.

    """

    individual: OptionalNullable[CreateProfileIndividual] = UNSET

    business: OptionalNullable[CreateProfileBusiness] = UNSET

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
