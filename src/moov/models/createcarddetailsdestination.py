"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from moov.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateCardDetailsDestinationTypedDict(TypedDict):
    r"""If transfer involves card acceptance, override default card acceptance properties."""

    dynamic_descriptor: NotRequired[str]
    r"""An optional override of the default card statement descriptor for a transfer. Accounts must be enabled by Moov to set this field.

    """


class CreateCardDetailsDestination(BaseModel):
    r"""If transfer involves card acceptance, override default card acceptance properties."""

    dynamic_descriptor: Annotated[
        Optional[str], pydantic.Field(alias="dynamicDescriptor")
    ] = None
    r"""An optional override of the default card statement descriptor for a transfer. Accounts must be enabled by Moov to set this field.

    """
