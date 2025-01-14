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


class DataExportApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def export_data(self, *, database_key: "str", body: "Optional[GsaDataExportRequest]" = None, x_ansys_vc_mode: "Optional[str]" = None, mode: "Optional[str]" = None) -> "Union[GsaDataExportResponse, None]":
        """Export data from the given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: GsaDataExportRequest
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.

        Returns
        -------
        Union[GsaDataExportResponse, None]
        """
        data = self._export_data_with_http_info(database_key, body, x_ansys_vc_mode, mode, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _export_data_with_http_info(self, database_key: "str", body: "Optional[GsaDataExportRequest]" = None, x_ansys_vc_mode: "Optional[str]" = None, mode: "Optional[str]" = None, **kwargs: Any) -> Any:
        all_params = ["database_key", "body", "x_ansys_vc_mode", "mode", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method export_data")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'export_data'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: list[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

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
            200: "GsaDataExportResponse",
            404: None,
            403: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}:export", "POST",
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

    def export_data_from_integration_schema(self, *, schema: "str", body: "Optional[GsaIntegrationDataExportRequest]" = None) -> "Union[GsaDataExportResponse, None]":
        """Export data from the integration schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
        body: GsaIntegrationDataExportRequest

        Returns
        -------
        Union[GsaDataExportResponse, None]
        """
        data = self._export_data_from_integration_schema_with_http_info(schema, body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _export_data_from_integration_schema_with_http_info(self, schema: "str", body: "Optional[GsaIntegrationDataExportRequest]" = None, **kwargs: Any) -> Any:
        all_params = ["schema", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method export_data_from_integration_schema")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError("Missing the required parameter 'schema' when calling 'export_data_from_integration_schema'")

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]

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
            200: "GsaDataExportResponse",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}:export", "POST",
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
