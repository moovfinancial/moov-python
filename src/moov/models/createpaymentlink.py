"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .paymentlinkcustomeroptions import (
    PaymentLinkCustomerOptions,
    PaymentLinkCustomerOptionsTypedDict,
)
from .paymentlinkdisplayoptions import (
    PaymentLinkDisplayOptions,
    PaymentLinkDisplayOptionsTypedDict,
)
from .paymentlinkpaymentdetails import (
    PaymentLinkPaymentDetails,
    PaymentLinkPaymentDetailsTypedDict,
)
from .paymentlinkpayoutdetails import (
    PaymentLinkPayoutDetails,
    PaymentLinkPayoutDetailsTypedDict,
)
from datetime import datetime
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreatePaymentLinkTypedDict(TypedDict):
    r"""Request to create a new payment link.

    A payment link must include either `payment` or `payout` details, but not both. For payout payment links,
    `maxUses` will automatically be set to 1, as these are intended for a one-time disbursement
    to a specific recipient.

    **Note:** The `payout` option is currently under development and is not yet available for general use.
    """

    partner_account_id: str
    r"""The partner's Moov account ID."""
    merchant_payment_method_id: str
    r"""The merchant's preferred payment method ID. Must be a wallet payment method."""
    amount: AmountTypedDict
    display: PaymentLinkDisplayOptionsTypedDict
    r"""Customizable display options for a payment link."""
    max_uses: NotRequired[int]
    r"""An optional limit on the number of times this payment link can be used.

    **For payouts, `maxUses` is always 1.**
    """
    expires_on: NotRequired[datetime]
    r"""An optional expiration date for this payment link."""
    customer: NotRequired[PaymentLinkCustomerOptionsTypedDict]
    payment: NotRequired[PaymentLinkPaymentDetailsTypedDict]
    r"""Options for payment links used to collect payment."""
    payout: NotRequired[PaymentLinkPayoutDetailsTypedDict]


class CreatePaymentLink(BaseModel):
    r"""Request to create a new payment link.

    A payment link must include either `payment` or `payout` details, but not both. For payout payment links,
    `maxUses` will automatically be set to 1, as these are intended for a one-time disbursement
    to a specific recipient.

    **Note:** The `payout` option is currently under development and is not yet available for general use.
    """

    partner_account_id: Annotated[str, pydantic.Field(alias="partnerAccountID")]
    r"""The partner's Moov account ID."""

    merchant_payment_method_id: Annotated[
        str, pydantic.Field(alias="merchantPaymentMethodID")
    ]
    r"""The merchant's preferred payment method ID. Must be a wallet payment method."""

    amount: Amount

    display: PaymentLinkDisplayOptions
    r"""Customizable display options for a payment link."""

    max_uses: Annotated[Optional[int], pydantic.Field(alias="maxUses")] = None
    r"""An optional limit on the number of times this payment link can be used.

    **For payouts, `maxUses` is always 1.**
    """

    expires_on: Annotated[Optional[datetime], pydantic.Field(alias="expiresOn")] = None
    r"""An optional expiration date for this payment link."""

    customer: Optional[PaymentLinkCustomerOptions] = None

    payment: Optional[PaymentLinkPaymentDetails] = None
    r"""Options for payment links used to collect payment."""

    payout: Optional[PaymentLinkPayoutDetails] = None
