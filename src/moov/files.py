"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from moov import models, utils
from moov._hooks import HookContext
from moov.types import OptionalNullable, UNSET
from moov.utils import get_security_from_env
from typing import List, Optional, Union


class UploadFileAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class ListFilesAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class GetFileDetailsAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"


class Files(BaseSDK):
    r"""Files can be used for a multitude of different use cases including but not limited to, individual identity verification and business underwriting. You may need to provide documentation to enable capabilities or to keep capabilities enabled for an account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. To learn about uploading files in the Moov Dashboard, read our [file upload guide](https://docs.moov.io/guides/dashboard/accounts/#file-upload)."""

    def upload_file(
        self,
        *,
        account_id: str,
        file_upload_request: Union[
            models.FileUploadRequest, models.FileUploadRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[UploadFileAcceptEnum] = None,
    ) -> models.UploadFileResponse:
        r"""Upload file

        Upload a file and link it to the provided Moov account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

        :param account_id: ID of the account.
        :param file_upload_request:
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

        request = models.UploadFileRequest(
            account_id=account_id,
            file_upload_request=utils.get_pydantic_model(
                file_upload_request, models.FileUploadRequest
            ),
        )

        req = self.build_request(
            method="POST",
            path="/accounts/{accountID}/files",
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
                request.file_upload_request,
                False,
                False,
                "multipart",
                models.FileUploadRequest,
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
                operation_id="uploadFile",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.UploadFileResponse(
                result=utils.unmarshal_json(http_res.text, models.File), headers={}
            )
        if utils.match_response(http_res, ["400", "404", "422", "4XX", "5XX"], "*"):
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
            return models.UploadFileResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def upload_file_async(
        self,
        *,
        account_id: str,
        file_upload_request: Union[
            models.FileUploadRequest, models.FileUploadRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[UploadFileAcceptEnum] = None,
    ) -> models.UploadFileResponse:
        r"""Upload file

        Upload a file and link it to the provided Moov account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.write` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

        :param account_id: ID of the account.
        :param file_upload_request:
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

        request = models.UploadFileRequest(
            account_id=account_id,
            file_upload_request=utils.get_pydantic_model(
                file_upload_request, models.FileUploadRequest
            ),
        )

        req = self.build_request_async(
            method="POST",
            path="/accounts/{accountID}/files",
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
                request.file_upload_request,
                False,
                False,
                "multipart",
                models.FileUploadRequest,
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
                operation_id="uploadFile",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "404", "422", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.UploadFileResponse(
                result=utils.unmarshal_json(http_res.text, models.File), headers={}
            )
        if utils.match_response(http_res, ["400", "404", "422", "4XX", "5XX"], "*"):
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
            return models.UploadFileResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def list_files(
        self,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ListFilesAcceptEnum] = None,
    ) -> models.ListFilesResponse:
        r"""List files

        List all the files associated with a particular Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

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

        request = models.ListFilesRequest(
            account_id=account_id,
        )

        req = self.build_request(
            method="GET",
            path="/accounts/{accountID}/files",
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
                operation_id="listFiles",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListFilesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.File]),
                headers={},
            )
        if utils.match_response(http_res, ["404", "4XX", "5XX"], "*"):
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
            return models.ListFilesResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_files_async(
        self,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ListFilesAcceptEnum] = None,
    ) -> models.ListFilesResponse:
        r"""List files

        List all the files associated with a particular Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

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

        request = models.ListFilesRequest(
            account_id=account_id,
        )

        req = self.build_request_async(
            method="GET",
            path="/accounts/{accountID}/files",
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
                operation_id="listFiles",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListFilesResponse(
                result=utils.unmarshal_json(http_res.text, List[models.File]),
                headers={},
            )
        if utils.match_response(http_res, ["404", "4XX", "5XX"], "*"):
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
            return models.ListFilesResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_file_details(
        self,
        *,
        account_id: str,
        file_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetFileDetailsAcceptEnum] = None,
    ) -> models.GetFileDetailsResponse:
        r"""Get file details

        Retrieve file details associated with a specific Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

        :param account_id: ID of the account.
        :param file_id: Identifier for the file.
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

        request = models.GetFileDetailsRequest(
            account_id=account_id,
            file_id=file_id,
        )

        req = self.build_request(
            method="GET",
            path="/accounts/{accountID}/files/{fileID}",
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
                operation_id="getFileDetails",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetFileDetailsResponse(
                result=utils.unmarshal_json(http_res.text, models.File), headers={}
            )
        if utils.match_response(http_res, ["404", "4XX", "5XX"], "*"):
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
            return models.GetFileDetailsResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_file_details_async(
        self,
        *,
        account_id: str,
        file_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetFileDetailsAcceptEnum] = None,
    ) -> models.GetFileDetailsResponse:
        r"""Get file details

        Retrieve file details associated with a specific Moov account. <br><br> To use this endpoint from the browser, you'll need to specify the `/accounts/{accountID}/files.read` scope when generating a [token](https://docs.moov.io/api/authentication/access-tokens/).

        :param account_id: ID of the account.
        :param file_id: Identifier for the file.
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

        request = models.GetFileDetailsRequest(
            account_id=account_id,
            file_id=file_id,
        )

        req = self.build_request_async(
            method="GET",
            path="/accounts/{accountID}/files/{fileID}",
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
                operation_id="getFileDetails",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return models.GetFileDetailsResponse(
                result=utils.unmarshal_json(http_res.text, models.File), headers={}
            )
        if utils.match_response(http_res, ["404", "4XX", "5XX"], "*"):
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
            return models.GetFileDetailsResponse(result=http_res.text, headers={})

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )