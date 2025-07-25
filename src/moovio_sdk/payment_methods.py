"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from moovio_sdk import utils
from moovio_sdk._hooks import HookContext
from moovio_sdk.models import components, errors, operations
from moovio_sdk.types import OptionalNullable, UNSET
from moovio_sdk.utils import get_security_from_env
from moovio_sdk.utils.unmarshal_json_response import unmarshal_json_response
from typing import List, Mapping, Optional


class PaymentMethods(BaseSDK):
    def list(
        self,
        *,
        account_id: str,
        source_id: Optional[str] = None,
        payment_method_type: Optional[components.PaymentMethodType] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.ListPaymentMethodsResponse:
        r"""Retrieve a list of payment methods associated with a Moov account. Read our [payment methods
        guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

        :param account_id:
        :param source_id: Optional parameter to filter the account's payment methods by source ID.   A source ID can be a [walletID](https://docs.moov.io/api/sources/wallets/list/), [cardID](https://docs.moov.io/api/sources/cards/list/),  or [bankAccountID](https://docs.moov.io/api/sources/bank-accounts/list/).
        :param payment_method_type: Optional parameter to filter the account's payment methods by payment method type.
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

        request = operations.ListPaymentMethodsRequest(
            account_id=account_id,
            source_id=source_id,
            payment_method_type=payment_method_type,
        )

        req = self._build_request(
            method="GET",
            path="/accounts/{accountID}/payment-methods",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.ListPaymentMethodsGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="listPaymentMethods",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListPaymentMethodsResponse(
                result=unmarshal_json_response(
                    List[components.PaymentMethod], http_res
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "429"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)

    async def list_async(
        self,
        *,
        account_id: str,
        source_id: Optional[str] = None,
        payment_method_type: Optional[components.PaymentMethodType] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.ListPaymentMethodsResponse:
        r"""Retrieve a list of payment methods associated with a Moov account. Read our [payment methods
        guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

        :param account_id:
        :param source_id: Optional parameter to filter the account's payment methods by source ID.   A source ID can be a [walletID](https://docs.moov.io/api/sources/wallets/list/), [cardID](https://docs.moov.io/api/sources/cards/list/),  or [bankAccountID](https://docs.moov.io/api/sources/bank-accounts/list/).
        :param payment_method_type: Optional parameter to filter the account's payment methods by payment method type.
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

        request = operations.ListPaymentMethodsRequest(
            account_id=account_id,
            source_id=source_id,
            payment_method_type=payment_method_type,
        )

        req = self._build_request_async(
            method="GET",
            path="/accounts/{accountID}/payment-methods",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.ListPaymentMethodsGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="listPaymentMethods",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListPaymentMethodsResponse(
                result=unmarshal_json_response(
                    List[components.PaymentMethod], http_res
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "429"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)

    def get(
        self,
        *,
        account_id: str,
        payment_method_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetPaymentMethodResponse:
        r"""Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

        :param account_id:
        :param payment_method_id:
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

        request = operations.GetPaymentMethodRequest(
            account_id=account_id,
            payment_method_id=payment_method_id,
        )

        req = self._build_request(
            method="GET",
            path="/accounts/{accountID}/payment-methods/{paymentMethodID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetPaymentMethodGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getPaymentMethod",
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
            return operations.GetPaymentMethodResponse(
                result=unmarshal_json_response(components.PaymentMethod, http_res),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "404", "429"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)

    async def get_async(
        self,
        *,
        account_id: str,
        payment_method_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetPaymentMethodResponse:
        r"""Get the specified payment method associated with a Moov account. Read our [payment methods guide](https://docs.moov.io/guides/money-movement/payment-methods/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/payment-methods.read` scope.

        :param account_id:
        :param payment_method_id:
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

        request = operations.GetPaymentMethodRequest(
            account_id=account_id,
            payment_method_id=payment_method_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/accounts/{accountID}/payment-methods/{paymentMethodID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetPaymentMethodGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getPaymentMethod",
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
            return operations.GetPaymentMethodResponse(
                result=unmarshal_json_response(components.PaymentMethod, http_res),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "404", "429"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "504"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)
