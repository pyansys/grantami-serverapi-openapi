"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401
from . import ApiBase


if TYPE_CHECKING:
    import pathlib
    from ..models import *


class LicenseApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def checkout_app_license(self, *, body: "Optional[GsaAppNameLicenseCheckoutRequest]" = None) -> "GsaAppNameLicenseCheckoutResponse":
        """Checks out server wide licenses and returns a bool for each provided app name indicating if  the relevant license(s) required have been checked out.

        This method makes a synchronous HTTP request.

        Parameters
        ----------
        body: GsaAppNameLicenseCheckoutRequest

        Returns
        -------
        GsaAppNameLicenseCheckoutResponse
        """
        data = self._checkout_app_license_with_http_info(body, _return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _checkout_app_license_with_http_info(self, body: "Optional[GsaAppNameLicenseCheckoutRequest]" = None, **kwargs: Any) -> Any:
        all_params = ["body", "_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method checkout_app_license")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        if "body" in params and body is not None:
            body_params = params["body"]
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["text/plain", "application/json", "text/json"])

        # HTTP header 'Content-Type'
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json-patch+json", "application/json", "text/json", "application/*+json"])

        response_type_map: dict[int, Optional[str]] = {
            200: "GsaAppNameLicenseCheckoutResponse",
        }
        
        return self.api_client.call_api(
            "/v1alpha/license/server-licenses:ensure-checked-out", "POST",
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

    def ensure_user_license_available(self) -> "Union[MicrosoftAspNetCoreMvcObjectResult, None]":
        """Either checks out a user license for the requesting user, or returns an error response if no such license is available.  This method is a no-op because it relies on license check to happen within Granta.Server.Api.Auth.UserContextFilter

        This method makes a synchronous HTTP request.

        Returns
        -------
        Union[MicrosoftAspNetCoreMvcObjectResult, None]
        """
        data = self._ensure_user_license_available_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _ensure_user_license_available_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method ensure_user_license_available")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["text/plain", "application/json", "text/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: None,
            403: "MicrosoftAspNetCoreMvcObjectResult",
        }
        
        return self.api_client.call_api(
            "/v1alpha/license/user-license:ensure-checked-out", "GET",
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

    def get_server_license(self) -> "GsaEnabledLicensesInfo":
        """Get info on which server licenses are enabled, and the license expiry date.

        This method makes a synchronous HTTP request.

        Returns
        -------
        GsaEnabledLicensesInfo
        """
        data = self._get_server_license_with_http_info(_return_http_data_only=True)
        return data  # type: ignore[no-any-return]

    def _get_server_license_with_http_info(self, **kwargs: Any) -> Any:
        all_params = ["_return_http_data_only", "_preload_content", "_request_timeout"]

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}' to method get_server_license")
            params[key] = val
        del params["kwargs"]

        collection_formats: dict[str, Any] = {}

        path_params: dict[str, Any] = {}

        query_params: list[Any] = []

        header_params: dict[str, Any] = {}

        form_params: list[Any] = []
        local_var_files: dict[str, Any] = {}

        body_params = None
        # HTTP header 'Accept'
        header_params["Accept"] = self.api_client.select_header_accept(["text/plain", "application/json", "text/json"])


        response_type_map: dict[int, Optional[str]] = {
            200: "GsaEnabledLicensesInfo",
        }
        
        return self.api_client.call_api(
            "/v1alpha/license/server-licenses", "GET",
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
