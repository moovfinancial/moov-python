"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .amount import Amount, AmountTypedDict
from .cancellation import Cancellation, CancellationTypedDict
from .cardacquiringdispute import CardAcquiringDispute, CardAcquiringDisputeTypedDict
from .cardacquiringrefund import CardAcquiringRefund, CardAcquiringRefundTypedDict
from .facilitatorfee import FacilitatorFee, FacilitatorFeeTypedDict
from .moovfeedetails import MoovFeeDetails, MoovFeeDetailsTypedDict
from .transferdestination import TransferDestination, TransferDestinationTypedDict
from .transferfailurereason import TransferFailureReason
from .transfersource import TransferSource, TransferSourceTypedDict
from .transferstatus import TransferStatus
from datetime import datetime
from moovio_sdk.types import BaseModel
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreatedTransferTypedDict(TypedDict):
    transfer_id: str
    created_on: datetime
    source: NotRequired[TransferSourceTypedDict]
    destination: NotRequired[TransferDestinationTypedDict]
    completed_on: NotRequired[datetime]
    status: NotRequired[TransferStatus]
    r"""Status of a transfer."""
    failure_reason: NotRequired[TransferFailureReason]
    r"""Reason for a transfer's failure."""
    amount: NotRequired[AmountTypedDict]
    description: NotRequired[str]
    r"""An optional description of the transfer that is used on receipts and for your own internal use."""
    metadata: NotRequired[Dict[str, str]]
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""
    facilitator_fee: NotRequired[FacilitatorFeeTypedDict]
    r"""Total or markup fee."""
    moov_fee: NotRequired[int]
    r"""Fees charged to your platform account for transfers."""
    moov_fee_decimal: NotRequired[str]
    r"""Same as `moovFee`, but a decimal-formatted numerical string that represents up to 9 decimal place precision."""
    moov_fee_details: NotRequired[MoovFeeDetailsTypedDict]
    r"""Processing and pass-through costs that add up to the moovFee."""
    group_id: NotRequired[str]
    cancellations: NotRequired[List[CancellationTypedDict]]
    refunded_amount: NotRequired[AmountTypedDict]
    refunds: NotRequired[List[CardAcquiringRefundTypedDict]]
    disputed_amount: NotRequired[AmountTypedDict]
    disputes: NotRequired[List[CardAcquiringDisputeTypedDict]]
    sweep_id: NotRequired[str]
    schedule_id: NotRequired[str]
    occurrence_id: NotRequired[str]
    payment_link_code: NotRequired[str]
    sales_tax_amount: NotRequired[AmountTypedDict]
    r"""Optional sales tax amount. `transfer.amount.value` should be inclusive of any sales tax and represents the total amount charged."""
    foreign_id: NotRequired[str]
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""


class CreatedTransfer(BaseModel):
    transfer_id: Annotated[str, pydantic.Field(alias="transferID")]

    created_on: Annotated[datetime, pydantic.Field(alias="createdOn")]

    source: Optional[TransferSource] = None

    destination: Optional[TransferDestination] = None

    completed_on: Annotated[Optional[datetime], pydantic.Field(alias="completedOn")] = (
        None
    )

    status: Optional[TransferStatus] = None
    r"""Status of a transfer."""

    failure_reason: Annotated[
        Optional[TransferFailureReason], pydantic.Field(alias="failureReason")
    ] = None
    r"""Reason for a transfer's failure."""

    amount: Optional[Amount] = None

    description: Optional[str] = None
    r"""An optional description of the transfer that is used on receipts and for your own internal use."""

    metadata: Optional[Dict[str, str]] = None
    r"""Free-form key-value pair list. Useful for storing information that is not captured elsewhere."""

    facilitator_fee: Annotated[
        Optional[FacilitatorFee], pydantic.Field(alias="facilitatorFee")
    ] = None
    r"""Total or markup fee."""

    moov_fee: Annotated[Optional[int], pydantic.Field(alias="moovFee")] = None
    r"""Fees charged to your platform account for transfers."""

    moov_fee_decimal: Annotated[
        Optional[str], pydantic.Field(alias="moovFeeDecimal")
    ] = None
    r"""Same as `moovFee`, but a decimal-formatted numerical string that represents up to 9 decimal place precision."""

    moov_fee_details: Annotated[
        Optional[MoovFeeDetails], pydantic.Field(alias="moovFeeDetails")
    ] = None
    r"""Processing and pass-through costs that add up to the moovFee."""

    group_id: Annotated[Optional[str], pydantic.Field(alias="groupID")] = None

    cancellations: Optional[List[Cancellation]] = None

    refunded_amount: Annotated[
        Optional[Amount], pydantic.Field(alias="refundedAmount")
    ] = None

    refunds: Optional[List[CardAcquiringRefund]] = None

    disputed_amount: Annotated[
        Optional[Amount], pydantic.Field(alias="disputedAmount")
    ] = None

    disputes: Optional[List[CardAcquiringDispute]] = None

    sweep_id: Annotated[Optional[str], pydantic.Field(alias="sweepID")] = None

    schedule_id: Annotated[Optional[str], pydantic.Field(alias="scheduleID")] = None

    occurrence_id: Annotated[Optional[str], pydantic.Field(alias="occurrenceID")] = None

    payment_link_code: Annotated[
        Optional[str], pydantic.Field(alias="paymentLinkCode")
    ] = None

    sales_tax_amount: Annotated[
        Optional[Amount], pydantic.Field(alias="salesTaxAmount")
    ] = None
    r"""Optional sales tax amount. `transfer.amount.value` should be inclusive of any sales tax and represents the total amount charged."""

    foreign_id: Annotated[Optional[str], pydantic.Field(alias="foreignID")] = None
    r"""Optional alias from a foreign/external system which can be used to reference this resource."""
