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


class SchemaLayoutsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def applications(
        self, *, database_key: "str", table_guid: "str"
    ) -> "Union[GsaApplicationsInfo, None]":
        """Returns applications that are either MI Applications, or in use in layouts in this table.  Can be used as applicable applications for layouts.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str

        Returns
        -------
        Union[GsaApplicationsInfo, None]
        """
        data = self._applications_with_http_info(
            database_key, table_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _applications_with_http_info(
        self, database_key: "str", table_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method applications"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'applications'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'applications'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaApplicationsInfo",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts:applications",
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

    def create_layout(
        self, *, database_key: "str", table_guid: "str", body: "Optional[GsaCreateLayout]" = None
    ) -> "Union[GsaLayout, None]":
        """Create a new layout.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        body: GsaCreateLayout

        Returns
        -------
        Union[GsaLayout, None]
        """
        data = self._create_layout_with_http_info(
            database_key, table_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_layout_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GsaCreateLayout]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_layout"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_layout'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'create_layout'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            201: "GsaLayout",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts",
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

    def delete_layout(
        self, *, database_key: "str", table_guid: "str", layout_guid: "str"
    ) -> "None":
        """Delete a layout.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str

        Returns
        -------
        None
        """
        data = self._delete_layout_with_http_info(
            database_key, table_guid, layout_guid, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _delete_layout_with_http_info(
        self, database_key: "str", table_guid: "str", layout_guid: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_layout"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_layout'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_layout'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'delete_layout'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map: Dict[int, Optional[str]] = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}",
            "DELETE",
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

    def get_layout(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GsaLayout, None]":
        """Get a layout with a specified guid for a given database and table.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        show_full_detail: bool
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GsaLayout, None]
        """
        data = self._get_layout_with_http_info(
            database_key,
            table_guid,
            layout_guid,
            show_full_detail,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_layout_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        show_full_detail: "Optional[bool]" = None,
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "show_full_detail",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_layout")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_layout'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_layout'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'get_layout'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

        query_params: List[Any] = []
        if "show_full_detail" in params and show_full_detail is not None:
            query_params.append(("showFullDetail", params["show_full_detail"]))
        if "mode" in params and mode is not None:
            query_params.append(("mode", params["mode"]))

        header_params: Dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaLayout",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}",
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

    def get_layouts(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        application: "Optional[str]" = None,
    ) -> "Union[GsaLayoutsInfo, None]":
        """Get all layouts for table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        application: str
            Optionally filter by application that the layout is applicable to.

        Returns
        -------
        Union[GsaLayoutsInfo, None]
        """
        data = self._get_layouts_with_http_info(
            database_key,
            table_guid,
            mode,
            x_ansys_vc_mode,
            application,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_layouts_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        application: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "mode",
            "x_ansys_vc_mode",
            "application",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_layouts")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_layouts'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_layouts'"
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
        if "application" in params and application is not None:
            query_params.append(("application", params["application"]))

        header_params: Dict[str, Any] = {}
        if "x_ansys_vc_mode" in params and x_ansys_vc_mode is not None:
            header_params["X-Ansys-VC-Mode"] = params["x_ansys_vc_mode"]

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaLayoutsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts",
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

    def update_layout(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GsaUpdateLayout]" = None,
    ) -> "Union[GsaLayout, None]":
        """Update a layout.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        layout_guid: str
        body: GsaUpdateLayout

        Returns
        -------
        Union[GsaLayout, None]
        """
        data = self._update_layout_with_http_info(
            database_key, table_guid, layout_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_layout_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        layout_guid: "str",
        body: "Optional[GsaUpdateLayout]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "layout_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_layout"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_layout'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'update_layout'"
            )
        # verify the required parameter "layout_guid" is set
        if "layout_guid" not in params or params["layout_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_guid' when calling 'update_layout'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "layout_guid" in params and layout_guid is not None:
            path_params["layout-guid"] = params["layout_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json-patch+json", "application/json", "text/json", "application/*+json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GsaLayout",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}",
            "PATCH",
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
