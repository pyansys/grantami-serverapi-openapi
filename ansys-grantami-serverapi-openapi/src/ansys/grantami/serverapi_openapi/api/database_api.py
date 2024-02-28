"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    BinaryIO,
    List,
    Optional,
    Union,
)  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class DatabaseApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_standard_namesgenerate_integration_schema_post(
        self, *, database_key: "str", body: "Optional[List[str]]" = None
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema with attributes for each provided standard name in the given database. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        body: List[str]

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_standard_namesgenerate_integration_schema_post_with_http_info(
            database_key, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_standard_namesgenerate_integration_schema_post_with_http_info(
        self, database_key: "str", body: "Optional[List[str]]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_standard_namesgenerate_integration_schema_post"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_standard_namesgenerate_integration_schema_post'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

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
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/standard-names:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get(
        self, *, database_key: "str", table_identity: "int", layout_identity: "int"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given layout. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_identity: int
        layout_identity: int

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get_with_http_info(
            database_key, table_identity, layout_identity, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get_with_http_info(
        self,
        database_key: "str",
        table_identity: "int",
        layout_identity: "int",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_identity",
            "layout_identity",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get'"
            )
        # verify the required parameter "table_identity" is set
        if "table_identity" not in params or params["table_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'table_identity' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get'"
            )
        # verify the required parameter "layout_identity" is set
        if "layout_identity" not in params or params["layout_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_identity' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_identitygenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_identity" in params and table_identity is not None:
            path_params["table-identity"] = params["table_identity"]
        if "layout_identity" in params and layout_identity is not None:
            path_params["layout-identity"] = params["layout_identity"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-identity}/layout/{layout-identity}:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get(
        self, *, database_key: "str", table_identity: "int", layout_name: "str"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given layout. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_identity: int
        layout_name: str

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get_with_http_info(
            database_key, table_identity, layout_name, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get_with_http_info(
        self,
        database_key: "str",
        table_identity: "int",
        layout_name: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_identity",
            "layout_name",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get'"
            )
        # verify the required parameter "table_identity" is set
        if "table_identity" not in params or params["table_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'table_identity' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get'"
            )
        # verify the required parameter "layout_name" is set
        if "layout_name" not in params or params["layout_name"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_name' when calling 'v1alpha_databases_database_key_tables_table_identity_layout_layout_namegenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_identity" in params and table_identity is not None:
            path_params["table-identity"] = params["table_identity"]
        if "layout_name" in params and layout_name is not None:
            path_params["layout-name"] = params["layout_name"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-identity}/layout/{layout-name}:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get(
        self, *, database_key: "str", table_identity: "int"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given table. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_identity: int

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get_with_http_info(
            database_key, table_identity, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get_with_http_info(
        self, database_key: "str", table_identity: "int", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_identity",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get'"
            )
        # verify the required parameter "table_identity" is set
        if "table_identity" not in params or params["table_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'table_identity' when calling 'v1alpha_databases_database_key_tables_table_identitygenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_identity" in params and table_identity is not None:
            path_params["table-identity"] = params["table_identity"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-identity}:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get(
        self, *, database_key: "str", table_name: "str", layout_identity: "int"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given layout. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_name: str
        layout_identity: int

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get_with_http_info(
            database_key, table_name, layout_identity, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get_with_http_info(
        self,
        database_key: "str",
        table_name: "str",
        layout_identity: "int",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "table_name",
            "layout_identity",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get'"
            )
        # verify the required parameter "table_name" is set
        if "table_name" not in params or params["table_name"] is None:
            raise ValueError(
                "Missing the required parameter 'table_name' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get'"
            )
        # verify the required parameter "layout_identity" is set
        if "layout_identity" not in params or params["layout_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_identity' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_identitygenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_name" in params and table_name is not None:
            path_params["table-name"] = params["table_name"]
        if "layout_identity" in params and layout_identity is not None:
            path_params["layout-identity"] = params["layout_identity"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-name}/layout/{layout-identity}:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get(
        self, *, database_key: "str", table_name: "str", layout_name: "str"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given layout. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_name: str
        layout_name: str

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get_with_http_info(
            database_key, table_name, layout_name, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get_with_http_info(
        self, database_key: "str", table_name: "str", layout_name: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_name",
            "layout_name",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get'"
            )
        # verify the required parameter "table_name" is set
        if "table_name" not in params or params["table_name"] is None:
            raise ValueError(
                "Missing the required parameter 'table_name' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get'"
            )
        # verify the required parameter "layout_name" is set
        if "layout_name" not in params or params["layout_name"] is None:
            raise ValueError(
                "Missing the required parameter 'layout_name' when calling 'v1alpha_databases_database_key_tables_table_name_layout_layout_namegenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_name" in params and table_name is not None:
            path_params["table-name"] = params["table_name"]
        if "layout_name" in params and layout_name is not None:
            path_params["layout-name"] = params["layout_name"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-name}/layout/{layout-name}:generate-integration-schema",
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

    def v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get(
        self, *, database_key: "str", table_name: "str"
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema from the attributes in the given table. The user must be an Admin user for the database.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        table_name: str

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get_with_http_info(
            database_key, table_name, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get_with_http_info(
        self, database_key: "str", table_name: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "table_name",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get'"
            )
        # verify the required parameter "table_name" is set
        if "table_name" not in params or params["table_name"] is None:
            raise ValueError(
                "Missing the required parameter 'table_name' when calling 'v1alpha_databases_database_key_tables_table_namegenerate_integration_schema_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "table_name" in params and table_name is not None:
            path_params["table-name"] = params["table_name"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/tables/{table-name}:generate-integration-schema",
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

    def v1alpha_databases_database_keysearch_index_status_get(
        self, *, database_key: "str", include_diagnostics: "Optional[bool]" = None
    ) -> "Union[GrantaServerApiSearchIndexStatus, None]":
        """Get Search Index Status for a given database

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        include_diagnostics: bool

        Returns
        -------
        Union[GrantaServerApiSearchIndexStatus, None]
        """
        data = (
            self._v1alpha_databases_database_keysearch_index_status_get_with_http_info(
                database_key, include_diagnostics, _return_http_data_only=True
            )
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_databases_database_keysearch_index_status_get_with_http_info(
        self,
        database_key: "str",
        include_diagnostics: "Optional[bool]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "include_diagnostics",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_databases_database_keysearch_index_status_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'v1alpha_databases_database_keysearch_index_status_get'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]

        query_params: List[Any] = []
        if "include_diagnostics" in params and include_diagnostics is not None:
            query_params.append(("include-diagnostics", params["include_diagnostics"]))

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map: Dict[int, Optional[str]] = {
            200: "GrantaServerApiSearchIndexStatus",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}:search-index-status",
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

    def v1alpha_standard_namesgenerate_integration_schema_post(
        self, *, body: "Optional[List[str]]" = None
    ) -> "Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Generate an integration schema with attributes for each provided standard name. This will include attribute from all loaded databases for which the user is an Admin.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: List[str]

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = (
            self._v1alpha_standard_namesgenerate_integration_schema_post_with_http_info(
                body, _return_http_data_only=True
            )
        )
        return data  # type: ignore[no-any-return]

    def _v1alpha_standard_namesgenerate_integration_schema_post_with_http_info(
        self, body: "Optional[List[str]]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_standard_namesgenerate_integration_schema_post"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

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
            200: "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/standard-names:generate-integration-schema",
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
