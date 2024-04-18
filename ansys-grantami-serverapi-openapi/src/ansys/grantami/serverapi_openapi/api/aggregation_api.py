# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ApiBase

if TYPE_CHECKING:
    import pathlib

    from ..models import *


class AggregationApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def database_aggregation(
        self,
        *,
        database_key: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiAggregationsAggregationsResponse, None]":
        """Runs an aggregation against the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: GrantaServerApiAggregationsAggregationsRequest
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.

        Returns
        -------
        Union[GrantaServerApiAggregationsAggregationsResponse, None]
        """
        data = self._database_aggregation_with_http_info(
            database_key, body, x_ansys_vc_mode, mode, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _database_aggregation_with_http_info(
        self,
        database_key: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "body",
            "x_ansys_vc_mode",
            "mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method database_aggregation"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'database_aggregation'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: List[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: Dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiAggregationsAggregationsResponse",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}:aggregations",
            "POST",
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

    def database_aggregation_for_table_with_guid(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiAggregationsAggregationsResponse, None]":
        """Runs an aggregation against the table.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        body: GrantaServerApiAggregationsAggregationsRequest
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.

        Returns
        -------
        Union[GrantaServerApiAggregationsAggregationsResponse, None]
        """
        data = self._database_aggregation_for_table_with_guid_with_http_info(
            database_key,
            table_guid,
            body,
            x_ansys_vc_mode,
            mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _database_aggregation_for_table_with_guid_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "body",
            "x_ansys_vc_mode",
            "mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method database_aggregation_for_table_with_guid"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'database_aggregation_for_table_with_guid'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'database_aggregation_for_table_with_guid'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params: List[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: Dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiAggregationsAggregationsResponse",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}:aggregations",
            "POST",
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

    def database_aggregation_for_table_with_identity(
        self,
        *,
        database_key: "str",
        table_identity: "int",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiAggregationsAggregationsResponse, None]":
        """Runs an aggregation against the table.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_identity: int
        body: GrantaServerApiAggregationsAggregationsRequest
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.

        Returns
        -------
        Union[GrantaServerApiAggregationsAggregationsResponse, None]
        """
        data = self._database_aggregation_for_table_with_identity_with_http_info(
            database_key,
            table_identity,
            body,
            x_ansys_vc_mode,
            mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _database_aggregation_for_table_with_identity_with_http_info(
        self,
        database_key: "str",
        table_identity: "int",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_identity",
            "body",
            "x_ansys_vc_mode",
            "mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method database_aggregation_for_table_with_identity"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'database_aggregation_for_table_with_identity'"
            )
        # verify the required parameter "table_identity" is set
        if "table_identity" not in params or params["table_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'table_identity' when calling 'database_aggregation_for_table_with_identity'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_identity" in params and table_identity is not None:
            path_params["table-identity"] = params["table_identity"]

        query_params: List[Any] = []
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: Dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiAggregationsAggregationsResponse",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-identity}:aggregations",
            "POST",
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

    def integration_aggregation(
        self,
        *,
        schema: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
    ) -> "Union[GrantaServerApiAggregationsAggregationsResponse, None]":
        """Runs an aggregation against the integration schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
        body: GrantaServerApiAggregationsAggregationsRequest

        Returns
        -------
        Union[GrantaServerApiAggregationsAggregationsResponse, None]
        """
        data = self._integration_aggregation_with_http_info(
            schema, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _integration_aggregation_with_http_info(
        self,
        schema: "str",
        body: "Optional[GrantaServerApiAggregationsAggregationsRequest]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "schema",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method integration_aggregation"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'integration_aggregation'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            [
                "application/json-patch+json",
                "application/json",
                "text/json",
                "application/*+json",
            ]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiAggregationsAggregationsResponse",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}:aggregations",
            "POST",
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
