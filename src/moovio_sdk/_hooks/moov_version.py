from typing import Union

import httpx

from .types import SDKConfiguration, SDKInitHook, BeforeRequestContext, BeforeRequestHook

class MoovVersionHook(SDKInitHook, BeforeRequestHook):

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        """Sets the X-Moov-Version global variable to the OpenAPI document version"""
        config.globals.x_moov_version = config.openapi_doc_version

        return config

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        """Adds the X-Moov-Version header to each request"""
        print(f"Globals: {hook_ctx.config.globals}")
        request.headers["X-Moov-Version"] = str(hook_ctx.config.globals.x_moov_version)
        return request
