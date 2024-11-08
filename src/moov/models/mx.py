"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .mxauthorizationcode import MXAuthorizationCode, MXAuthorizationCodeTypedDict
from moov.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class MxTypedDict(TypedDict):
    r"""Describes the account to link to the Moov account using a MX processor token. <br><br> `sandbox` - When linking a bank account to a `sandbox` account using an MX authorization token a default bank account routing number will be used. The following default data will be used to generate the bank account in this flow:
    ```
    RoutingNumber: \"123456780\",
    BankName: \"Gringotts Bank\"
    ```

    """

    mx: NotRequired[Nullable[MXAuthorizationCodeTypedDict]]
    r"""The authorization code of a MX account which allows a processor to retrieve a linked payment account. <br><br> `sandbox` - When linking a bank account to a `sandbox` account using a MX authorization code it will utilize MX's sandbox environment. The MX authorization code provided must be generated from MX's sandbox environment."""


class Mx(BaseModel):
    r"""Describes the account to link to the Moov account using a MX processor token. <br><br> `sandbox` - When linking a bank account to a `sandbox` account using an MX authorization token a default bank account routing number will be used. The following default data will be used to generate the bank account in this flow:
    ```
    RoutingNumber: \"123456780\",
    BankName: \"Gringotts Bank\"
    ```

    """

    mx: OptionalNullable[MXAuthorizationCode] = UNSET
    r"""The authorization code of a MX account which allows a processor to retrieve a linked payment account. <br><br> `sandbox` - When linking a bank account to a `sandbox` account using a MX authorization code it will utilize MX's sandbox environment. The MX authorization code provided must be generated from MX's sandbox environment."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["mx"]
        nullable_fields = ["mx"]
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
