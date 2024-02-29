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


class IntegrationApi(ApiBase):  # type: ignore[misc]
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def add_schema(
        self,
        *,
        body: "Optional[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier]" = None,
    ) -> "Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Add an integration schema. Will fail if the schema is not valid, or if the user is not both a global administrator and an administrator for the schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._add_schema_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _add_schema_with_http_info(
        self,
        body: "Optional[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier]" = None,
        **kwargs: Any,
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
                    f"Got an unexpected keyword argument '{key}' to method add_schema"
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

        response_type_map = {
            201: "GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas",
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

    def all_schema_status(
        self, *, include_diagnostics: "Optional[bool]" = None
    ) -> "Dict[str, GrantaServerApiIntegrationIntegrationSchemaStatus]":
        """Returns the status of all available integration schemas.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        include_diagnostics: bool

        Returns
        -------
        Dict[str, GrantaServerApiIntegrationIntegrationSchemaStatus]
        """
        data = self._all_schema_status_with_http_info(
            include_diagnostics, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _all_schema_status_with_http_info(
        self, include_diagnostics: "Optional[bool]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "include_diagnostics",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method all_schema_status"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}

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

        response_type_map = {
            200: "dict(str, GrantaServerApiIntegrationIntegrationSchemaStatus)",
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas:search-index-status",
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

    def delete_schema(self, *, schema: "str") -> "None":
        """Delete an integration schema. Will fail if the schema does not exist, or if the user is not both a global administrator and an administrator for the schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
            Schema to be deleted

        Returns
        -------
        None
        """
        data = self._delete_schema_with_http_info(schema, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _delete_schema_with_http_info(self, schema: "str", **kwargs: Any) -> Any:
        all_params = [
            "schema",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_schema"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'delete_schema'"
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

        response_type_map = {
            204: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}",
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

    def get_schema(
        self, *, schema: "str", include_implicit_attributes: "Optional[bool]" = None
    ) -> "Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Returns the full object representing the integration schema.  Names and identities of source items will be populated if they can be found in the databases currently loaded in MI, otherwise just the GUIDs will be returned.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
            The schema name.
        include_implicit_attributes: bool
            Whether to add in the schema attributes derived from certain record properties (e.g. Record Name) that are implicitly in all integration schemas. False by default.

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._get_schema_with_http_info(
            schema, include_implicit_attributes, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_schema_with_http_info(
        self,
        schema: "str",
        include_implicit_attributes: "Optional[bool]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "schema",
            "include_implicit_attributes",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_schema"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'get_schema'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]

        query_params: List[Any] = []
        if (
            "include_implicit_attributes" in params
            and include_implicit_attributes is not None
        ):
            query_params.append(
                ("includeImplicitAttributes", params["include_implicit_attributes"])
            )

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}",
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

    def get_status_for_integration_schema(
        self, *, schema: "str", include_diagnostics: "Optional[bool]" = None
    ) -> "GrantaServerApiIntegrationIntegrationSchemaStatus":
        """get_status_for_integration_schema

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
        include_diagnostics: bool

        Returns
        -------
        GrantaServerApiIntegrationIntegrationSchemaStatus
        """
        data = self._get_status_for_integration_schema_with_http_info(
            schema, include_diagnostics, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_status_for_integration_schema_with_http_info(
        self, schema: "str", include_diagnostics: "Optional[bool]" = None, **kwargs: Any
    ) -> Any:
        all_params = [
            "schema",
            "include_diagnostics",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_status_for_integration_schema"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'get_status_for_integration_schema'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]

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

        response_type_map = {
            200: "GrantaServerApiIntegrationIntegrationSchemaStatus",
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}:search-index-status",
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

    def schema_table_mappings(
        self, *, schema: "str", database_key: "str", table_identity: "int"
    ) -> "Union[List[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None]":
        """Returns a list of the schema source mapping from the given table. Will fail if the database is not loaded in MI.  Names and identities of source items will be populated.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
        database_key: str
        table_identity: int

        Returns
        -------
        Union[List[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier], None]
        """
        data = self._schema_table_mappings_with_http_info(
            schema, database_key, table_identity, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _schema_table_mappings_with_http_info(
        self, schema: "str", database_key: "str", table_identity: "int", **kwargs: Any
    ) -> Any:
        all_params = [
            "schema",
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
                    f"Got an unexpected keyword argument '{key}' to method schema_table_mappings"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'schema_table_mappings'"
            )
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'schema_table_mappings'"
            )
        # verify the required parameter "table_identity" is set
        if "table_identity" not in params or params["table_identity"] is None:
            raise ValueError(
                "Missing the required parameter 'table_identity' when calling 'schema_table_mappings'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]
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

        response_type_map = {
            200: "list[GrantaServerApiIntegrationSchemaSourceOfGrantaServerApiObjectIdentifier]",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}/sources/database/{database-key}/table/{table-identity}",
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

    def schema_targets(
        self, *, schema: "str", include_implicit_attributes: "Optional[bool]" = None
    ) -> "Union[List[GrantaServerApiIntegrationSchemaAttribute], None]":
        """Returns a list of the attributes defined in the integration schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
            The schema name.
        include_implicit_attributes: bool
            Whether to add in the schema attributes derived from certain record properties (e.g. Record Name) that are implicitly in all integration schemas. False by default.

        Returns
        -------
        Union[List[GrantaServerApiIntegrationSchemaAttribute], None]
        """
        data = self._schema_targets_with_http_info(
            schema, include_implicit_attributes, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _schema_targets_with_http_info(
        self,
        schema: "str",
        include_implicit_attributes: "Optional[bool]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "schema",
            "include_implicit_attributes",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method schema_targets"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'schema_targets'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "schema" in params and schema is not None:
            path_params["schema"] = params["schema"]

        query_params: List[Any] = []
        if (
            "include_implicit_attributes" in params
            and include_implicit_attributes is not None
        ):
            query_params.append(
                ("includeImplicitAttributes", params["include_implicit_attributes"])
            )

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "list[GrantaServerApiIntegrationSchemaAttribute]",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}/attributes",
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

    def schemas(self) -> "List[str]":
        """Lists the available integration schemas.

        This method makes a synchronous HTTP request.

        Returns
        -------
        List[str]
        """
        data = self._schemas_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _schemas_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method schemas"
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
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "list[str]",
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas",
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

    def update_schema(
        self,
        *,
        schema: "str",
        body: "Optional[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier]" = None,
    ) -> "Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]":
        """Updates an integration schema, or adds a new one if there is not one with the same key already.  Will fail if the schema is not valid, or if the user is not both a global administrator and an administrator for the schema.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        schema: str
        body: GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier

        Returns
        -------
        Union[GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier, None]
        """
        data = self._update_schema_with_http_info(
            schema, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _update_schema_with_http_info(
        self,
        schema: "str",
        body: "Optional[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier]" = None,
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
                    f"Got an unexpected keyword argument '{key}' to method update_schema"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "schema" is set
        if "schema" not in params or params["schema"] is None:
            raise ValueError(
                "Missing the required parameter 'schema' when calling 'update_schema'"
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

        response_type_map = {
            201: "GrantaServerApiIntegrationSchemaIntegrationSchemaOfGrantaServerApiObjectIdentifier",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/integration-schemas/{schema}",
            "PUT",
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
