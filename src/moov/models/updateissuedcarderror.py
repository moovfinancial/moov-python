"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createauthorizedusererror import CreateAuthorizedUserError
from moov import utils
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated


class UpdateIssuedCardErrorData(BaseModel):
    state: Optional[str] = None

    memo: Optional[str] = None

    authorized_user: Annotated[
        Optional[CreateAuthorizedUserError], pydantic.Field(alias="authorizedUser")
    ] = None


class UpdateIssuedCardError(Exception):
    data: UpdateIssuedCardErrorData

    def __init__(self, data: UpdateIssuedCardErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UpdateIssuedCardErrorData)
