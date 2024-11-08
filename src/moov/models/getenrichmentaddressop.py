"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .enrichmentaddress import EnrichmentAddress, EnrichmentAddressTypedDict
from moov.types import BaseModel
from moov.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class GetEnrichmentAddressRequestTypedDict(TypedDict):
    search: str
    r"""Partial or complete address to search.

    """
    max_results: NotRequired[int]
    r"""Maximum number of results to return.

    """
    include_cities: NotRequired[str]
    r"""Limits results to a list of given cities.

    """
    include_states: NotRequired[str]
    r"""Limits results to a list of given states.

    """
    include_zipcodes: NotRequired[str]
    r"""Limits results to a list of given zipcodes.

    """
    exclude_states: NotRequired[str]
    r"""Exclude list of states from results. No `include` pararmeters may be used with this parameter.

    """
    prefer_cities: NotRequired[str]
    r"""Display results with the listed cities at the top.

    """
    prefer_states: NotRequired[str]
    r"""Display results with the listed states at the top.

    """
    prefer_zipcodes: NotRequired[str]
    r"""Display results with the listed zipcodes at the top.

    """
    prefer_ratio: NotRequired[int]
    r"""Specifies the percentage of address suggestions that should be preferred and will appear at the top of the results.

    """
    prefer_geolocation: NotRequired[str]
    r"""If omitted or set to `city` it uses the sender's IP address to determine location, then automatically adds the city and state to the preferCities value. This parameter takes precedence over other `include` or `exclude` parameters meaning that if it is not set to `none` you may see addresses from areas you do not wish to see.

    """
    selected: NotRequired[str]
    r"""Useful for narrowing results with `addressLine2` suggestions such as `Apt` (denotes an apartment building with multiple residences).

    """
    source: NotRequired[str]
    r"""Include results from alternate data sources. Allowed values are -- `all` (non-postal addresses) or `postal` (postal addresses only).

    """


class GetEnrichmentAddressRequest(BaseModel):
    search: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Partial or complete address to search.

    """

    max_results: Annotated[
        Optional[int],
        pydantic.Field(alias="maxResults"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Maximum number of results to return.

    """

    include_cities: Annotated[
        Optional[str],
        pydantic.Field(alias="includeCities"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limits results to a list of given cities.

    """

    include_states: Annotated[
        Optional[str],
        pydantic.Field(alias="includeStates"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limits results to a list of given states.

    """

    include_zipcodes: Annotated[
        Optional[str],
        pydantic.Field(alias="includeZipcodes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Limits results to a list of given zipcodes.

    """

    exclude_states: Annotated[
        Optional[str],
        pydantic.Field(alias="excludeStates"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exclude list of states from results. No `include` pararmeters may be used with this parameter.

    """

    prefer_cities: Annotated[
        Optional[str],
        pydantic.Field(alias="preferCities"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Display results with the listed cities at the top.

    """

    prefer_states: Annotated[
        Optional[str],
        pydantic.Field(alias="preferStates"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Display results with the listed states at the top.

    """

    prefer_zipcodes: Annotated[
        Optional[str],
        pydantic.Field(alias="preferZipcodes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Display results with the listed zipcodes at the top.

    """

    prefer_ratio: Annotated[
        Optional[int],
        pydantic.Field(alias="preferRatio"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Specifies the percentage of address suggestions that should be preferred and will appear at the top of the results.

    """

    prefer_geolocation: Annotated[
        Optional[str],
        pydantic.Field(alias="preferGeolocation"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If omitted or set to `city` it uses the sender's IP address to determine location, then automatically adds the city and state to the preferCities value. This parameter takes precedence over other `include` or `exclude` parameters meaning that if it is not set to `none` you may see addresses from areas you do not wish to see.

    """

    selected: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Useful for narrowing results with `addressLine2` suggestions such as `Apt` (denotes an apartment building with multiple residences).

    """

    source: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include results from alternate data sources. Allowed values are -- `all` (non-postal addresses) or `postal` (postal addresses only).

    """


GetEnrichmentAddressResponseResultTypedDict = Union[
    List[EnrichmentAddressTypedDict], str
]


GetEnrichmentAddressResponseResult = Union[List[EnrichmentAddress], str]


class GetEnrichmentAddressResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetEnrichmentAddressResponseResultTypedDict


class GetEnrichmentAddressResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetEnrichmentAddressResponseResult
