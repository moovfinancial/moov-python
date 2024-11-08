"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .returnpolicy import ReturnPolicy
from .underwritingstatus import UnderwritingStatus
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VolumeByCustomerTypeTypedDict(TypedDict):
    business_to_business_percentage: NotRequired[int]
    consumer_to_business_percentage: NotRequired[int]


class VolumeByCustomerType(BaseModel):
    business_to_business_percentage: Annotated[
        Optional[int], pydantic.Field(alias="businessToBusinessPercentage")
    ] = None

    consumer_to_business_percentage: Annotated[
        Optional[int], pydantic.Field(alias="consumerToBusinessPercentage")
    ] = None


class CardVolumeDistributionTypedDict(TypedDict):
    ecommerce_percentage: NotRequired[int]
    card_present_percentage: NotRequired[int]
    mail_or_phone_percentage: NotRequired[int]
    debt_repayment_percentage: NotRequired[int]


class CardVolumeDistribution(BaseModel):
    ecommerce_percentage: Annotated[
        Optional[int], pydantic.Field(alias="ecommercePercentage")
    ] = None

    card_present_percentage: Annotated[
        Optional[int], pydantic.Field(alias="cardPresentPercentage")
    ] = None

    mail_or_phone_percentage: Annotated[
        Optional[int], pydantic.Field(alias="mailOrPhonePercentage")
    ] = None

    debt_repayment_percentage: Annotated[
        Optional[int], pydantic.Field(alias="debtRepaymentPercentage")
    ] = None


class FulfillmentTypedDict(TypedDict):
    has_physical_goods: NotRequired[bool]
    is_shipping_product: NotRequired[bool]
    shipment_duration_days: NotRequired[int]
    return_policy: NotRequired[ReturnPolicy]
    r"""Describes the return policy."""


class Fulfillment(BaseModel):
    has_physical_goods: Annotated[
        Optional[bool], pydantic.Field(alias="hasPhysicalGoods")
    ] = None

    is_shipping_product: Annotated[
        Optional[bool], pydantic.Field(alias="isShippingProduct")
    ] = None

    shipment_duration_days: Annotated[
        Optional[int], pydantic.Field(alias="shipmentDurationDays")
    ] = None

    return_policy: Annotated[
        Optional[ReturnPolicy], pydantic.Field(alias="returnPolicy")
    ] = None
    r"""Describes the return policy."""


class UnderwritingTypedDict(TypedDict):
    r"""Describes underwriting values (in USD) used for card payment acceptance."""

    average_transaction_size: NotRequired[int]
    max_transaction_size: NotRequired[int]
    average_monthly_transaction_volume: NotRequired[int]
    status: NotRequired[UnderwritingStatus]
    r"""This field is deprecated and will be removed in a future release."""
    volume_by_customer_type: NotRequired[VolumeByCustomerTypeTypedDict]
    card_volume_distribution: NotRequired[CardVolumeDistributionTypedDict]
    fulfillment: NotRequired[FulfillmentTypedDict]


class Underwriting(BaseModel):
    r"""Describes underwriting values (in USD) used for card payment acceptance."""

    average_transaction_size: Annotated[
        Optional[int], pydantic.Field(alias="averageTransactionSize")
    ] = None

    max_transaction_size: Annotated[
        Optional[int], pydantic.Field(alias="maxTransactionSize")
    ] = None

    average_monthly_transaction_volume: Annotated[
        Optional[int], pydantic.Field(alias="averageMonthlyTransactionVolume")
    ] = None

    status: Annotated[
        Optional[UnderwritingStatus],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""This field is deprecated and will be removed in a future release."""

    volume_by_customer_type: Annotated[
        Optional[VolumeByCustomerType], pydantic.Field(alias="volumeByCustomerType")
    ] = None

    card_volume_distribution: Annotated[
        Optional[CardVolumeDistribution], pydantic.Field(alias="cardVolumeDistribution")
    ] = None

    fulfillment: Optional[Fulfillment] = None
