# cda_client.AuthorizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cwms_data_auth_keys_with_key_name**](AuthorizationApi.md#delete_cwms_data_auth_keys_with_key_name) | **DELETE** /cwms-data/auth/keys/{key-name} | Delete cwmsData auth keys with keyName
[**get_cwms_data_auth_keys**](AuthorizationApi.md#get_cwms_data_auth_keys) | **GET** /cwms-data/auth/keys | Get cwmsData auth keys
[**get_cwms_data_auth_keys_with_key_name**](AuthorizationApi.md#get_cwms_data_auth_keys_with_key_name) | **GET** /cwms-data/auth/keys/{key-name} | Get cwmsData auth keys with keyName
[**post_cwms_data_auth_keys**](AuthorizationApi.md#post_cwms_data_auth_keys) | **POST** /cwms-data/auth/keys | Post cwmsData auth keys

# **delete_cwms_data_auth_keys_with_key_name**
> ApiKey delete_cwms_data_auth_keys_with_key_name(key_name, body=body)

Delete cwmsData auth keys with keyName

Delete API key for a user

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.AuthorizationApi(cda_client.ApiClient(configuration))
key_name = 'key_name_example' # str | 
body = cda_client.ApiKey() # ApiKey |  (optional)

try:
    # Delete cwmsData auth keys with keyName
    api_response = api_instance.delete_cwms_data_auth_keys_with_key_name(key_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->delete_cwms_data_auth_keys_with_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 
 **body** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_auth_keys**
> list[ApiKey] get_cwms_data_auth_keys()

Get cwmsData auth keys

View all keys for the current user

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.AuthorizationApi(cda_client.ApiClient(configuration))

try:
    # Get cwmsData auth keys
    api_response = api_instance.get_cwms_data_auth_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_cwms_data_auth_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiKey]**](ApiKey.md)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwms_data_auth_keys_with_key_name**
> ApiKey get_cwms_data_auth_keys_with_key_name(key_name)

Get cwmsData auth keys with keyName

View specific key

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.AuthorizationApi(cda_client.ApiClient(configuration))
key_name = 'key_name_example' # str | Name of the specific key to get more information for. NOTE: Case-sensitive.

try:
    # Get cwmsData auth keys with keyName
    api_response = api_instance.get_cwms_data_auth_keys_with_key_name(key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_cwms_data_auth_keys_with_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Name of the specific key to get more information for. NOTE: Case-sensitive. | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cwms_data_auth_keys**
> ApiKey post_cwms_data_auth_keys(body=body)

Post cwmsData auth keys

Create a new API Key for user. The randomly generated key is returned to the caller. A provided key will be ignored.

### Example
```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = cda_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: CwmsAAACacAuth
configuration = cda_client.Configuration()
configuration.api_key['JSESSIONIDSSO'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JSESSIONIDSSO'] = 'Bearer'

# create an instance of the API class
api_instance = cda_client.AuthorizationApi(cda_client.ApiClient(configuration))
body = cda_client.ApiKey() # ApiKey |  (optional)

try:
    # Post cwmsData auth keys
    api_response = api_instance.post_cwms_data_auth_keys(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_cwms_data_auth_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[ApiKey](../README.md#ApiKey), [CwmsAAACacAuth](../README.md#CwmsAAACacAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

