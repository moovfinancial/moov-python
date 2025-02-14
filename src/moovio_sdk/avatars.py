"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from moovio_sdk import utils
from moovio_sdk._hooks import HookContext
from moovio_sdk.models import components, errors, operations
from moovio_sdk.types import OptionalNullable, UNSET
from moovio_sdk.utils import get_security_from_env
from typing import Mapping, Optional


class Avatars(BaseSDK):
    def get(
        self,
        *,
        unique_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetAvatarResponse:
        r"""Get avatar image for an account using a unique ID.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/profile-enrichment.read` scope.

        :param unique_id: Any unique ID associated with an account such as accountID, representativeID, routing number, or userID.
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

        request = operations.GetAvatarRequest(
            unique_id=unique_id,
        )

        req = self._build_request(
            method="GET",
            path="/avatars/{uniqueID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="image/*",
            http_headers=http_headers,
            _globals=operations.GetAvatarGlobals(
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
                operation_id="getAvatar",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "image/*"):
            return operations.GetAvatarResponse(
                result=http_res, headers=utils.get_response_headers(http_res.headers)
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
        unique_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetAvatarResponse:
        r"""Get avatar image for an account using a unique ID.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/profile-enrichment.read` scope.

        :param unique_id: Any unique ID associated with an account such as accountID, representativeID, routing number, or userID.
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

        request = operations.GetAvatarRequest(
            unique_id=unique_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/avatars/{uniqueID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="image/*",
            http_headers=http_headers,
            _globals=operations.GetAvatarGlobals(
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
                operation_id="getAvatar",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "image/*"):
            return operations.GetAvatarResponse(
                result=http_res, headers=utils.get_response_headers(http_res.headers)
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
