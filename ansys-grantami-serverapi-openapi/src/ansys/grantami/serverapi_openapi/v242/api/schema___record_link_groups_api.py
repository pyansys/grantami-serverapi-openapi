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


class SchemaRecordLinkGroupsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_record_link_group(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup]" = None,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]":
        """Create a new record link group.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        body: GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]
        """
        data = self._create_record_link_group_with_http_info(
            database_key, table_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_record_link_group_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        body: "Optional[GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup]" = None,
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
                    f"Got an unexpected keyword argument '{key}' to method create_record_link_group"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_record_link_group'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'create_record_link_group'"
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
            201: "GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups",
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

    def delete_record_link_group(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        record_link_group_type: "str",
    ) -> "None":
        """Delete a record link group.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_link_group_guid: str
        record_link_group_type: str
            The record link group type.

        Returns
        -------
        None
        """
        data = self._delete_record_link_group_with_http_info(
            database_key,
            table_guid,
            record_link_group_guid,
            record_link_group_type,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _delete_record_link_group_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        record_link_group_type: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_link_group_guid",
            "record_link_group_type",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_record_link_group"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_record_link_group'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_record_link_group'"
            )
        # verify the required parameter "record_link_group_guid" is set
        if "record_link_group_guid" not in params or params["record_link_group_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_link_group_guid' when calling 'delete_record_link_group'"
            )
        # verify the required parameter "record_link_group_type" is set
        if "record_link_group_type" not in params or params["record_link_group_type"] is None:
            raise ValueError(
                "Missing the required parameter 'record_link_group_type' when calling 'delete_record_link_group'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_link_group_guid" in params and record_link_group_guid is not None:
            path_params["record-link-group-guid"] = params["record_link_group_guid"]
        if "record_link_group_type" in params and record_link_group_type is not None:
            path_params["record-link-group-type"] = params["record_link_group_type"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map: Dict[int, Optional[str]] = {
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups/{record-link-group-guid}/{record-link-group-type}",
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

    def get_inbound_record_link_groups(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, None]":
        """Get all record link groups pointing towards provided table

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, None]
        """
        data = self._get_inbound_record_link_groups_with_http_info(
            database_key, table_guid, mode, x_ansys_vc_mode, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_inbound_record_link_groups_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_inbound_record_link_groups"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_inbound_record_link_groups'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_inbound_record_link_groups'"
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
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups:inbound-link-groups",
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

    def get_record_link_group(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        record_link_group_type: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]":
        """Get individual record link group

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_link_group_guid: str
        record_link_group_type: str
            The record link group type.
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]
        """
        data = self._get_record_link_group_with_http_info(
            database_key,
            table_guid,
            record_link_group_guid,
            record_link_group_type,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_record_link_group_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        record_link_group_type: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_link_group_guid",
            "record_link_group_type",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_record_link_group"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_record_link_group'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_record_link_group'"
            )
        # verify the required parameter "record_link_group_guid" is set
        if "record_link_group_guid" not in params or params["record_link_group_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_link_group_guid' when calling 'get_record_link_group'"
            )
        # verify the required parameter "record_link_group_type" is set
        if "record_link_group_type" not in params or params["record_link_group_type"] is None:
            raise ValueError(
                "Missing the required parameter 'record_link_group_type' when calling 'get_record_link_group'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_link_group_guid" in params and record_link_group_guid is not None:
            path_params["record-link-group-guid"] = params["record_link_group_guid"]
        if "record_link_group_type" in params and record_link_group_type is not None:
            path_params["record-link-group-type"] = params["record_link_group_type"]

        query_params: List[Any] = []
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
            200: "GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups/{record-link-group-guid}/{record-link-group-type}",
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

    def get_record_link_groups(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, None]":
        """Get all record link groups

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo, None]
        """
        data = self._get_record_link_groups_with_http_info(
            database_key, table_guid, mode, x_ansys_vc_mode, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_record_link_groups_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "mode",
            "x_ansys_vc_mode",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_record_link_groups"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_record_link_groups'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_record_link_groups'"
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
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroupsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups",
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

    def update_record_link_group(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        body: "Optional[GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup]" = None,
    ) -> "Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]":
        """Update record link group.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_link_group_guid: str
        body: GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup

        Returns
        -------
        Union[GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup, None]
        """
        data = self._update_record_link_group_with_http_info(
            database_key, table_guid, record_link_group_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_record_link_group_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_link_group_guid: "str",
        body: "Optional[GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_link_group_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_record_link_group"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_record_link_group'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'update_record_link_group'"
            )
        # verify the required parameter "record_link_group_guid" is set
        if "record_link_group_guid" not in params or params["record_link_group_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_link_group_guid' when calling 'update_record_link_group'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_link_group_guid" in params and record_link_group_guid is not None:
            path_params["record-link-group-guid"] = params["record_link_group_guid"]

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
            200: "GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-link-groups/{record-link-group-guid}",
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
