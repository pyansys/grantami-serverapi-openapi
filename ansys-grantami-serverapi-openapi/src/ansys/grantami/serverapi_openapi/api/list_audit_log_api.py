"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class ListAuditLogApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def get_list_audit_log_search_results(self, *, result_resource_identifier: "str") -> "Union[None, list[GsaListAuditLogItem]]":
        """Returns the search results found in the specified resource

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        result_resource_identifier: str

        Returns
        -------
        Union[None, list[GsaListAuditLogItem]]
        """
        data = self._get_list_audit_log_search_results_with_http_info(result_resource_identifier, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_list_audit_log_search_results_with_http_info(self, result_resource_identifier: "str", **kwargs: Any) -> Any:
        all_params = ["result_resource_identifier", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_list_audit_log_search_results")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "result_resource_identifier" is set
        if "result_resource_identifier" not in params or params["result_resource_identifier"] is None:
            raise ValueError("Missing the required parameter 'result_resource_identifier' when calling 'get_list_audit_log_search_results'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "result_resource_identifier" in params and result_resource_identifier is not None:
            path_params["resultResourceIdentifier"] = params["result_resource_identifier"]

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["text/plain", "application/json", "text/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: "list[GsaListAuditLogItem]",
            403: None,
            404: None,
            410: None,
        }
        
        return self.api_client.call_api(
            "/api/v1/lists/audit/search/results/{resultResourceIdentifier}", "GET",
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

    def run_list_audit_log_search(self, *, body: "Optional[GsaListAuditLogSearchRequest]" = None) -> "Union[GsaRecordListSearchInfo, None]":
        """Posts a search request, and returns an object containing search result identifier

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaListAuditLogSearchRequest

        Returns
        -------
        Union[GsaRecordListSearchInfo, None]
        """
        data = self._run_list_audit_log_search_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _run_list_audit_log_search_with_http_info(self, body: "Optional[GsaListAuditLogSearchRequest]" = None, **kwargs: Any) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method run_list_audit_log_search")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["text/plain", "application/json", "text/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map: dict[int, Optional[str]] = {
            201: "GsaRecordListSearchInfo",
            400: None,
            403: None,
        }
        
        return self.api_client.call_api(
            "/api/v1/lists/audit/search", "POST",
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
