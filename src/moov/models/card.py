"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .basicpaymentmethod import BasicPaymentMethod, BasicPaymentMethodTypedDict
from .cardaccountupdater import CardAccountUpdater, CardAccountUpdaterTypedDict
from .cardexpiration import CardExpiration, CardExpirationTypedDict
from .cardtype import CardType
from enum import Enum
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Brand(str, Enum):
    r"""The card brand."""

    AMERICAN_EXPRESS = "American Express"
    DISCOVER = "Discover"
    MASTERCARD = "Mastercard"
    VISA = "Visa"


class Cvv(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class AddressLine1(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class PostalCode(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class FirstName(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class LastName(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class MiddleName(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class FullName(str, Enum):
    NO_MATCH = "noMatch"
    MATCH = "match"
    NOT_CHECKED = "notChecked"
    UNAVAILABLE = "unavailable"
    PARTIAL_MATCH = "partialMatch"


class AccountNameTypedDict(TypedDict):
    r"""The results of submitting cardholder name to a card network for verification."""

    first_name: NotRequired[FirstName]
    last_name: NotRequired[LastName]
    middle_name: NotRequired[MiddleName]
    full_name: NotRequired[FullName]


class AccountName(BaseModel):
    r"""The results of submitting cardholder name to a card network for verification."""

    first_name: Annotated[Optional[FirstName], pydantic.Field(alias="firstName")] = None

    last_name: Annotated[Optional[LastName], pydantic.Field(alias="lastName")] = None

    middle_name: Annotated[Optional[MiddleName], pydantic.Field(alias="middleName")] = (
        None
    )

    full_name: Annotated[Optional[FullName], pydantic.Field(alias="fullName")] = None


class CardVerificationTypedDict(TypedDict):
    r"""The results of submitting cardholder data to a card network for verification."""

    cvv: NotRequired[Cvv]
    address_line1: NotRequired[AddressLine1]
    postal_code: NotRequired[PostalCode]
    account_name: NotRequired[AccountNameTypedDict]


class CardVerification(BaseModel):
    r"""The results of submitting cardholder data to a card network for verification."""

    cvv: Optional[Cvv] = None

    address_line1: Annotated[
        Optional[AddressLine1], pydantic.Field(alias="addressLine1")
    ] = None

    postal_code: Annotated[Optional[PostalCode], pydantic.Field(alias="postalCode")] = (
        None
    )

    account_name: Annotated[
        Optional[AccountName], pydantic.Field(alias="accountName")
    ] = None


class DomesticPushToCard(str, Enum):
    r"""Indicates which level of domestic push-to-card transfer is supported by the card, if any."""

    NOT_SUPPORTED = "not-supported"
    STANDARD = "standard"
    FAST_FUNDS = "fast-funds"
    UNKNOWN = "unknown"


class DomesticPullFromCard(str, Enum):
    r"""Indicates if the card supports domestic pull-from-card transfer."""

    NOT_SUPPORTED = "not-supported"
    SUPPORTED = "supported"
    UNKNOWN = "unknown"


class CardTypedDict(TypedDict):
    r"""Describes a card on a Moov account."""

    card_id: NotRequired[str]
    r"""UUID v4"""
    fingerprint: NotRequired[str]
    r"""Uniquely identifies a linked payment card or token.
    For Apple Pay, the fingerprint is based on the tokenized card number and may vary based on the user's device.
    This field can be used to identify specific payment methods across multiple accounts on your platform.

    """
    brand: NotRequired[Brand]
    card_type: NotRequired[CardType]
    r"""The type of the card."""
    card_category: NotRequired[str]
    r"""The category or level of the card defined by the issuer. Examples include, but not limited to \"REWARDS\", \"TRADITIONAL REWARDS\", \"CLASSIC\", and \"CORPORATE PURCHASING\"."""
    last_four_card_number: NotRequired[str]
    r"""Last four digits of the card number"""
    bin: NotRequired[str]
    r"""The first six to eight digits of the card number, which identifies the financial institution that issued the card."""
    expiration: NotRequired[CardExpirationTypedDict]
    r"""The expiration date of the card or token."""
    holder_name: NotRequired[str]
    r"""The name of the cardholder as it appears on the card."""
    billing_address: NotRequired[AddressTypedDict]
    card_verification: NotRequired[CardVerificationTypedDict]
    issuer: NotRequired[str]
    r"""Financial institution that issued the card."""
    issuer_country: NotRequired[str]
    r"""Country where the card was issued."""
    issuer_url: NotRequired[str]
    r"""URL of the issuer."""
    issuer_phone: NotRequired[str]
    r"""Phone number of the issuer."""
    commercial: NotRequired[Nullable[bool]]
    r"""If true, the card is for commercial use, or associated with a business. If false, the card is associated with a general consumer."""
    regulated: NotRequired[Nullable[bool]]
    r"""If true, the card issuing bank is regulated, and the scheme fees for debit transactions will be limited based on the Durbin Amendment. If false, the card issuing bank is not regulated, and the scheme fees will not be limited."""
    card_on_file: NotRequired[bool]
    r"""Indicates cardholder has authorized card to be stored for future payments."""
    merchant_account_id: NotRequired[str]
    r"""ID of the Moov account acting as a merchant or other entity authorized to store the card.
    Defaults to your platform account ID if cardOnFile is set to true and no other account is provided.

    """
    card_account_updater: NotRequired[CardAccountUpdaterTypedDict]
    r"""The results of the most recent card update request."""
    domestic_push_to_card: NotRequired[DomesticPushToCard]
    domestic_pull_from_card: NotRequired[DomesticPullFromCard]
    payment_methods: NotRequired[List[BasicPaymentMethodTypedDict]]
    r"""Includes any payment methods generated for a newly linked card, removing the need to
    call the List Payment Methods endpoint following a successful Link Card request.

    **NOTE: This field is only populated for Link Card requests made with the `X-Wait-For` header.**

    """


class Card(BaseModel):
    r"""Describes a card on a Moov account."""

    card_id: Annotated[Optional[str], pydantic.Field(alias="cardID")] = None
    r"""UUID v4"""

    fingerprint: Optional[str] = None
    r"""Uniquely identifies a linked payment card or token.
    For Apple Pay, the fingerprint is based on the tokenized card number and may vary based on the user's device.
    This field can be used to identify specific payment methods across multiple accounts on your platform.

    """

    brand: Optional[Brand] = None

    card_type: Annotated[Optional[CardType], pydantic.Field(alias="cardType")] = None
    r"""The type of the card."""

    card_category: Annotated[Optional[str], pydantic.Field(alias="cardCategory")] = None
    r"""The category or level of the card defined by the issuer. Examples include, but not limited to \"REWARDS\", \"TRADITIONAL REWARDS\", \"CLASSIC\", and \"CORPORATE PURCHASING\"."""

    last_four_card_number: Annotated[
        Optional[str], pydantic.Field(alias="lastFourCardNumber")
    ] = None
    r"""Last four digits of the card number"""

    bin: Optional[str] = None
    r"""The first six to eight digits of the card number, which identifies the financial institution that issued the card."""

    expiration: Optional[CardExpiration] = None
    r"""The expiration date of the card or token."""

    holder_name: Annotated[Optional[str], pydantic.Field(alias="holderName")] = None
    r"""The name of the cardholder as it appears on the card."""

    billing_address: Annotated[
        Optional[Address], pydantic.Field(alias="billingAddress")
    ] = None

    card_verification: Annotated[
        Optional[CardVerification], pydantic.Field(alias="cardVerification")
    ] = None

    issuer: Optional[str] = None
    r"""Financial institution that issued the card."""

    issuer_country: Annotated[Optional[str], pydantic.Field(alias="issuerCountry")] = (
        None
    )
    r"""Country where the card was issued."""

    issuer_url: Annotated[Optional[str], pydantic.Field(alias="issuerURL")] = None
    r"""URL of the issuer."""

    issuer_phone: Annotated[Optional[str], pydantic.Field(alias="issuerPhone")] = None
    r"""Phone number of the issuer."""

    commercial: OptionalNullable[bool] = UNSET
    r"""If true, the card is for commercial use, or associated with a business. If false, the card is associated with a general consumer."""

    regulated: OptionalNullable[bool] = UNSET
    r"""If true, the card issuing bank is regulated, and the scheme fees for debit transactions will be limited based on the Durbin Amendment. If false, the card issuing bank is not regulated, and the scheme fees will not be limited."""

    card_on_file: Annotated[Optional[bool], pydantic.Field(alias="cardOnFile")] = False
    r"""Indicates cardholder has authorized card to be stored for future payments."""

    merchant_account_id: Annotated[
        Optional[str], pydantic.Field(alias="merchantAccountID")
    ] = None
    r"""ID of the Moov account acting as a merchant or other entity authorized to store the card.
    Defaults to your platform account ID if cardOnFile is set to true and no other account is provided.

    """

    card_account_updater: Annotated[
        Optional[CardAccountUpdater], pydantic.Field(alias="cardAccountUpdater")
    ] = None
    r"""The results of the most recent card update request."""

    domestic_push_to_card: Annotated[
        Optional[DomesticPushToCard], pydantic.Field(alias="domesticPushToCard")
    ] = None

    domestic_pull_from_card: Annotated[
        Optional[DomesticPullFromCard], pydantic.Field(alias="domesticPullFromCard")
    ] = None

    payment_methods: Annotated[
        Optional[List[BasicPaymentMethod]], pydantic.Field(alias="paymentMethods")
    ] = None
    r"""Includes any payment methods generated for a newly linked card, removing the need to
    call the List Payment Methods endpoint following a successful Link Card request.

    **NOTE: This field is only populated for Link Card requests made with the `X-Wait-For` header.**

    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "cardID",
            "fingerprint",
            "brand",
            "cardType",
            "cardCategory",
            "lastFourCardNumber",
            "bin",
            "expiration",
            "holderName",
            "billingAddress",
            "cardVerification",
            "issuer",
            "issuerCountry",
            "issuerURL",
            "issuerPhone",
            "commercial",
            "regulated",
            "cardOnFile",
            "merchantAccountID",
            "cardAccountUpdater",
            "domesticPushToCard",
            "domesticPullFromCard",
            "paymentMethods",
        ]
        nullable_fields = ["commercial", "regulated"]
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