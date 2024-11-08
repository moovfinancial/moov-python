"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from moov import models, utils
from moov._hooks import HookContext
from moov.types import OptionalNullable, UNSET
from moov.utils import get_security_from_env
from typing import Optional, Union


class GetBrandingAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class CreateBrandingAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class UpdateBrandingAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class BrandingSDK(BaseSDK):
    def get_branding(
        self,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetBrandingAcceptEnum] = None,
    ) -> models.GetBrandingResponse:
        r"""Get account branding

        Gets the brand properties for the specified account.


        :param account_id: ID of the account.
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

        request = models.GetBrandingRequest(
            account_id=account_id,
        )

        req = self.build_request(
            method="GET",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                operation_id="getBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "4XX", "5XX"], "*"):
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
            return models.GetBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_branding_async(
        self,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetBrandingAcceptEnum] = None,
    ) -> models.GetBrandingResponse:
        r"""Get account branding

        Gets the brand properties for the specified account.


        :param account_id: ID of the account.
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

        request = models.GetBrandingRequest(
            account_id=account_id,
        )

        req = self.build_request_async(
            method="GET",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                operation_id="getBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "4XX", "5XX"], "*"):
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
            return models.GetBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def create_branding(
        self,
        *,
        account_id: str,
        request_body: Union[
            models.CreateBrandingCreateBrandingRequest,
            models.CreateBrandingCreateBrandingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[CreateBrandingAcceptEnum] = None,
    ) -> models.CreateBrandingResponse:
        r"""Create a brand

        Creates the brand properties for the specified account.


        :param account_id: ID of the account.
        :param request_body:
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

        request = models.CreateBrandingRequest(
            account_id=account_id,
            request_body=utils.get_pydantic_model(
                request_body, models.CreateBrandingCreateBrandingRequest
            ),
        )

        req = self.build_request(
            method="POST",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.CreateBrandingCreateBrandingRequest,
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
                operation_id="createBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.CreateBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "422", "4XX", "5XX"], "*"):
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
            return models.CreateBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_branding_async(
        self,
        *,
        account_id: str,
        request_body: Union[
            models.CreateBrandingCreateBrandingRequest,
            models.CreateBrandingCreateBrandingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[CreateBrandingAcceptEnum] = None,
    ) -> models.CreateBrandingResponse:
        r"""Create a brand

        Creates the brand properties for the specified account.


        :param account_id: ID of the account.
        :param request_body:
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

        request = models.CreateBrandingRequest(
            account_id=account_id,
            request_body=utils.get_pydantic_model(
                request_body, models.CreateBrandingCreateBrandingRequest
            ),
        )

        req = self.build_request_async(
            method="POST",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.CreateBrandingCreateBrandingRequest,
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
                operation_id="createBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.CreateBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "422", "4XX", "5XX"], "*"):
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
            return models.CreateBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def update_branding(
        self,
        *,
        account_id: str,
        request_body: Union[
            models.UpdateBrandingPatchBrandingRequest,
            models.UpdateBrandingPatchBrandingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[UpdateBrandingAcceptEnum] = None,
    ) -> models.UpdateBrandingResponse:
        r"""Update branding

        Updates the brand properties for the specified account.


        :param account_id: ID of the account.
        :param request_body:
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

        request = models.UpdateBrandingRequest(
            account_id=account_id,
            request_body=utils.get_pydantic_model(
                request_body, models.UpdateBrandingPatchBrandingRequest
            ),
        )

        req = self.build_request(
            method="PATCH",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.UpdateBrandingPatchBrandingRequest,
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
                operation_id="updateBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.UpdateBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "422", "4XX", "5XX"], "*"):
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
            return models.UpdateBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def update_branding_async(
        self,
        *,
        account_id: str,
        request_body: Union[
            models.UpdateBrandingPatchBrandingRequest,
            models.UpdateBrandingPatchBrandingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[UpdateBrandingAcceptEnum] = None,
    ) -> models.UpdateBrandingResponse:
        r"""Update branding

        Updates the brand properties for the specified account.


        :param account_id: ID of the account.
        :param request_body:
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

        request = models.UpdateBrandingRequest(
            account_id=account_id,
            request_body=utils.get_pydantic_model(
                request_body, models.UpdateBrandingPatchBrandingRequest
            ),
        )

        req = self.build_request_async(
            method="PATCH",
            path="/accounts/{accountID}/branding",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/plain;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.UpdateBrandingPatchBrandingRequest,
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
                operation_id="updateBranding",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["403", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.UpdateBrandingResponse(
                result=utils.unmarshal_json(http_res.text, models.Branding), headers={}
            )
        if utils.match_response(http_res, ["403", "404", "422", "4XX", "5XX"], "*"):
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
            return models.UpdateBrandingResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
