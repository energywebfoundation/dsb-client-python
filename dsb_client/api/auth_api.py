"""
    DSB Message Broker API

    Swagger documentation for the DSB Message Broker API  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dsb_client.api_client import ApiClient, Endpoint as _Endpoint
from dsb_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dsb_client.model.login_data_dto import LoginDataDTO
from dsb_client.model.login_return_data_dto import LoginReturnDataDTO


class AuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __auth_controller_login(
            self,
            login_data_dto,
            **kwargs
        ):
            """auth_controller_login  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.auth_controller_login(login_data_dto, async_req=True)
            >>> result = thread.get()

            Args:
                login_data_dto (LoginDataDTO):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LoginReturnDataDTO
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['login_data_dto'] = \
                login_data_dto
            return self.call_with_http_info(**kwargs)

        self.auth_controller_login = _Endpoint(
            settings={
                'response_type': (LoginReturnDataDTO,),
                'auth': [],
                'endpoint_path': '/auth/login',
                'operation_id': 'auth_controller_login',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'login_data_dto',
                ],
                'required': [
                    'login_data_dto',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'login_data_dto':
                        (LoginDataDTO,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'login_data_dto': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__auth_controller_login
        )
