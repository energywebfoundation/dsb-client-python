# dsb_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_login**](AuthApi.md#auth_controller_login) | **POST** /auth/login | 


# **auth_controller_login**
> LoginReturnDataDTO auth_controller_login(login_data_dto)



### Example

```python
import time
import dsb_client
from dsb_client.api import auth_api
from dsb_client.model.login_data_dto import LoginDataDTO
from dsb_client.model.login_return_data_dto import LoginReturnDataDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dsb_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_data_dto = LoginDataDTO(
        identity_token="identity_token_example",
    ) # LoginDataDTO | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.auth_controller_login(login_data_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_data_dto** | [**LoginDataDTO**](LoginDataDTO.md)|  |

### Return type

[**LoginReturnDataDTO**](LoginReturnDataDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

