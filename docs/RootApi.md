# dsb_client.RootApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_controller_get_accessible_channels**](RootApi.md#app_controller_get_accessible_channels) | **GET** / | 


# **app_controller_get_accessible_channels**
> app_controller_get_accessible_channels()



Returns 200 response code with \"OK\"

### Example

```python
import time
import dsb_client
from dsb_client.api import root_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dsb_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = root_api.RootApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.app_controller_get_accessible_channels()
    except dsb_client.ApiException as e:
        print("Exception when calling RootApi->app_controller_get_accessible_channels: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

