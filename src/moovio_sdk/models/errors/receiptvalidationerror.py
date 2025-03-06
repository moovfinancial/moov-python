"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moovio_sdk import utils
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class ReceiptValidationErrorData(BaseModel):
    kind: Optional[str] = None

    email: Optional[str] = None

    email_account_id: Annotated[
        Optional[str], pydantic.Field(alias="emailAccountID")
    ] = None

    for_transfer_id: Annotated[Optional[str], pydantic.Field(alias="forTransferID")] = (
        None
    )

    for_schedule_id: Annotated[Optional[str], pydantic.Field(alias="forScheduleID")] = (
        None
    )

    for_occurrence_id: Annotated[
        Optional[str], pydantic.Field(alias="forOccurrenceID")
    ] = None


class ReceiptValidationError(Exception):
    data: ReceiptValidationErrorData

    def __init__(self, data: ReceiptValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ReceiptValidationErrorData)
