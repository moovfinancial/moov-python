"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class LinkApplePaymentMethodTypedDict(TypedDict):
    r"""Provides information about the underlying card.

    Refer to [Apple's documentation](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymenttoken/1916113-paymentmethod)
    for more information.
    """

    display_name: str
    r"""A display-friendly discription of the card."""
    network: str
    r"""The card's payment network."""
    type: str
    r"""The type of card."""


class LinkApplePaymentMethod(BaseModel):
    r"""Provides information about the underlying card.

    Refer to [Apple's documentation](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymenttoken/1916113-paymentmethod)
    for more information.
    """

    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""A display-friendly discription of the card."""

    network: str
    r"""The card's payment network."""

    type: str
    r"""The type of card."""
