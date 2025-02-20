"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from moovio_sdk import utils
from moovio_sdk._hooks import HookContext
from moovio_sdk.models import components, errors, operations
from moovio_sdk.types import OptionalNullable, UNSET
from moovio_sdk.utils import get_security_from_env
from typing import Mapping, Optional


class EnrichedAddress(BaseSDK):
    def get(
        self,
        *,
        search: str,
        max_results: Optional[int] = None,
        include_cities: Optional[str] = None,
        include_states: Optional[str] = None,
        include_zipcodes: Optional[str] = None,
        exclude_states: Optional[str] = None,
        prefer_cities: Optional[str] = None,
        prefer_states: Optional[str] = None,
        prefer_zipcodes: Optional[str] = None,
        prefer_ratio: Optional[int] = None,
        prefer_geolocation: Optional[str] = None,
        selected: Optional[str] = None,
        source: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetEnrichmentAddressResponse:
        r"""Fetch enriched address suggestions. Requires a partial address.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/profile-enrichment.read` scope.

        :param search: Partial or complete address to search.
        :param max_results: Maximum number of results to return.
        :param include_cities: Limits results to a list of given cities.
        :param include_states: Limits results to a list of given states.
        :param include_zipcodes: Limits results to a list of given zipcodes.
        :param exclude_states: Exclude list of states from results. No `include` pararmeters may be used with this parameter.
        :param prefer_cities: Display results with the listed cities at the top.
        :param prefer_states: Display results with the listed states at the top.
        :param prefer_zipcodes: Display results with the listed zipcodes at the top.
        :param prefer_ratio: Specifies the percentage of address suggestions that should be preferred and will appear at the top of the results.
        :param prefer_geolocation: If omitted or set to `city`, it uses the sender's IP address to determine location, then automatically adds the city and state    to the preferCities value. This parameter takes precedence over other `include` or `exclude` parameters meaning that if it is    not set to `none`, you may see addresses from areas you do not wish to see.
        :param selected: Useful for narrowing results with `addressLine2` suggestions such as `Apt` (denotes an apartment building with multiple residences).
        :param source: Include results from alternate data sources. Allowed values are `all` (non-postal addresses), or `postal` (postal addresses only).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = operations.GetEnrichmentAddressRequest(
            search=search,
            max_results=max_results,
            include_cities=include_cities,
            include_states=include_states,
            include_zipcodes=include_zipcodes,
            exclude_states=exclude_states,
            prefer_cities=prefer_cities,
            prefer_states=prefer_states,
            prefer_zipcodes=prefer_zipcodes,
            prefer_ratio=prefer_ratio,
            prefer_geolocation=prefer_geolocation,
            selected=selected,
            source=source,
        )

        req = self._build_request(
            method="GET",
            path="/enrichment/address",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetEnrichmentAddressGlobals(
                x_moov_version=self.sdk_configuration.globals.x_moov_version,
            ),
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="getEnrichmentAddress",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetEnrichmentAddressResponse(
                result=utils.unmarshal_json(
                    http_res.text, components.EnrichedAddressResponse
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "404", "429"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_async(
        self,
        *,
        search: str,
        max_results: Optional[int] = None,
        include_cities: Optional[str] = None,
        include_states: Optional[str] = None,
        include_zipcodes: Optional[str] = None,
        exclude_states: Optional[str] = None,
        prefer_cities: Optional[str] = None,
        prefer_states: Optional[str] = None,
        prefer_zipcodes: Optional[str] = None,
        prefer_ratio: Optional[int] = None,
        prefer_geolocation: Optional[str] = None,
        selected: Optional[str] = None,
        source: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetEnrichmentAddressResponse:
        r"""Fetch enriched address suggestions. Requires a partial address.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/profile-enrichment.read` scope.

        :param search: Partial or complete address to search.
        :param max_results: Maximum number of results to return.
        :param include_cities: Limits results to a list of given cities.
        :param include_states: Limits results to a list of given states.
        :param include_zipcodes: Limits results to a list of given zipcodes.
        :param exclude_states: Exclude list of states from results. No `include` pararmeters may be used with this parameter.
        :param prefer_cities: Display results with the listed cities at the top.
        :param prefer_states: Display results with the listed states at the top.
        :param prefer_zipcodes: Display results with the listed zipcodes at the top.
        :param prefer_ratio: Specifies the percentage of address suggestions that should be preferred and will appear at the top of the results.
        :param prefer_geolocation: If omitted or set to `city`, it uses the sender's IP address to determine location, then automatically adds the city and state    to the preferCities value. This parameter takes precedence over other `include` or `exclude` parameters meaning that if it is    not set to `none`, you may see addresses from areas you do not wish to see.
        :param selected: Useful for narrowing results with `addressLine2` suggestions such as `Apt` (denotes an apartment building with multiple residences).
        :param source: Include results from alternate data sources. Allowed values are `all` (non-postal addresses), or `postal` (postal addresses only).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = operations.GetEnrichmentAddressRequest(
            search=search,
            max_results=max_results,
            include_cities=include_cities,
            include_states=include_states,
            include_zipcodes=include_zipcodes,
            exclude_states=exclude_states,
            prefer_cities=prefer_cities,
            prefer_states=prefer_states,
            prefer_zipcodes=prefer_zipcodes,
            prefer_ratio=prefer_ratio,
            prefer_geolocation=prefer_geolocation,
            selected=selected,
            source=source,
        )

        req = self._build_request_async(
            method="GET",
            path="/enrichment/address",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetEnrichmentAddressGlobals(
                x_moov_version=self.sdk_configuration.globals.x_moov_version,
            ),
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="getEnrichmentAddress",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetEnrichmentAddressResponse(
                result=utils.unmarshal_json(
                    http_res.text, components.EnrichedAddressResponse
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "404", "429"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
