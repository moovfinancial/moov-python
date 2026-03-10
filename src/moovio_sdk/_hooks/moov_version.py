import httpx
from typing import Union

from .types import BeforeRequestContext, BeforeRequestHook


class MoovVersionHook(BeforeRequestHook):

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        """Sets the X-Moov-Version header on every outgoing request"""

        request.headers["X-Moov-Version"] = hook_ctx.config.openapi_doc_version
        return request
