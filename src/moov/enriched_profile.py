"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from moov import models, utils
from moov._hooks import HookContext
from moov.types import OptionalNullable, UNSET
from moov.utils import get_security_from_env
from typing import Optional


class GetEnrichmentProfileAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class EnrichedProfile(BaseSDK):
    r"""By supplying an email address, you can retrieve a profile with enriched data fields. This service is offered in collaboration with Clearbit."""

    def get_enrichment_profile(
        self,
        *,
        email: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetEnrichmentProfileAcceptEnum] = None,
    ) -> models.GetEnrichmentProfileResponse:
        r"""Get enriched profile

        Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit.
        <br><br> To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


        :param email: Valid email address belonging to the profile of interest
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetEnrichmentProfileRequest(
            email=email,
        )

        req = self.build_request(
            method="GET",
            path="/enrichment/profile",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
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
                operation_id="getEnrichmentProfile",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "429", "4XX", "503", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetEnrichmentProfileResponse(
                result=utils.unmarshal_json(http_res.text, models.EnrichmentProfile),
                headers={},
            )
        if utils.match_response(http_res, ["404", "422", "4XX", "503", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "429", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "text/plain"):
            return models.GetEnrichmentProfileResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_enrichment_profile_async(
        self,
        *,
        email: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetEnrichmentProfileAcceptEnum] = None,
    ) -> models.GetEnrichmentProfileResponse:
        r"""Get enriched profile

        Fetch enriched profile data. Requires a valid email address. This service is offered in collaboration with Clearbit.
        <br><br> To use this endpoint from the browser, you'll need to specify the `/profile-enrichment.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).


        :param email: Valid email address belonging to the profile of interest
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetEnrichmentProfileRequest(
            email=email,
        )

        req = self.build_request_async(
            method="GET",
            path="/enrichment/profile",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
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
                operation_id="getEnrichmentProfile",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "429", "4XX", "503", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetEnrichmentProfileResponse(
                result=utils.unmarshal_json(http_res.text, models.EnrichmentProfile),
                headers={},
            )
        if utils.match_response(http_res, ["404", "422", "4XX", "503", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "429", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "text/plain"):
            return models.GetEnrichmentProfileResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )