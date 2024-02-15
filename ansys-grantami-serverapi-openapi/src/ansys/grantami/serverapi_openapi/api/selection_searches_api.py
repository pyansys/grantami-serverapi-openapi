"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Dict, IO, List, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class SelectionSearchesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_selection_searches_get(
        self,
    ) -> "Union[List[GrantaServerApiSelectionSearchesSelectionSearch], None]":
        """Returns all searches visible to the calling user.

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[List[GrantaServerApiSelectionSearchesSelectionSearch], None]
        """
        data = self._v1alpha_selection_searches_get_with_http_info(
            _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_get_with_http_info(self, **kwargs):
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_get"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "list[GrantaServerApiSelectionSearchesSelectionSearch]",
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches",
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

    def v1alpha_selection_searches_post(
        self,
        *,
        body: "Optional[GrantaServerApiSelectionSearchesCreateSearchRequest]" = None,
    ) -> "Union[GrantaServerApiSelectionSearchesSelectionSearch, None]":
        """Creates a new search with the specified properties.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSelectionSearchesCreateSearchRequest

        Returns
        -------
        Union[GrantaServerApiSelectionSearchesSelectionSearch, None]
        """
        data = self._v1alpha_selection_searches_post_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_post_with_http_info(
        self,
        body: "Optional[GrantaServerApiSelectionSearchesCreateSearchRequest]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_post"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

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
            201: "GrantaServerApiSelectionSearchesSelectionSearch",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches",
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

    def v1alpha_selection_searches_search_post(
        self,
        *,
        body: "Optional[GrantaServerApiSelectionSearchesFindSearchRequest]" = None,
    ) -> "Union[GrantaServerApiSelectionSearchesSelectionSearch, None]":
        """Retrieves a collection of searches that match the specified criteria.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSelectionSearchesFindSearchRequest

        Returns
        -------
        Union[GrantaServerApiSelectionSearchesSelectionSearch, None]
        """
        data = self._v1alpha_selection_searches_search_post_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_search_post_with_http_info(
        self,
        body: "Optional[GrantaServerApiSelectionSearchesFindSearchRequest]" = None,
        **kwargs,
    ):
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_search_post"
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

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
            200: "GrantaServerApiSelectionSearchesSelectionSearch",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches/search",
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

    def v1alpha_selection_searches_search_search_identifier_delete(
        self, *, search_identifier: "str"
    ) -> "None":
        """Delete an existing selection search.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        search_identifier: str

        Returns
        -------
        None
        """
        data = self._v1alpha_selection_searches_search_search_identifier_delete_with_http_info(
            search_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_search_search_identifier_delete_with_http_info(
        self, search_identifier: "str", **kwargs
    ):
        all_params = [
            "search_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_search_search_identifier_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "search_identifier" is set
        if "search_identifier" not in params or params["search_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'search_identifier' when calling 'v1alpha_selection_searches_search_search_identifier_delete'"
            )

        collection_formats = {}

        path_params = {}
        if "search_identifier" in params and search_identifier is not None:
            path_params["searchIdentifier"] = params["search_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        response_type_map = {
            200: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches/search/{searchIdentifier}",
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

    def v1alpha_selection_searches_search_search_identifier_get(
        self, *, search_identifier: "str"
    ) -> "Union[GrantaServerApiSelectionSearchesSelectionSearch, None]":
        """Returns the given search if it exists and the calling user has access to it

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        search_identifier: str

        Returns
        -------
        Union[GrantaServerApiSelectionSearchesSelectionSearch, None]
        """
        data = self._v1alpha_selection_searches_search_search_identifier_get_with_http_info(
            search_identifier, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_search_search_identifier_get_with_http_info(
        self, search_identifier: "str", **kwargs
    ):
        all_params = [
            "search_identifier",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_search_search_identifier_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "search_identifier" is set
        if "search_identifier" not in params or params["search_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'search_identifier' when calling 'v1alpha_selection_searches_search_search_identifier_get'"
            )

        collection_formats = {}

        path_params = {}
        if "search_identifier" in params and search_identifier is not None:
            path_params["searchIdentifier"] = params["search_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSelectionSearchesSelectionSearch",
            403: None,
            404: None,
            410: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches/search/{searchIdentifier}",
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

    def v1alpha_selection_searches_search_search_identifier_put(
        self,
        *,
        search_identifier: "str",
        body: "Optional[GrantaServerApiSelectionSearchesSaveSearchRequest]" = None,
    ) -> "None":
        """If the search exists, updates the properties of the search. This will overwrite all current properties.  If the search does not exist or the calling user does not have access to it, returns '404 not found' response.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        search_identifier: str
        body: GrantaServerApiSelectionSearchesSaveSearchRequest

        Returns
        -------
        None
        """
        data = self._v1alpha_selection_searches_search_search_identifier_put_with_http_info(
            search_identifier, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_selection_searches_search_search_identifier_put_with_http_info(
        self,
        search_identifier: "str",
        body: "Optional[GrantaServerApiSelectionSearchesSaveSearchRequest]" = None,
        **kwargs,
    ):
        all_params = [
            "search_identifier",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_selection_searches_search_search_identifier_put"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "search_identifier" is set
        if "search_identifier" not in params or params["search_identifier"] is None:
            raise ValueError(
                "Missing the required parameter 'search_identifier' when calling 'v1alpha_selection_searches_search_search_identifier_put'"
            )

        collection_formats = {}

        path_params = {}
        if "search_identifier" in params and search_identifier is not None:
            path_params["searchIdentifier"] = params["search_identifier"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
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
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/selection-searches/search/{searchIdentifier}",
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
