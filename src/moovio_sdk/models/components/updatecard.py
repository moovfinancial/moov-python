"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .e2eetokenupdate import E2EETokenUpdate, E2EETokenUpdateTypedDict
from .updatecardaddress import UpdateCardAddress, UpdateCardAddressTypedDict
from .updatecardexpiration import UpdateCardExpiration, UpdateCardExpirationTypedDict
from moovio_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateCardTypedDict(TypedDict):
    e2ee: NotRequired[E2EETokenUpdateTypedDict]
    r"""Wraps a compact-serialized JSON Web Encryption (JWE) token used for secure transmission of sensitive data (e.g., PCI information) through intermediaries.
    This token is encrypted using the public key from /end-to-end-keys and wraps an AES key. For details and examples, refer to our
    [GitHub repository](https://github.com/moovfinancial/moov-go/blob/main/examples/e2ee/e2ee_test.go).
    """
    billing_address: NotRequired[UpdateCardAddressTypedDict]
    expiration: NotRequired[UpdateCardExpirationTypedDict]
    card_cvv: NotRequired[str]
    card_on_file: NotRequired[bool]
    merchant_account_id: NotRequired[str]
    verify_name: NotRequired[bool]
    holder_name: NotRequired[str]


class UpdateCard(BaseModel):
    e2ee: Optional[E2EETokenUpdate] = None
    r"""Wraps a compact-serialized JSON Web Encryption (JWE) token used for secure transmission of sensitive data (e.g., PCI information) through intermediaries.
    This token is encrypted using the public key from /end-to-end-keys and wraps an AES key. For details and examples, refer to our
    [GitHub repository](https://github.com/moovfinancial/moov-go/blob/main/examples/e2ee/e2ee_test.go).
    """

    billing_address: Annotated[
        Optional[UpdateCardAddress], pydantic.Field(alias="billingAddress")
    ] = None

    expiration: Optional[UpdateCardExpiration] = None

    card_cvv: Annotated[Optional[str], pydantic.Field(alias="cardCvv")] = None

    card_on_file: Annotated[Optional[bool], pydantic.Field(alias="cardOnFile")] = None

    merchant_account_id: Annotated[
        Optional[str], pydantic.Field(alias="merchantAccountID")
    ] = None

    verify_name: Annotated[Optional[bool], pydantic.Field(alias="verifyName")] = None

    holder_name: Annotated[Optional[str], pydantic.Field(alias="holderName")] = None
