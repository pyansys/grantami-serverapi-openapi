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

class SchemaConstantsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_constants_constant_guid_delete(self, *, database_key: "str", constant_guid: "str") -> "Union[GrantaServerApiExceptionsConstantDeletionException, None]":
        """Delete a constant

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            Database in which constant will be search for
        constant_guid: str
            Guid of constant to delete

        Returns
        -------
        Union[GrantaServerApiExceptionsConstantDeletionException, None]
        """
        data = self._v1alpha_databases_database_key_constants_constant_guid_delete_with_http_info(database_key, constant_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_constants_constant_guid_delete_with_http_info(self, database_key: "str", constant_guid: "str", **kwargs):
        all_params = ["database_key", "constant_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_constants_constant_guid_delete")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_constants_constant_guid_delete'")
        # verify the required parameter "constant_guid" is set
        if "constant_guid" not in params or params["constant_guid"] is None:
            raise ValueError("Missing the required parameter 'constant_guid' when calling 'v1alpha_databases_database_key_constants_constant_guid_delete'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "constant_guid" in params and constant_guid is not None:
            path_params["constant-guid"] = params["constant_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            400: "GrantaServerApiExceptionsConstantDeletionException",
            200: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/constants/{constant-guid}", "DELETE",
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

    def v1alpha_databases_database_key_constants_constant_guid_get(self, *, database_key: "str", constant_guid: "str") -> "Union[GrantaServerApiSchemaConstantsConstant, None]":
        """Get individual constant

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            Database in which constant will be search for
        constant_guid: str
            Guid of requested constant

        Returns
        -------
        Union[GrantaServerApiSchemaConstantsConstant, None]
        """
        data = self._v1alpha_databases_database_key_constants_constant_guid_get_with_http_info(database_key, constant_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_constants_constant_guid_get_with_http_info(self, database_key: "str", constant_guid: "str", **kwargs):
        all_params = ["database_key", "constant_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_constants_constant_guid_get")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_constants_constant_guid_get'")
        # verify the required parameter "constant_guid" is set
        if "constant_guid" not in params or params["constant_guid"] is None:
            raise ValueError("Missing the required parameter 'constant_guid' when calling 'v1alpha_databases_database_key_constants_constant_guid_get'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "constant_guid" in params and constant_guid is not None:
            path_params["constant-guid"] = params["constant_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            200: "GrantaServerApiSchemaConstantsConstant",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/constants/{constant-guid}", "GET",
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

    def v1alpha_databases_database_key_constants_constant_guid_patch(self, *, database_key: "str", constant_guid: "str", body: "Optional[GrantaServerApiSchemaConstantsUpdateConstant]" = None) -> "Union[GrantaServerApiSchemaConstantsConstant, None]":
        """Update constant.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            Database in which constant will be search for
        constant_guid: str
            Guid of constant to update
        body: GrantaServerApiSchemaConstantsUpdateConstant
            Constant data to be updated

        Returns
        -------
        Union[GrantaServerApiSchemaConstantsConstant, None]
        """
        data = self._v1alpha_databases_database_key_constants_constant_guid_patch_with_http_info(database_key, constant_guid, body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_constants_constant_guid_patch_with_http_info(self, database_key: "str", constant_guid: "str", body: "Optional[GrantaServerApiSchemaConstantsUpdateConstant]" = None, **kwargs):
        all_params = ["database_key", "constant_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_constants_constant_guid_patch")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_constants_constant_guid_patch'")
        # verify the required parameter "constant_guid" is set
        if "constant_guid" not in params or params["constant_guid"] is None:
            raise ValueError("Missing the required parameter 'constant_guid' when calling 'v1alpha_databases_database_key_constants_constant_guid_patch'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "constant_guid" in params and constant_guid is not None:
            path_params["constant-guid"] = params["constant_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map = {
            200: "GrantaServerApiSchemaConstantsConstant",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/constants/{constant-guid}", "PATCH",
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

    def v1alpha_databases_database_key_constants_get(self, *, database_key: "str") -> "Union[GrantaServerApiSchemaConstantsConstantsInfo, None]":
        """Get all constants

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str

        Returns
        -------
        Union[GrantaServerApiSchemaConstantsConstantsInfo, None]
        """
        data = self._v1alpha_databases_database_key_constants_get_with_http_info(database_key, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_constants_get_with_http_info(self, database_key: "str", **kwargs):
        all_params = ["database_key", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_constants_get")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_constants_get'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            200: "GrantaServerApiSchemaConstantsConstantsInfo",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/constants", "GET",
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

    def v1alpha_databases_database_key_constants_post(self, *, database_key: "str", body: "Optional[GrantaServerApiSchemaConstantsCreateConstant]" = None) -> "Union[GrantaServerApiSchemaConstantsConstant, None]":
        """Create a new constant.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
            Database in which constant will be created
        body: GrantaServerApiSchemaConstantsCreateConstant
            Constant to add to database

        Returns
        -------
        Union[GrantaServerApiSchemaConstantsConstant, None]
        """
        data = self._v1alpha_databases_database_key_constants_post_with_http_info(database_key, body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_constants_post_with_http_info(self, database_key: "str", body: "Optional[GrantaServerApiSchemaConstantsCreateConstant]" = None, **kwargs):
        all_params = ["database_key", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_constants_post")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_constants_post'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map = {
            200: "GrantaServerApiSchemaConstantsConstant",
            201: None,
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/constants", "POST",
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
