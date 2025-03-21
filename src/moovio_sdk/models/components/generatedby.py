"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .generatedbyaccountid import GeneratedByAccountID, GeneratedByAccountIDTypedDict
from .generatedbybankaccountid import (
    GeneratedByBankAccountID,
    GeneratedByBankAccountIDTypedDict,
)
from .generatedbycardid import GeneratedByCardID, GeneratedByCardIDTypedDict
from .generatedbydisputeid import GeneratedByDisputeID, GeneratedByDisputeIDTypedDict
from .generatedbytransferid import GeneratedByTransferID, GeneratedByTransferIDTypedDict
from typing import Union
from typing_extensions import TypeAliasType


GeneratedByTypedDict = TypeAliasType(
    "GeneratedByTypedDict",
    Union[
        GeneratedByTransferIDTypedDict,
        GeneratedByCardIDTypedDict,
        GeneratedByDisputeIDTypedDict,
        GeneratedByAccountIDTypedDict,
        GeneratedByBankAccountIDTypedDict,
    ],
)
r"""The entity that generated the fee."""


GeneratedBy = TypeAliasType(
    "GeneratedBy",
    Union[
        GeneratedByTransferID,
        GeneratedByCardID,
        GeneratedByDisputeID,
        GeneratedByAccountID,
        GeneratedByBankAccountID,
    ],
)
r"""The entity that generated the fee."""
