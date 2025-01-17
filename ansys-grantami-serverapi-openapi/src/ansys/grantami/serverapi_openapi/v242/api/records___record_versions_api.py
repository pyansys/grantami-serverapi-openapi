# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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


class RecordsRecordVersionsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def delete_record_version(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
    ) -> "None":
        """Deletes the record version.  If the table is version controlled, only the current unreleased record version can be deleted.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_history_guid: str
        record_version_guid: str

        Returns
        -------
        None
        """
        data = self._delete_record_version_with_http_info(
            database_key,
            table_guid,
            record_history_guid,
            record_version_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _delete_record_version_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_history_guid",
            "record_version_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_record_version"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_record_version'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'delete_record_version'"
            )
        # verify the required parameter "record_history_guid" is set
        if "record_history_guid" not in params or params["record_history_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_history_guid' when calling 'delete_record_version'"
            )
        # verify the required parameter "record_version_guid" is set
        if "record_version_guid" not in params or params["record_version_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_version_guid' when calling 'delete_record_version'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_history_guid" in params and record_history_guid is not None:
            path_params["record-history-guid"] = params["record_history_guid"]
        if "record_version_guid" in params and record_version_guid is not None:
            path_params["record-version-guid"] = params["record_version_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map: Dict[int, Optional[str]] = {
            200: None,
            400: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-histories/{record-history-guid}/record-versions/{record-version-guid}",
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

    def get_modifiable_record_version(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
    ) -> "Union[GrantaServerApiExceptionsVersionControlGetModifiableRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]":
        """Gets the latest modifiable record version, or creates a new one if none exists. The record version must be the latest version, and must be either released or withdrawn.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_history_guid: str
        record_version_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsVersionControlGetModifiableRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]
        """
        data = self._get_modifiable_record_version_with_http_info(
            database_key,
            table_guid,
            record_history_guid,
            record_version_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_modifiable_record_version_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_history_guid",
            "record_version_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_modifiable_record_version"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_modifiable_record_version'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_modifiable_record_version'"
            )
        # verify the required parameter "record_history_guid" is set
        if "record_history_guid" not in params or params["record_history_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_history_guid' when calling 'get_modifiable_record_version'"
            )
        # verify the required parameter "record_version_guid" is set
        if "record_version_guid" not in params or params["record_version_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_version_guid' when calling 'get_modifiable_record_version'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_history_guid" in params and record_history_guid is not None:
            path_params["record-history-guid"] = params["record_history_guid"]
        if "record_version_guid" in params and record_version_guid is not None:
            path_params["record-version-guid"] = params["record_version_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            201: "GrantaServerApiRecordsRecordVersionsRecordVersion",
            400: "GrantaServerApiExceptionsVersionControlGetModifiableRecordVersionControlException",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-histories/{record-history-guid}/record-versions/{record-version-guid}:get-modifiable-version",
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

    def get_record_version(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
    ) -> "Union[GrantaServerApiRecordsRecordVersionsRecordVersion, None]":
        """Get a record version with a specified guid for a given database, table and record history.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_history_guid: str
        record_version_guid: str
        mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        x_ansys_vc_mode: str
            The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.

        Returns
        -------
        Union[GrantaServerApiRecordsRecordVersionsRecordVersion, None]
        """
        data = self._get_record_version_with_http_info(
            database_key,
            table_guid,
            record_history_guid,
            record_version_guid,
            mode,
            x_ansys_vc_mode,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_record_version_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        mode: "Optional[str]" = None,
        x_ansys_vc_mode: "Optional[str]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_history_guid",
            "record_version_guid",
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
                    f"Got an unexpected keyword argument '{key}' to method get_record_version"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_record_version'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'get_record_version'"
            )
        # verify the required parameter "record_history_guid" is set
        if "record_history_guid" not in params or params["record_history_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_history_guid' when calling 'get_record_version'"
            )
        # verify the required parameter "record_version_guid" is set
        if "record_version_guid" not in params or params["record_version_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_version_guid' when calling 'get_record_version'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_history_guid" in params and record_history_guid is not None:
            path_params["record-history-guid"] = params["record_history_guid"]
        if "record_version_guid" in params and record_version_guid is not None:
            path_params["record-version-guid"] = params["record_version_guid"]

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
            200: "GrantaServerApiRecordsRecordVersionsRecordVersion",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-histories/{record-history-guid}/record-versions/{record-version-guid}",
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

    def release_record_version(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
    ) -> "Union[GrantaServerApiExceptionsVersionControlReleaseRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]":
        """Releases the record version.  Must be an unreleased record version.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_history_guid: str
        record_version_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsVersionControlReleaseRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]
        """
        data = self._release_record_version_with_http_info(
            database_key,
            table_guid,
            record_history_guid,
            record_version_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _release_record_version_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_history_guid",
            "record_version_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method release_record_version"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'release_record_version'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'release_record_version'"
            )
        # verify the required parameter "record_history_guid" is set
        if "record_history_guid" not in params or params["record_history_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_history_guid' when calling 'release_record_version'"
            )
        # verify the required parameter "record_version_guid" is set
        if "record_version_guid" not in params or params["record_version_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_version_guid' when calling 'release_record_version'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_history_guid" in params and record_history_guid is not None:
            path_params["record-history-guid"] = params["record_history_guid"]
        if "record_version_guid" in params and record_version_guid is not None:
            path_params["record-version-guid"] = params["record_version_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiRecordsRecordVersionsRecordVersion",
            400: "GrantaServerApiExceptionsVersionControlReleaseRecordVersionControlException",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-histories/{record-history-guid}/record-versions/{record-version-guid}:release",
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

    def withdraw_record_version(
        self,
        *,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
    ) -> "Union[GrantaServerApiExceptionsVersionControlWithdrawRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]":
        """Withdraws the record version.  Must be a released record version.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_guid: str
        record_history_guid: str
        record_version_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsVersionControlWithdrawRecordVersionControlException, GrantaServerApiRecordsRecordVersionsRecordVersion, None]
        """
        data = self._withdraw_record_version_with_http_info(
            database_key,
            table_guid,
            record_history_guid,
            record_version_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _withdraw_record_version_with_http_info(
        self,
        database_key: "str",
        table_guid: "str",
        record_history_guid: "str",
        record_version_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_guid",
            "record_history_guid",
            "record_version_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method withdraw_record_version"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'withdraw_record_version'"
            )
        # verify the required parameter "table_guid" is set
        if "table_guid" not in params or params["table_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'table_guid' when calling 'withdraw_record_version'"
            )
        # verify the required parameter "record_history_guid" is set
        if "record_history_guid" not in params or params["record_history_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_history_guid' when calling 'withdraw_record_version'"
            )
        # verify the required parameter "record_version_guid" is set
        if "record_version_guid" not in params or params["record_version_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'record_version_guid' when calling 'withdraw_record_version'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_guid" in params and table_guid is not None:
            path_params["table-guid"] = params["table_guid"]
        if "record_history_guid" in params and record_history_guid is not None:
            path_params["record-history-guid"] = params["record_history_guid"]
        if "record_version_guid" in params and record_version_guid is not None:
            path_params["record-version-guid"] = params["record_version_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiRecordsRecordVersionsRecordVersion",
            400: "GrantaServerApiExceptionsVersionControlWithdrawRecordVersionControlException",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-guid}/record-histories/{record-history-guid}/record-versions/{record-version-guid}:withdraw",
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
