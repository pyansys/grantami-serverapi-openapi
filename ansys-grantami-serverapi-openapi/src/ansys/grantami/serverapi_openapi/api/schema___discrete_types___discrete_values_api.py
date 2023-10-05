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

class SchemaDiscreteTypesDiscreteValuesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str") -> "Union[GrantaServerApiExceptionsDiscreteValueDeletionException, None]":
        """Delete a single discrete value. It must not be used by any data, or the operation will fail.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str

        Returns
        -------
        Union[GrantaServerApiExceptionsDiscreteValueDeletionException, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete_with_http_info(database_key, discrete_type_guid, discrete_value_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", **kwargs):
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_delete'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            400: "GrantaServerApiExceptionsDiscreteValueDeletionException",
            200: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "DELETE",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str") -> "Union[GrantaServerApiSchemaDiscreteValue, None]":
        """Gets specific discrete value for a given discreteType within a given database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValue, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get_with_http_info(database_key, discrete_type_guid, discrete_value_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", **kwargs):
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_get'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            200: "GrantaServerApiSchemaDiscreteValue",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "GET",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch(self, *, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValue]" = None) -> "Union[GrantaServerApiSchemaDiscreteValue, None]":
        """Update discrete value.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        discrete_value_guid: str
        body: GrantaServerApiSchemaDiscreteValue

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValue, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch_with_http_info(database_key, discrete_type_guid, discrete_value_guid, body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch_with_http_info(self, database_key: "str", discrete_type_guid: "str", discrete_value_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValue]" = None, **kwargs):
        all_params = ["database_key", "discrete_type_guid", "discrete_value_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch'")
        # verify the required parameter "discrete_value_guid" is set
        if "discrete_value_guid" not in params or params["discrete_value_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_value_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_discrete_value_guid_patch'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]
        if "discrete_value_guid" in params and discrete_value_guid is not None:
            path_params["discrete-value-guid"] = params["discrete_value_guid"]

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
            200: "GrantaServerApiSchemaDiscreteValue",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values/{discrete-value-guid}", "PATCH",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get(self, *, database_key: "str", discrete_type_guid: "str") -> "Union[GrantaServerApiSchemaDiscreteValuesInfo, None]":
        """Gets all discrete values for a given discreteType. If discreteType is ordered, then discreteValues will be return in order, otherwise order is not deterministic.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValuesInfo, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get_with_http_info(database_key, discrete_type_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get_with_http_info(self, database_key: "str", discrete_type_guid: "str", **kwargs):
        all_params = ["database_key", "discrete_type_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_get'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            200: "GrantaServerApiSchemaDiscreteValuesInfo",
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "GET",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post(self, *, database_key: "str", discrete_type_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValue]" = None) -> "Union[GrantaServerApiSchemaDiscreteValue, None]":
        """Create new discrete value. If it's ordered, it will be added at the end.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        body: GrantaServerApiSchemaDiscreteValue

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValue, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post_with_http_info(database_key, discrete_type_guid, body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post_with_http_info(self, database_key: "str", discrete_type_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValue]" = None, **kwargs):
        all_params = ["database_key", "discrete_type_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_post'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

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
            200: "GrantaServerApiSchemaDiscreteValue",
            201: None,
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "POST",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put(self, *, database_key: "str", discrete_type_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValuesInfo]" = None) -> "Union[GrantaServerApiSchemaDiscreteValuesInfo, None]":
        """Replace the whole discrete value collection for a given discrete type.  This will result in adding, modifying, deleting and reordering discrete values. If any of those operations fail, the whole operation fails.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str
        body: GrantaServerApiSchemaDiscreteValuesInfo

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValuesInfo, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put_with_http_info(database_key, discrete_type_guid, body, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put_with_http_info(self, database_key: "str", discrete_type_guid: "str", body: "Optional[GrantaServerApiSchemaDiscreteValuesInfo]" = None, **kwargs):
        all_params = ["database_key", "discrete_type_guid", "body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_values_put'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

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
            200: "GrantaServerApiSchemaDiscreteValuesInfo",
            400: None,
            403: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values", "PUT",
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

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get(self, *, database_key: "str", discrete_type_guid: "str") -> "Union[GrantaServerApiSchemaDiscreteValuesInfo, None]":
        """Find discrete values that are not in use by any data

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        discrete_type_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaDiscreteValuesInfo, None]
        """
        data = self._v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get_with_http_info(database_key, discrete_type_guid, _return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get_with_http_info(self, database_key: "str", discrete_type_guid: "str", **kwargs):
        all_params = ["database_key", "discrete_type_guid", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get")
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError("Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get'")
        # verify the required parameter "discrete_type_guid" is set
        if "discrete_type_guid" not in params or params["discrete_type_guid"] is None:
            raise ValueError("Missing the required parameter 'discrete_type_guid' when calling 'v1alpha_databases_database_key_discrete_types_discrete_type_guid_discrete_valuesfind_unused_get'")

        collection_formats = {}

        path_params = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "discrete_type_guid" in params and discrete_type_guid is not None:
            path_params["discrete-type-guid"] = params["discrete_type_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        response_type_map = {
            200: "GrantaServerApiSchemaDiscreteValuesInfo",
            400: None,
            404: None,
        }
        
        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}/discrete-values:find-unused", "GET",
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
