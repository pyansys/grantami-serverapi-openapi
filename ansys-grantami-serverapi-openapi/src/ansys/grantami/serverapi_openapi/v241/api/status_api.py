"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Dict, List, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    from ..models import *


class StatusApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_status_get(self) -> "None":
        """Check whether the API is available

        This method makes a synchronous HTTP request.

        Returns
        -------
        None
        """
        data = self._v1alpha_status_get_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_status_get_with_http_info(self, **kwargs):
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_status_get"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        response_type_map = {
            200: None,
        }

        return self.api_client.call_api(
            "/v1alpha/status",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
            response_type_map=response_type_map,
        )
