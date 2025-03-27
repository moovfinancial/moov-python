"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from datetime import datetime
from moovio_sdk import utils
from moovio_sdk._hooks import HookContext
from moovio_sdk.models import components, errors, operations
from moovio_sdk.types import OptionalNullable, UNSET
from moovio_sdk.utils import get_security_from_env
from typing import List, Mapping, Optional


class WalletTransactions(BaseSDK):
    def list(
        self,
        *,
        account_id: str,
        wallet_id: str,
        skip: Optional[int] = None,
        count: Optional[int] = None,
        transaction_type: Optional[components.WalletTransactionType] = None,
        transaction_types: Optional[List[components.WalletTransactionType]] = None,
        source_type: Optional[components.WalletTransactionSourceType] = None,
        source_id: Optional[str] = None,
        status: Optional[components.WalletTransactionStatus] = None,
        created_start_date_time: Optional[datetime] = None,
        created_end_date_time: Optional[datetime] = None,
        completed_start_date_time: Optional[datetime] = None,
        completed_end_date_time: Optional[datetime] = None,
        sweep_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.ListWalletTransactionsResponse:
        r"""List all the transactions associated with a particular Moov wallet.

        Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

        :param account_id:
        :param wallet_id:
        :param skip:
        :param count:
        :param transaction_type: Optional parameter to filter by transaction type.
        :param transaction_types: Optional, comma-separated parameter to filter by transaction types.
        :param source_type: Optional parameter to filter by source type (i.e. transfer, dispute, issuing-transaction).
        :param source_id: Optional parameter to filter by source ID.
        :param status: Optional parameter to filter by status (`pending` or `completed`).
        :param created_start_date_time: Optional date-time which inclusively filters all transactions created after this date-time.
        :param created_end_date_time: Optional date-time which exclusively filters all transactions created before this date-time.
        :param completed_start_date_time: Optional date-time which inclusively filters all transactions completed after this date-time.
        :param completed_end_date_time: Optional date-time which exclusively filters all transactions completed before this date-time.
        :param sweep_id: Optional ID to filter for transactions accrued in a sweep.
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

        request = operations.ListWalletTransactionsRequest(
            account_id=account_id,
            skip=skip,
            count=count,
            wallet_id=wallet_id,
            transaction_type=transaction_type,
            transaction_types=transaction_types,
            source_type=source_type,
            source_id=source_id,
            status=status,
            created_start_date_time=created_start_date_time,
            created_end_date_time=created_end_date_time,
            completed_start_date_time=completed_start_date_time,
            completed_end_date_time=completed_end_date_time,
            sweep_id=sweep_id,
        )

        req = self._build_request(
            method="GET",
            path="/accounts/{accountID}/wallets/{walletID}/transactions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.ListWalletTransactionsGlobals(
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
                operation_id="listWalletTransactions",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListWalletTransactionsResponse(
                result=utils.unmarshal_json(
                    http_res.text, List[components.WalletTransaction]
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "429"], "*"):
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

    async def list_async(
        self,
        *,
        account_id: str,
        wallet_id: str,
        skip: Optional[int] = None,
        count: Optional[int] = None,
        transaction_type: Optional[components.WalletTransactionType] = None,
        transaction_types: Optional[List[components.WalletTransactionType]] = None,
        source_type: Optional[components.WalletTransactionSourceType] = None,
        source_id: Optional[str] = None,
        status: Optional[components.WalletTransactionStatus] = None,
        created_start_date_time: Optional[datetime] = None,
        created_end_date_time: Optional[datetime] = None,
        completed_start_date_time: Optional[datetime] = None,
        completed_end_date_time: Optional[datetime] = None,
        sweep_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.ListWalletTransactionsResponse:
        r"""List all the transactions associated with a particular Moov wallet.

        Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

        :param account_id:
        :param wallet_id:
        :param skip:
        :param count:
        :param transaction_type: Optional parameter to filter by transaction type.
        :param transaction_types: Optional, comma-separated parameter to filter by transaction types.
        :param source_type: Optional parameter to filter by source type (i.e. transfer, dispute, issuing-transaction).
        :param source_id: Optional parameter to filter by source ID.
        :param status: Optional parameter to filter by status (`pending` or `completed`).
        :param created_start_date_time: Optional date-time which inclusively filters all transactions created after this date-time.
        :param created_end_date_time: Optional date-time which exclusively filters all transactions created before this date-time.
        :param completed_start_date_time: Optional date-time which inclusively filters all transactions completed after this date-time.
        :param completed_end_date_time: Optional date-time which exclusively filters all transactions completed before this date-time.
        :param sweep_id: Optional ID to filter for transactions accrued in a sweep.
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

        request = operations.ListWalletTransactionsRequest(
            account_id=account_id,
            skip=skip,
            count=count,
            wallet_id=wallet_id,
            transaction_type=transaction_type,
            transaction_types=transaction_types,
            source_type=source_type,
            source_id=source_id,
            status=status,
            created_start_date_time=created_start_date_time,
            created_end_date_time=created_end_date_time,
            completed_start_date_time=completed_start_date_time,
            completed_end_date_time=completed_end_date_time,
            sweep_id=sweep_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/accounts/{accountID}/wallets/{walletID}/transactions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.ListWalletTransactionsGlobals(
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
                operation_id="listWalletTransactions",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.ListWalletTransactionsResponse(
                result=utils.unmarshal_json(
                    http_res.text, List[components.WalletTransaction]
                ),
                headers=utils.get_response_headers(http_res.headers),
            )
        if utils.match_response(http_res, ["401", "403", "429"], "*"):
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

    def get(
        self,
        *,
        account_id: str,
        wallet_id: str,
        transaction_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetWalletTransactionResponse:
        r"""Get details on a specific wallet transaction.

        Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

        :param account_id:
        :param wallet_id:
        :param transaction_id:
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

        request = operations.GetWalletTransactionRequest(
            account_id=account_id,
            wallet_id=wallet_id,
            transaction_id=transaction_id,
        )

        req = self._build_request(
            method="GET",
            path="/accounts/{accountID}/wallets/{walletID}/transactions/{transactionID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetWalletTransactionGlobals(
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
                operation_id="getWalletTransaction",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetWalletTransactionResponse(
                result=utils.unmarshal_json(
                    http_res.text, components.WalletTransaction
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
        account_id: str,
        wallet_id: str,
        transaction_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> operations.GetWalletTransactionResponse:
        r"""Get details on a specific wallet transaction.

        Read our [wallet transactions guide](https://docs.moov.io/guides/sources/wallets/transactions/) to learn more.

        To access this endpoint using an [access token](https://docs.moov.io/api/authentication/access-tokens/)
        you'll need to specify the `/accounts/{accountID}/wallets.read` scope.

        :param account_id:
        :param wallet_id:
        :param transaction_id:
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

        request = operations.GetWalletTransactionRequest(
            account_id=account_id,
            wallet_id=wallet_id,
            transaction_id=transaction_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/accounts/{accountID}/wallets/{walletID}/transactions/{transactionID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=operations.GetWalletTransactionGlobals(
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
                operation_id="getWalletTransaction",
                oauth2_scopes=None,
                security_source=get_security_from_env(
                    self.sdk_configuration.security, components.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "403", "404", "429", "4XX", "500", "504", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetWalletTransactionResponse(
                result=utils.unmarshal_json(
                    http_res.text, components.WalletTransaction
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
