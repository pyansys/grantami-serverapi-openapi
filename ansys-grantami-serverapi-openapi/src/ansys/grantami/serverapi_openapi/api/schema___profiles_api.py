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


class SchemaProfilesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_profiles_get(
        self,
    ) -> "Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]":
        """Get AllProfilesInfo

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]
        """
        data = self._v1alpha_profiles_get_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_get_with_http_info(self, **kwargs):
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_get"
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
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaProfilesAllProfilesInfo",
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def v1alpha_profiles_patch(
        self,
        *,
        body: "Optional[GrantaServerApiSchemaProfilesUpdateAllProfilesInfo]" = None,
    ) -> "Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]":
        """Update AllProfilesInfo

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSchemaProfilesUpdateAllProfilesInfo

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesAllProfilesInfo, None]
        """
        data = self._v1alpha_profiles_patch_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_patch_with_http_info(
        self,
        body: "Optional[GrantaServerApiSchemaProfilesUpdateAllProfilesInfo]" = None,
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_patch"
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
        # multipart/form-data request detected. Content-Type header will be
        # populated by openapi-common based on request content.

        response_type_map = {
            200: "GrantaServerApiSchemaProfilesAllProfilesInfo",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def v1alpha_profiles_post(
        self, *, body: "Optional[GrantaServerApiSchemaProfilesCreateProfile]" = None
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Create a new profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GrantaServerApiSchemaProfilesCreateProfile

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._v1alpha_profiles_post_with_http_info(
            body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_post_with_http_info(
        self,
        body: "Optional[GrantaServerApiSchemaProfilesCreateProfile]" = None,
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
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_post"
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
        # multipart/form-data request detected. Content-Type header will be
        # populated by openapi-common based on request content.

        response_type_map = {
            201: "GrantaServerApiSchemaProfilesProfile",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles",
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

    def v1alpha_profiles_profile_guid_delete(self, *, profile_guid: "str") -> "None":
        """Delete a profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str

        Returns
        -------
        None
        """
        data = self._v1alpha_profiles_profile_guid_delete_with_http_info(
            profile_guid, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_profile_guid_delete_with_http_info(
        self, profile_guid: "str", **kwargs
    ):
        all_params = [
            "profile_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_profile_guid_delete"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'v1alpha_profiles_profile_guid_delete'"
            )

        collection_formats = {}

        path_params = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        response_type_map = {
            200: None,
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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

    def v1alpha_profiles_profile_guid_get(
        self, *, profile_guid: "str"
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Get individual profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._v1alpha_profiles_profile_guid_get_with_http_info(
            profile_guid, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_profile_guid_get_with_http_info(
        self, profile_guid: "str", **kwargs
    ):
        all_params = [
            "profile_guid",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_profile_guid_get"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'v1alpha_profiles_profile_guid_get'"
            )

        collection_formats = {}

        path_params = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        response_type_map = {
            200: "GrantaServerApiSchemaProfilesProfile",
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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

    def v1alpha_profiles_profile_guid_patch(
        self,
        *,
        profile_guid: "str",
        body: "Optional[GrantaServerApiSchemaProfilesUpdateProfile]" = None,
    ) -> "Union[GrantaServerApiSchemaProfilesProfile, None]":
        """Update a profile

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        profile_guid: str
        body: GrantaServerApiSchemaProfilesUpdateProfile

        Returns
        -------
        Union[GrantaServerApiSchemaProfilesProfile, None]
        """
        data = self._v1alpha_profiles_profile_guid_patch_with_http_info(
            profile_guid, body, _return_http_data_only=True
        )
        return data  # type: ignore[return-value]

    def _v1alpha_profiles_profile_guid_patch_with_http_info(
        self,
        profile_guid: "str",
        body: "Optional[GrantaServerApiSchemaProfilesUpdateProfile]" = None,
        **kwargs,
    ):
        all_params = [
            "profile_guid",
            "body",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
        ]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method v1alpha_profiles_profile_guid_patch"
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "profile_guid" is set
        if "profile_guid" not in params or params["profile_guid"] is None:
            raise ValueError(
                "Missing the required parameter 'profile_guid' when calling 'v1alpha_profiles_profile_guid_patch'"
            )

        collection_formats = {}

        path_params = {}
        if "profile_guid" in params and profile_guid is not None:
            path_params["profile-guid"] = params["profile_guid"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

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
        # multipart/form-data request detected. Content-Type header will be
        # populated by openapi-common based on request content.

        response_type_map = {
            200: "GrantaServerApiSchemaProfilesProfile",
            400: None,
            403: None,
            404: None,
        }

        return self.api_client.call_api(
            "/v1alpha/profiles/{profile-guid}",
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
