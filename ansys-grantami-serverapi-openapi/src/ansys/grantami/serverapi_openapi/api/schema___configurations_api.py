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


class SchemaConfigurationsApi(ApiBase):  # type: ignore[misc]
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def create_configuration(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsCreateConfiguration]" = None,
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Create a new configuration.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        body: GrantaServerApiSchemaConfigurationsCreateConfiguration

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._create_configuration_with_http_info(
            database_key, configuration_type, body, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _create_configuration_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsCreateConfiguration]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method create_configuration"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'create_configuration'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'create_configuration'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
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
            201: "GrantaServerApiSchemaConfigurationsConfiguration",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}",
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

    def delete_configuration(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
    ) -> "None":
        """Delete a configuration

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        None
        """
        data = self._delete_configuration_with_http_info(
            database_key,
            configuration_type,
            configuration_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _delete_configuration_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method delete_configuration"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'delete_configuration'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'delete_configuration'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'delete_configuration'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map = {
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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

    def export_configuration(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
    ) -> "None":
        """Get individual configuration as a file

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        None
        """
        data = self._export_configuration_with_http_info(
            database_key,
            configuration_type,
            configuration_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _export_configuration_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method export_configuration"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'export_configuration'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'export_configuration'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'export_configuration'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None

        response_type_map = {
            200: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}:export",
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

    def get_configuration(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Get individual configuration

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._get_configuration_with_http_info(
            database_key,
            configuration_type,
            configuration_guid,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _get_configuration_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_configuration"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_configuration'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'get_configuration'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'get_configuration'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaConfigurationsConfiguration",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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

    def get_configurations(
        self, *, database_key: "str", configuration_type: "str"
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfigurationsInfo, None]":
        """Get all configurations of given type

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfigurationsInfo, None]
        """
        data = self._get_configurations_with_http_info(
            database_key, configuration_type, _return_http_data_only=True
        )
        return data  # type: ignore[no-any-return]

    def _get_configurations_with_http_info(
        self, database_key: "str", configuration_type: "str", **kwargs: Any
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_configurations"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'get_configurations'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'get_configurations'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaConfigurationsConfigurationsInfo",
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}",
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

    def update_configuration(
        self,
        *,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsUpdateConfiguration]" = None,
    ) -> "Union[GrantaServerApiSchemaConfigurationsConfiguration, None]":
        """Update a configuration.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        database_key: str
        configuration_type: str
            The configuration type.
        configuration_guid: str
        body: GrantaServerApiSchemaConfigurationsUpdateConfiguration

        Returns
        -------
        Union[GrantaServerApiSchemaConfigurationsConfiguration, None]
        """
        data = self._update_configuration_with_http_info(
            database_key,
            configuration_type,
            configuration_guid,
            body,
            _return_http_data_only=True,
        )
        return data  # type: ignore[no-any-return]

    def _update_configuration_with_http_info(
        self,
        database_key: "str",
        configuration_type: "str",
        configuration_guid: "str",
        body: "Optional[GrantaServerApiSchemaConfigurationsUpdateConfiguration]" = None,
        **kwargs: Any,
    ) -> Any:
        all_params = [
            "database_key",
            "configuration_type",
            "configuration_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_configuration"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "database_key" is set
        if "database_key" not in params or params["database_key"] is None:
            raise ValueError(
                "Missing the required parameter 'database_key' when calling 'update_configuration'"
            )
        # verify the required parameter "configuration_type" is set
        if "configuration_type" not in params or params["configuration_type"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_type' when calling 'update_configuration'"
            )
        # verify the required parameter "configuration_guid" is set
        if "configuration_guid" not in params or params["configuration_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'configuration_guid' when calling 'update_configuration'"
            )

        collection_formats: Dict[str, Any] = {}

        path_params: Dict[str, Any] = {}
        if "database_key" in params and database_key is not None:
            path_params["database-key"] = params["database_key"]
        if "configuration_type" in params and configuration_type is not None:
            path_params["configuration-type"] = params["configuration_type"]
        if "configuration_guid" in params and configuration_guid is not None:
            path_params["configuration-guid"] = params["configuration_guid"]

        query_params: List[Any] = []

        header_params: Dict[str, Any] = {}

        form_params: List[Any] = []
        local_var_files: Dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
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
            200: "GrantaServerApiSchemaConfigurationsConfiguration",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/databases/{database-key}/configurations/{configuration-type}/{configuration-guid}",
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
