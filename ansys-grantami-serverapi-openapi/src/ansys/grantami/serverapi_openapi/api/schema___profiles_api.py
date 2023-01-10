# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from . import ApiBase


class SchemaProfilesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_profiles_get(self, **kwargs):  # noqa: E501
        """Get AllProfilesInfo  # noqa: E501

        This method makes a synchronous HTTP request.

        :return: GrantaServerApiSchemaAllProfilesInfo
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_get_with_http_info(**kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get AllProfilesInfo  # noqa: E501

        This method makes a synchronous HTTP request.

        :return: GrantaServerApiSchemaAllProfilesInfo
        """

        all_params = []  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_get".format(key)
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaAllProfilesInfo',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_profiles_patch(self, **kwargs):  # noqa: E501
        """Update AllProfilesInfo  # noqa: E501

        This method makes a synchronous HTTP request.

        :param GrantaServerApiSchemaAllProfilesInfo body:
        :return: GrantaServerApiSchemaAllProfilesInfo
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_patch_with_http_info(**kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Update AllProfilesInfo  # noqa: E501

        This method makes a synchronous HTTP request.

        :param GrantaServerApiSchemaAllProfilesInfo body:
        :return: GrantaServerApiSchemaAllProfilesInfo
        """

        all_params = ['body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_patch".format(key)
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaAllProfilesInfo',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_profiles_post(self, **kwargs):  # noqa: E501
        """Create a new profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param GrantaServerApiSchemaProfile body:
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_post_with_http_info(**kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param GrantaServerApiSchemaProfile body:
        :return: None
        """

        all_params = ['body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_post".format(key)
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_profiles_profile_guid_delete(self, profile_guid, **kwargs):  # noqa: E501
        """Delete a profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_profile_guid_delete_with_http_info(profile_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_profile_guid_delete_with_http_info(self, profile_guid, **kwargs):  # noqa: E501
        """Delete a profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :return: None
        """

        all_params = ['profile_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_profile_guid_delete".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'profile_guid' is set
        if ('profile_guid' not in params or
                params['profile_guid'] is None):
            raise ValueError("Missing the required parameter `profile_guid` when calling `v1alpha_profiles_profile_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'profile_guid' in params:
            path_params['profile-guid'] = params['profile_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles/{profile-guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_profiles_profile_guid_get(self, profile_guid, **kwargs):  # noqa: E501
        """Get individual profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :return: GrantaServerApiSchemaProfile
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_profile_guid_get_with_http_info(profile_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_profile_guid_get_with_http_info(self, profile_guid, **kwargs):  # noqa: E501
        """Get individual profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :return: GrantaServerApiSchemaProfile
        """

        all_params = ['profile_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_profile_guid_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'profile_guid' is set
        if ('profile_guid' not in params or
                params['profile_guid'] is None):
            raise ValueError("Missing the required parameter `profile_guid` when calling `v1alpha_profiles_profile_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'profile_guid' in params:
            path_params['profile-guid'] = params['profile_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles/{profile-guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaProfile',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_profiles_profile_guid_patch(self, profile_guid, **kwargs):  # noqa: E501
        """Update a profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :param GrantaServerApiSchemaProfile body:
        :return: GrantaServerApiSchemaProfile
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_profiles_profile_guid_patch_with_http_info(profile_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_profiles_profile_guid_patch_with_http_info(self, profile_guid, **kwargs):  # noqa: E501
        """Update a profile  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str profile_guid: (required)
        :param GrantaServerApiSchemaProfile body:
        :return: GrantaServerApiSchemaProfile
        """

        all_params = ['profile_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_profiles_profile_guid_patch".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'profile_guid' is set
        if ('profile_guid' not in params or
                params['profile_guid'] is None):
            raise ValueError("Missing the required parameter `profile_guid` when calling `v1alpha_profiles_profile_guid_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'profile_guid' in params:
            path_params['profile-guid'] = params['profile_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/profiles/{profile-guid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaProfile',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
