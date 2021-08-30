# dsb_client.ChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_controller_create_channel**](ChannelApi.md#channel_controller_create_channel) | **POST** /channel | 
[**channel_controller_get_accessible_channels**](ChannelApi.md#channel_controller_get_accessible_channels) | **GET** /channel/pubsub | 
[**channel_controller_get_channel**](ChannelApi.md#channel_controller_get_channel) | **GET** /channel/{fqcn} | 
[**channel_controller_remove_channel**](ChannelApi.md#channel_controller_remove_channel) | **DELETE** /channel/{fqcn} | 
[**channel_controller_update_channel**](ChannelApi.md#channel_controller_update_channel) | **PATCH** /channel | 


# **channel_controller_create_channel**
> str channel_controller_create_channel(create_channel_dto)



Creates a channel

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import channel_api
from dsb_client.model.create_channel_dto import CreateChannelDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): access-token
configuration = dsb_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_api.ChannelApi(api_client)
    create_channel_dto = CreateChannelDto(
        fqcn="testChannel.channels.dsb.apps.energyweb.iam.ewc",
        topics=[{"namespace":"testTopic","schema":"{\"type\": \"object\",\"properties\": {\"data\": {\"type\": \"string\"}},\"required\": [\"data\"],\"additionalProperties\": false}"}],
        admins=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52"],
        publishers=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52","user.roles.dsb.apps.energyweb.iam.ewc"],
        subscribers=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52","user.roles.dsb.apps.energyweb.iam.ewc"],
        max_msg_age=86400000000,
        max_msg_size=1000000,
    ) # CreateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_create_channel(create_channel_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling ChannelApi->channel_controller_create_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_channel_dto** | [**CreateChannelDto**](CreateChannelDto.md)|  |

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Created channel&#39;s name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_get_accessible_channels**
> [dict] channel_controller_get_accessible_channels()



Returns the list of accessible channels to publish or subscribe based on DID and verified-roles of the user

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import channel_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): access-token
configuration = dsb_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_api.ChannelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.channel_controller_get_accessible_channels()
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling ChannelApi->channel_controller_get_accessible_channels: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[dict]**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of channels with their options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_get_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} channel_controller_get_channel(fqcn)



Returns the requested channel's options

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import channel_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): access-token
configuration = dsb_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_api.ChannelApi(api_client)
    fqcn = "testChannel.channels.dsb.apps.energyweb.iam.ewc" # str | Fully Qualified Channel Name (fcqn)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_get_channel(fqcn)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling ChannelApi->channel_controller_get_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Fully Qualified Channel Name (fcqn) |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_remove_channel**
> str channel_controller_remove_channel(fqcn)



Removes the channel

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import channel_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): access-token
configuration = dsb_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_api.ChannelApi(api_client)
    fqcn = "testChannel.channels.dsb.apps.energyweb.iam.ewc" # str | Fully Qualified Channel Name (fcqn)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_remove_channel(fqcn)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling ChannelApi->channel_controller_remove_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Fully Qualified Channel Name (fcqn) |

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel deletion result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_update_channel**
> str channel_controller_update_channel(update_channel_dto)



Updates a channel

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import channel_api
from dsb_client.model.update_channel_dto import UpdateChannelDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): access-token
configuration = dsb_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_api.ChannelApi(api_client)
    update_channel_dto = UpdateChannelDto(
        fqcn="testChannel.channels.dsb.apps.energyweb.iam.ewc",
        topics=[{"namespace":"testTopic","schema":"{\"type\": \"object\",\"properties\": {\"data\": {\"type\": \"string\"}},\"required\": [\"data\"],\"additionalProperties\": false}"}],
        admins=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52"],
        publishers=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52","user.roles.dsb.apps.energyweb.iam.ewc"],
        subscribers=["did:ethr:0x5aEa5Bf5c5b341A0BFhryv5b51b77Fb9807F1b52","user.roles.dsb.apps.energyweb.iam.ewc"],
        max_msg_age=86400000000,
        max_msg_size=1000000,
    ) # UpdateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_update_channel(update_channel_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling ChannelApi->channel_controller_update_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_channel_dto** | [**UpdateChannelDto**](UpdateChannelDto.md)|  |

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

