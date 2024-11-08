"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .rolepolicy import RolePolicy, RolePolicyTypedDict
from moov.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CreateRoleTypedDict(TypedDict):
    r"""Arguments to create a new role."""

    name: str
    r"""Descriptive name allowing spaces."""
    subjects: List[str]
    policies: List[RolePolicyTypedDict]


class CreateRole(BaseModel):
    r"""Arguments to create a new role."""

    name: str
    r"""Descriptive name allowing spaces."""

    subjects: List[str]

    policies: List[RolePolicy]
