"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from moovio_sdk import utils
from moovio_sdk._hooks import HookContext
from moovio_sdk.models import components, errors, operations
from moovio_sdk.types import BaseModel, OptionalNullable, UNSET
from moovio_sdk.utils import get_security_from_env
from typing import Any, Mapping, Optional, Union, cast


class EndToEndEncryption(BaseSDK):
    def test_encrypted_token(
        self,
        *,
        token: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.TestEndToEndTokenResponse:
        r"""Allows for testing a JWE token to ensure it's acceptable by Moov.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/ping.read` scope.

        :param token: An [RFC](https://datatracker.ietf.org/doc/html/rfc7516) compact-serialized JSON Web Encryption (JWE) token.
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

        request = components.E2EEToken(
            token=token,
        )

        req = self._build_request(
            method="POST",
            path="/debug/end-to-end-token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.TestEndToEndTokenGlobals(
                x_moov_version=self.sdk_configuration.globals.x_moov_version,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", components.E2EEToken
            ),
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
                operation_id="testEndToEndToken",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return operations.TestEndToEndTokenResponse(
                headers=utils.get_response_headers(http_res.headers)
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, errors.GenericErrorData)
            raise errors.GenericError(data=response_data)
        if utils.match_response(http_res, "429", "*"):
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

    async def test_encrypted_token_async(
        self,
        *,
        token: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.TestEndToEndTokenResponse:
        r"""Allows for testing a JWE token to ensure it's acceptable by Moov.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/ping.read` scope.

        :param token: An [RFC](https://datatracker.ietf.org/doc/html/rfc7516) compact-serialized JSON Web Encryption (JWE) token.
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

        request = components.E2EEToken(
            token=token,
        )

        req = self._build_request_async(
            method="POST",
            path="/debug/end-to-end-token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.TestEndToEndTokenGlobals(
                x_moov_version=self.sdk_configuration.globals.x_moov_version,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", components.E2EEToken
            ),
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
                operation_id="testEndToEndToken",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return operations.TestEndToEndTokenResponse(
                headers=utils.get_response_headers(http_res.headers)
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = utils.unmarshal_json(http_res.text, errors.GenericErrorData)
            raise errors.GenericError(data=response_data)
        if utils.match_response(http_res, "429", "*"):
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

    def generate_key(
        self,
        *,
        request: Union[
            operations.GenerateEndToEndKeyRequest,
            operations.GenerateEndToEndKeyRequestTypedDict,
        ] = operations.GenerateEndToEndKeyRequest(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GenerateEndToEndKeyResponse:
        r"""Generates a public key used to create a JWE token for passing secure authentication data through non-PCI compliant intermediaries.

        :param request: The request object to send.
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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GenerateEndToEndKeyRequest)
        request = cast(operations.GenerateEndToEndKeyRequest, request)

        req = self._build_request(
            method="POST",
            path="/end-to-end-keys",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GenerateEndToEndKeyGlobals(
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
                operation_id="generateEndToEndKey",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GenerateEndToEndKeyResponse(
                result=utils.unmarshal_json(http_res.text, components.JSONWebKey),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "429", "*"):
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

    async def generate_key_async(
        self,
        *,
        request: Union[
            operations.GenerateEndToEndKeyRequest,
            operations.GenerateEndToEndKeyRequestTypedDict,
        ] = operations.GenerateEndToEndKeyRequest(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GenerateEndToEndKeyResponse:
        r"""Generates a public key used to create a JWE token for passing secure authentication data through non-PCI compliant intermediaries.

        :param request: The request object to send.
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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GenerateEndToEndKeyRequest)
        request = cast(operations.GenerateEndToEndKeyRequest, request)

        req = self._build_request_async(
            method="POST",
            path="/end-to-end-keys",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GenerateEndToEndKeyGlobals(
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
                operation_id="generateEndToEndKey",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GenerateEndToEndKeyResponse(
                result=utils.unmarshal_json(http_res.text, components.JSONWebKey),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, "429", "*"):
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
